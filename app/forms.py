
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField,EmailField,IntegerField
from wtforms.validators import DataRequired, Length, Email, ValidationError

from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
class AddbookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    page_counts = IntegerField('Page Counts', validators=[DataRequired()])
    submit = SubmitField('Add Book')
    def validate_author(self, author):
        author = User.query.filter_by(username=author.data).first()
        if author is None:
            raise ValidationError('Author not found.')
            return render_template('add_book.html', form=self)