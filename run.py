from vocabulus import app
from vocabulus.config import DEBUG

print(DEBUG)
if __name__ == '__main__':
	app.run(debug=DEBUG)
