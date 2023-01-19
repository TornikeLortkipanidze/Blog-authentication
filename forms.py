from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired, URL, Email
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


class RegisterForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    email = StringField("Enter your email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    name = StringField("Enter your name", validators=[DataRequired()])
    email = StringField("Enter your email", validators=[DataRequired(), Email()])
    password = PasswordField("Enter your password", validators=[DataRequired()])
    submit = SubmitField("Submit")


class CommentForm(FlaskForm):
    body = CKEditorField("Comment field", validators=[DataRequired()])
    submit = SubmitField("Submit Comment")