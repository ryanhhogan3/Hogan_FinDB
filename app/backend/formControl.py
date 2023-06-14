from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5

from flask_wtf import FlaskForm, CSRFProtect
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length
import secrets

class NameForm(FlaskForm):
    name = StringField('Which actor is your favorite?', validators=[DataRequired(), Length(10, 40)])
    submit = SubmitField('Submit')