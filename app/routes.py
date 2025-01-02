from flask import render_template, abort, request, redirect, url_for, flash
from app import app, db
from app.models import Event
from datetime import datetime, timedelta, date
import calendar

# Hàm tiện ích để tạo calendar matrix
def create_calendar_matrix(year, month):
    """
    Tạo ma trận calendar cho tháng và năm được chỉ định
    Trả về list của list chứa các ngày trong tháng
    """
    cal = calendar.monthcalendar(year, month)
    return cal

# Context processor để inject các biến chung cho tất cả templates
@app.context_processor
def inject_dates():
    """
    Inject các biến ngày tháng cơ bản cho tất cả templates
    """
    today = datetime.now().date()
    return dict(
        today=today.strftime('%Y-%m-%d'),
        current_date=today,
        year=today.year,
        month=today.month,
        timedelta=timedelta  # Để sử dụng trong templates
    )

@app.route('/')
def home():
    """
    Trang chủ hiển thị:
    - Sự kiện hôm nay
    - Sự kiện sắp tới trong 7 ngày
    - Calendar tổng quan tháng hiện tại
    """
    today = datetime.now().date()
    # Lấy sự kiện hôm nay
    today_events = Event.query.filter_by(date=today).all()
    
    # Lấy sự kiện trong 7 ngày tới
    upcoming_events = Event.query.filter(
        Event.date > today,
        Event.date <= today + timedelta(days=7)
    ).order_by(Event.date).all()
    
    # Tạo calendar matrix cho tháng hiện tại
    calendar_matrix = create_calendar_matrix(today.year, today.month)
    
    return render_template('index.html',
                         today_events=today_events,
                         upcoming_events=upcoming_events,
                         calendar_matrix=calendar_matrix)

@app.route('/day/<date>')
def day_view(date):
    """
    Hiển thị view theo ngày
    date format: YYYY-MM-DD
    """
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        events = Event.query.filter_by(date=date_obj).order_by(Event.id).all()
        
        return render_template('day.html',
                             date=date_obj,
                             events=events)
    except ValueError:
        flash('Định dạng ngày không hợp lệ. Vui lòng sử dụng định dạng YYYY-MM-DD', 'error')
        return redirect(url_for('home'))

@app.route('/week/<date>')
def week_view(date):
    """
    Hiển thị view theo tuần
    date format: YYYY-MM-DD
    """
    try:
        date_obj = datetime.strptime(date, '%Y-%m-%d').date()
        # Tính ngày đầu tuần (Thứ 2)
        start_week = date_obj - timedelta(days=date_obj.weekday())
        # Tính ngày cuối tuần (Chủ nhật)
        end_week = start_week + timedelta(days=6)
        
        # Lấy tất cả sự kiện trong tuần
        events = Event.query.filter(
            Event.date >= start_week,
            Event.date <= end_week
        ).order_by(Event.date).all()
        
        # Tạo dictionary events theo ngày để dễ render
        events_by_date = {}
        for event in events:
            if event.date not in events_by_date:
                events_by_date[event.date] = []
            events_by_date[event.date].append(event)
        
        return render_template('week.html',
                             start_week=start_week,
                             end_week=end_week,
                             events=events,
                             events_by_date=events_by_date)
    except ValueError:
        flash('Định dạng ngày không hợp lệ', 'error')
        return redirect(url_for('home'))

@app.route('/month/<int:year>/<int:month>')
def month_view(year, month):
    """
    Hiển thị view theo tháng
    """
    try:
        # Validate month
        if not 1 <= month <= 12:
            raise ValueError("Tháng không hợp lệ")
            
        # Tạo calendar matrix
        calendar_matrix = create_calendar_matrix(year, month)
        
        # Lấy ngày đầu và cuối tháng
        first_day = date(year, month, 1)
        if month == 12:
            last_day = date(year + 1, 1, 1) - timedelta(days=1)
        else:
            last_day = date(year, month + 1, 1) - timedelta(days=1)
            
        # Lấy tất cả sự kiện trong tháng
        events = Event.query.filter(
            Event.date >= first_day,
            Event.date <= last_day
        ).order_by(Event.date).all()
        
        # Tạo dictionary events theo ngày
        events_by_date = {}
        for event in events:
            if event.date not in events_by_date:
                events_by_date[event.date] = []
            events_by_date[event.date].append(event)
        
        return render_template('month.html',
                             year=year,
                             month=month,
                             calendar_matrix=calendar_matrix,
                             events_by_date=events_by_date,
                             month_name=calendar.month_name[month])
    except ValueError as e:
        flash(str(e), 'error')
        return redirect(url_for('home'))

@app.route('/year/<int:year>')
def year_view(year):
    """
    Hiển thị view theo năm
    """
    try:
        # Lấy tất cả sự kiện trong năm
        start_date = date(year, 1, 1)
        end_date = date(year, 12, 31)
        
        events = Event.query.filter(
            Event.date >= start_date,
            Event.date <= end_date
        ).order_by(Event.date).all()
        
        # Tạo calendar matrix cho từng tháng
        calendar_matrices = {}
        for month in range(1, 13):
            calendar_matrices[month] = create_calendar_matrix(year, month)
            
        # Tổ chức events theo tháng
        events_by_month = {month: [] for month in range(1, 13)}
        for event in events:
            events_by_month[event.date.month].append(event)
            
        return render_template('year.html',
                             year=year,
                             calendar_matrices=calendar_matrices,
                             events_by_month=events_by_month)
    except ValueError:
        flash('Năm không hợp lệ', 'error')
        return redirect(url_for('home'))

# CRUD Operations cho Events
@app.route('/event/new', methods=['GET', 'POST'])
def new_event():
    """
    Tạo sự kiện mới
    """
    if request.method == 'POST':
        try:
            date_str = request.form.get('date')
            description = request.form.get('description')
            
            if not date_str or not description:
                raise ValueError("Vui lòng điền đầy đủ thông tin")
                
            date_obj = datetime.strptime(date_str, '%Y-%m-%d').date()
            
            event = Event(date=date_obj, description=description)
            db.session.add(event)
            db.session.commit()
            
            flash('Đã tạo sự kiện thành công', 'success')
            return redirect(url_for('day_view', date=date_str))
            
        except ValueError as e:
            flash(str(e), 'error')
            return redirect(url_for('new_event'))
            
    return render_template('event_form.html', event=None)

@app.route('/event/<int:id>/edit', methods=['GET', 'POST'])
def edit_event(id):
    """
    Chỉnh sửa sự kiện
    """
    event = Event.query.get_or_404(id)
    
    if request.method == 'POST':
        try:
            date_str = request.form.get('date')
            description = request.form.get('description')
            
            if not date_str or not description:
                raise ValueError("Vui lòng điền đầy đủ thông tin")
                
            event.date = datetime.strptime(date_str, '%Y-%m-%d').date()
            event.description = description
            
            db.session.commit()
            flash('Đã cập nhật sự kiện thành công', 'success')
            return redirect(url_for('day_view', date=date_str))
            
        except ValueError as e:
            flash(str(e), 'error')
            
    return render_template('event_form.html', event=event)

@app.route('/event/<int:id>/delete', methods=['POST'])
def delete_event(id):
    """
    Xóa sự kiện
    """
    event = Event.query.get_or_404(id)
    date_str = event.date.strftime('%Y-%m-%d')
    
    db.session.delete(event)
    db.session.commit()
    
    flash('Đã xóa sự kiện thành công', 'success')
    return redirect(url_for('day_view', date=date_str))

@app.errorhandler(404)
def not_found_error(error):
    """
    Xử lý lỗi 404
    """
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    """
    Xử lý lỗi 500
    """
    db.session.rollback()
    return render_template('500.html'), 500