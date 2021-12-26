from flask import render_template, redirect, url_for
from vocabulus import app
from vocabulus.words import words, closest_word
from vocabulus.forms import WordForm

# Index route
@app.route("/", methods=['GET', 'POST'])
def index():
	# Create a instance of the form
	form = WordForm()

	# If the form was valid
	if form.validate_on_submit():
		# TODO
		# Return the index page with the form
		return render_template("index.html", form=form)

	# Else if the form was invalid or not submitted
	else:
		# Return the index page with the form
		return render_template("index.html", form=form)

# Error handling routes
@app.errorhandler(404)
def error_404(error):
	return render_template("error.html", error_code=404, error_message="Not Found"), 404

@app.errorhandler(500)
def error_500(error):
	return render_template("error.html", error_code=500, error_message="Internal Server Error"), 500
