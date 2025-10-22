from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField('İsim', validators=[DataRequired(), Length(max=120)])
    email = StringField('E-posta', validators=[DataRequired(), Email(), Length(max=200)])
    company = StringField('Şirket', validators=[Length(max=200)])
    message = TextAreaField('Mesaj', validators=[DataRequired(), Length(max=2000)])