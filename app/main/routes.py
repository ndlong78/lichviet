from flask import render_template, redirect, url_for, flash, request, jsonify, abort
from flask_login import login_user, logout_user, login_required, current_user
from datetime import datetime, timedelta
from calendar import monthrange
from app import app, db
from app.models import User, Event, Category, RepeatType, EventReminder, CalendarSharing
from app.forms import LoginForm, RegistrationForm, EventForm, CategoryForm
from app.utils import convert_to_lunar, get_lunar_date

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('calendar'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Tên đăng nhập hoặc mật khẩu không đúng', 'error')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('calendar'))
    return render_template('auth/login.html', title='Đăng nhập', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('calendar'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Chúc mừng, bạn đã đăng ký thành công!', 'success')
        return redirect(url_for('login'))
    return render_template('auth/register.html', title='Đăng ký', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

# Calendar Views
@app.route('/')
@app.route('/calendar')
@login_required
def calendar():
    year = request.args.get('year', datetime.now().year, type=int)
    month = request.args.get('month', datetime.now().month, type=int)
    
    start_date = datetime(year, month, 1)
    _, last_day = monthrange(year, month)
    end_date = datetime(year, month, last_day)
    
    events = Event.query.filter_by(user_id=current_user.id)\
        .filter(Event.start_time.between(start_date, end_date))\
        .all()
    
    return render_template('calendar/month.html', 
                         year=year, 
                         month=month, 
                         events=events)

@app.route('/calendar/week')
@login_required
def week_view():
    date = request.args.get('date', datetime.now().date().isoformat())
    current_date = datetime.strptime(date, '%Y-%m-%d')
    
    # Get start of week (Monday)
    week_start = current_date - timedelta(days=current_date.weekday())
    week_end = week_start + timedelta(days=6)
    
    events = Event.query.filter_by(user_id=current_user.id)\
        .filter(Event.start_time.between(week_start, week_end))\
        .all()
    
    return render_template('calendar/week.html', 
                         week_start=week_start,
                         week_end=week_end, 
                         events=events)

@app.route('/calendar/year')
@login_required
def year_view():
    year = request.args.get('year', datetime.now().year, type=int)
    
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    
    events = Event.query.filter_by(user_id=current_user.id)\
        .filter(Event.start_time.between(start_date, end_date))\
        .all()
    
    return render_template('calendar/year.html', 
                         year=year, 
                         events=events)

# Event CRUD
@app.route('/event/new', methods=['GET', 'POST'])
@login_required
def new_event():
    form = EventForm()
    form.category_id.choices = [(c.id, c.name) for c in 
                              Category.query.filter_by(user_id=current_user.id)]
    
    if form.validate_on_submit():
        event = Event(
            title=form.title.data,
            description=form.description.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            location=form.location.data,
            is_lunar=form.is_lunar.data,
            is_all_day=form.is_all_day.data,
            repeat_type=form.repeat_type.data,
            repeat_interval=form.repeat_interval.data,
            category_id=form.category_id.data,
            user_id=current_user.id
        )
        
        if form.repeat_end_date.data:
            event.repeat_end_date = form.repeat_end_date.data
            
        if form.reminder_minutes.data:
            reminder = EventReminder(
                event_id=event.id,
                notification_type='email',
                minutes_before=form.reminder_minutes.data
            )
            db.session.add(reminder)
            
        db.session.add(event)
        db.session.commit()
        flash('Sự kiện đã được tạo thành công!', 'success')
        return redirect(url_for('calendar'))
        
    return render_template('event/edit.html', 
                         title='Thêm sự kiện mới',
                         form=form)

@app.route('/event/<int:id>/edit', methods=['GET', 'POST'])
@login_required
def edit_event(id):
    event = Event.query.get_or_404(id)
    if event.user_id != current_user.id:
        abort(403)
        
    form = EventForm(obj=event)
    form.category_id.choices = [(c.id, c.name) for c in 
                              Category.query.filter_by(user_id=current_user.id)]
    
    if form.validate_on_submit():
        event.title = form.title.data
        event.description = form.description.data
        event.start_time = form.start_time.data
        event.end_time = form.end_time.data
        event.location = form.location.data
        event.is_lunar = form.is_lunar.data
        event.is_all_day = form.is_all_day.data
        event.repeat_type = form.repeat_type.data
        event.repeat_interval = form.repeat_interval.data
        event.category_id = form.category_id.data
        event.repeat_end_date = form.repeat_end_date.data
        event.reminder_minutes = form.reminder_minutes.data
        
        db.session.commit()
        flash('Sự kiện đã được cập nhật!', 'success')
        return redirect(url_for('calendar'))
        
    return render_template('event/edit.html',
                         title='Chỉnh sửa sự kiện',
                         form=form,
                         event=event)

@app.route('/event/<int:id>/delete', methods=['POST'])
@login_required
def delete_event(id):
    event = Event.query.get_or_404(id)
    if event.user_id != current_user.id:
        abort(403)
        
    db.session.delete(event)
    db.session.commit()
    flash('Sự kiện đã được xóa!', 'success')
    return redirect(url_for('calendar'))

# API Endpoints
@app.route('/api/events')
@login_required
def get_events():
    start = request.args.get('start')
    end = request.args.get('end')
    
    if start and end:
        start_date = datetime.fromisoformat(start)
        end_date = datetime.fromisoformat(end)
        events = Event.query.filter_by(user_id=current_user.id)\
            .filter(Event.start_time.between(start_date, end_date))\
            .all()
    else:
        events = Event.query.filter_by(user_id=current_user.id).all()
    
    return jsonify([event.to_dict() for event in events])

@app.route('/api/categories')
@login_required
def get_categories():
    categories = Category.query.filter_by(user_id=current_user.id).all()
    return jsonify([category.to_dict() for category in categories])

@app.route('/api/events/<int:id>', methods=['PUT'])
@login_required
def update_event_api(id):
    event = Event.query.get_or_404(id)
    if event.user_id != current_user.id:
        abort(403)
    
    data = request.get_json()
    for key, value in data.items():
        if hasattr(event, key):
            setattr(event, key, value)
    
    db.session.commit()
    return jsonify(event.to_dict())

# Error handlers
@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404

@app.errorhandler(403)
def forbidden_error(error):
    return render_template('errors/403.html'), 403

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('errors/500.html'), 500