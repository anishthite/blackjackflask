from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class BetForm(FlaskForm):
    betAmount = IntegerField('Bet Amount:', validators=[DataRequired()], render_kw={'autofocus': True})
    submit = SubmitField('Submit')

class ActionForm(FlaskForm):
    hit = SubmitField('Hit')
    stand = SubmitField('Stand')