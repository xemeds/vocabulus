# Vocabulus

A web app to find new words given a relationship between two words.

# How it works

The vector representation of 50,000 words are loaded when the web app is started. Then whenever a word relation is submitted such as: `relation_word1`, `relation_word2` and `target_word`, the word of the closest vector to the vector calculation `relation_word1 - relation_word2 + target_word` is given to the user.

# Run locally

**Highly encouraged to create a python environment first.**

Clone the repository:

	$ git clone https://github.com/xemeds/vocabulus.git

Move into the cloned folder and install the required libraries:

	$ cd vocabulus
	$ pip install -r requirements.txt

After that run with:

	$ python run.py

Visit the below URL to view the flask app:

	127.0.0.1:5000

# Deploying

If you do not have a dedicated server, I highly recommend using [Linode](https://www.linode.com/), [Heroku](https://www.heroku.com/) or [PythonAnywhere](https://www.pythonanywhere.com/) to host your application.

Before deploying, make sure to set the following environment variables:

	$ export SECRET_KEY=
	$ export DEBUG=

If not they will default to the following values:

	SECRET_KEY=SECRET_KEY
	DEBUG=true

# References

The vec2word wordlist: [CS50AI/Lecture 6/vectors](https://cdn.cs50.net/ai/2020/spring/lectures/6/src6/vectors/words.txt)

# License

This project is under the [MIT](https://github.com/xemeds/vocabulus/blob/master/LICENSE) license.
