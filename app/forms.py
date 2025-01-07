from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SelectField, DateTimeField, IntegerField
from wtforms.validators import DataRequired, Email, Length, EqualTo, Optional
from app.models import RepeatType

class LoginForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    remember_me = BooleanField('Ghi nhớ đăng nhập')

class RegistrationForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[
        DataRequired(),
        Length(min=3, max=64)
    ])
    email = StringField('Email', validators=[
        DataRequired(),
        Email(),
        Length(max=120)
    ])
    password = PasswordField('Mật khẩu', validators=[
        DataRequired(),
        Length(min=6)
    ])
    password2 = PasswordField('Xác nhận mật khẩu', validators=[
        DataRequired(),
        EqualTo('password', message='Mật khẩu không khớp')
    ])
    first_name = StringField('Tên', validators=[Length(max=64)])
    last_name = StringField('Họ', validators=[Length(max=64)])

class EventForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Mô tả')
    start_time = DateTimeField('Thời gian bắt đầu', validators=[DataRequired()])
    end_time = DateTimeField('Thời gian kết thúc', validators=[DataRequired()])
    location = StringField('Địa điểm', validators=[Length(max=200)])
    is_lunar = BooleanField('Lịch âm')
    is_all_day = BooleanField('Cả ngày')
    category_id = SelectField('Danh mục', coerce=int, validators=[Optional()])
    repeat_type = SelectField('Lặp lại', choices=[
        (RepeatType.NONE.value, 'Không lặp lại'),
        (RepeatType.DAILY.value, 'Hàng ngày'),
        (RepeatType.WEEKLY.value, 'Hàng tuần'),
        (RepeatType.MONTHLY.value, 'Hàng tháng'),
        (RepeatType.YEARLY.value, 'Hàng năm'),
        (RepeatType.LUNAR_MONTHLY.value, 'Hàng tháng âm lịch'),
        (RepeatType.LUNAR_YEARLY.value, 'Hàng năm âm lịch')
    ])
    repeat_interval = IntegerField('Khoảng lặp', default=1)
    repeat_end_date = DateTimeField('Kết thúc lặp lại', validators=[Optional()])
    reminder_minutes = IntegerField('Nhắc trước (phút)', validators=[Optional()])

class CategoryForm(FlaskForm):
    name = StringField('Tên danh mục', validators=[DataRequired(), Length(max=50)])
    color = StringField('Màu sắc', validators=[DataRequired(), Length(max=7)])
    description = TextAreaField('Mô tả', validators=[Length(max=200)])