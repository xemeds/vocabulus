from flask import render_template, redirect, url_for
from vocabulus import app
# from vocabulus.forms import FORMS

# Index route
@app.route("/", methods=['GET', 'POST'])
def index():
	return render_template("index.html")

# Error handling routes
@app.errorhandler(404)
def error_404(error):
	return render_template("index.html"), 404

@app.errorhandler(500)
def error_500(error):
	return render_template("index.html"), 500