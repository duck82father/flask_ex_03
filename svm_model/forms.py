from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class QuestionForm(FlaskForm):
    subject = StringField('3P', validators=[DataRequired('필수입력 항목')])
    content = StringField('BLK', validators=[DataRequired('필수입력 항목')])

class AnswerForm(FlaskForm):
    content = TextAreaField('POSITION', validators=[DataRequired('내용은 필수입력 항목입니다.')])

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('password2', '비밀번호가 일치하지 않습니다')])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired('이메일은 필수입력 항목입니다.'), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('사용자이름', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired()])

class HobbyForm(FlaskForm):
    username = StringField('이름', validators=[DataRequired('이름을 입력해주세요.'), Length(min=3, max=25)])
    age = StringField('나이', validators=[DataRequired('나이를 입력해주세요')])
    purpose = StringField('취미의 목적', validators=[DataRequired('취미의 목적을 입력해주세요.')])
    hobby1 = StringField('관람 (영화, 공연, 전시회)')
    hobby2 = StringField('공부 (어학, 자격증, 독서)')
    hobby3 = StringField('운동 (수영, 헬스, 필라테스, 조깅)')
    hobby4 = StringField('기타 (봉사활동, 웹툰보기, 게임)')
    email = EmailField('이메일', validators=[DataRequired('이메일을 입력해주세요.'), Email()])