from flask import render_template
from datetime import datetime, timedelta
from calendar import monthcalendar
from app.main import main
from app.models import Event
from app.utils.date_utils import get_lunar_date

@main.route('/calendar/month/<int:year>/<int:month>')
def month_view(year=None, month=None):
    if year is None or month is None:
        today = datetime.now()
        year = today.year
        month = today.month

    # Tính toán tháng trước và tháng sau
    first_day = datetime(year, month, 1)
    if month == 1:
        prev_month = datetime(year-1, 12, 1)
    else:
        prev_month = datetime(year, month-1, 1)
    
    if month == 12:
        next_month = datetime(year+1, 1, 1)
    else:
        next_month = datetime(year, month+1, 1)

    # Lấy dữ liệu lịch
    calendar_data = get_month_calendar(year, month)
    
    # Context cho template
    context = {
        'year': year,
        'month': month,
        'month_name': get_vietnamese_month_name(month),
        'calendar_data': calendar_data,
        'prev_month': prev_month,
        'next_month': next_month,
        'today': datetime.now().date()
    }
    
    return render_template('calendar/month.html', **context)

# Utility functions for templates
@main.app_template_filter('lunar_date')
def lunar_date_filter(date):
    """Convert solar date to lunar date"""
    return get_lunar_date(date)

@main.app_context_processor
def utility_processor():
    def get_events_for_date(date):
        """Get events for a specific date"""
        return Event.query.filter(
            Event.start_time >= date,
            Event.start_time < date + timedelta(days=1)
        ).all()
    
    def is_today(date):
        """Check if date is today"""
        return date.date() == datetime.now().date()
    
    def is_other_month(date, current_month):
        """Check if date is from another month"""
        return date.month != current_month
    
    return dict(
        get_events_for_date=get_events_for_date,
        is_today=is_today,
        is_other_month=is_other_month
    )