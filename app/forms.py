from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.fields import DateTimeLocalField, ColorField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional, ValidationError
from app.models import User, RepeatType

class LoginForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired()])
    password = PasswordField('Mật khẩu', validators=[DataRequired()])
    remember_me = BooleanField('Ghi nhớ đăng nhập')
    submit = SubmitField('Đăng nhập')

class RegistrationForm(FlaskForm):
    username = StringField('Tên đăng nhập', validators=[DataRequired(), Length(min=3, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Mật khẩu', validators=[DataRequired(), Length(min=6)])
    password2 = PasswordField('Nhập lại mật khẩu', validators=[DataRequired(), EqualTo('password')])
    first_name = StringField('Tên', validators=[Optional(), Length(max=64)])
    last_name = StringField('Họ', validators=[Optional(), Length(max=64)])
    submit = SubmitField('Đăng ký')

    def validate_username(self, field):
        user = User.query.filter_by(username=field.data).first()
        if user is not None:
            raise ValidationError('Tên đăng nhập đã tồn tại.')

    def validate_email(self, field):
        user = User.query.filter_by(email=field.data).first()
        if user is not None:
            raise ValidationError('Email đã được sử dụng.')

class EventForm(FlaskForm):
    title = StringField('Tiêu đề', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Mô tả')
    start_time = DateTimeLocalField('Thời gian bắt đầu', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    end_time = DateTimeLocalField('Thời gian kết thúc', format='%Y-%m-%dT%H:%M', validators=[DataRequired()])
    location = StringField('Địa điểm', validators=[Optional(), Length(max=200)])
    is_lunar = BooleanField('Lịch âm')
    is_all_day = BooleanField('Cả ngày')
    category_id = SelectField('Danh mục', coerce=int, validators=[Optional()])
    repeat_type = SelectField('Lặp lại', choices=[(t.name, t.value) for t in RepeatType], validators=[Optional()])
    repeat_interval = IntegerField('Khoảng lặp lại', validators=[Optional()])
    repeat_end_date = DateTimeLocalField('Ngày kết thúc lặp lại', format='%Y-%m-%dT%H:%M', validators=[Optional()])
    reminder_minutes = SelectField('Nhắc nhở trước', 
                                 choices=[(0, 'Không nhắc'), (5, '5 phút'), (15, '15 phút'), 
                                        (30, '30 phút'), (60, '1 giờ'), (1440, '1 ngày')],
                                 coerce=int)
    submit = SubmitField('Lưu')

class CategoryForm(FlaskForm):
    name = StringField('Tên danh mục', validators=[DataRequired(), Length(max=50)])
    color = ColorField('Màu sắc', default='#3498db')
    description = TextAreaField('Mô tả', validators=[Optional(), Length(max=200)])
    submit = SubmitField('Lưu')