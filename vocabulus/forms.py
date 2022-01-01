from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, ValidationError
from wtforms.validators import DataRequired, Length, Optional
from vocabulus.words import words

# Validates a word
def validate_word(form, field):
	# Make sure the word is not too short or long
	if len(field.data) < 1 or len(field.data) > 100:
		return

	# Remove the spaces in the word and make it lowercase
	field.data = field.data.replace(" ", "").lower()

	# Check if the word exists in the word list
	try:
		words[field.data]
	except KeyError:
		raise ValidationError("Word does not exists in the system")

class WordForm(FlaskForm):
	target_word = StringField(validators=[DataRequired(), Length(min=1, max=100, message="Invalid word length"), validate_word])

	relation_word1 = StringField(validators=[DataRequired(), Length(min=1, max=100, message="Invalid word length"), validate_word])

	relation_word2 = StringField(validators=[DataRequired(), Length(min=1, max=100, message="Invalid word length"), validate_word])

	submit = SubmitField("=")
