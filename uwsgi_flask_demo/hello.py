import sys
import os
curpath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(curpath)

from flask import Flask
app = Flask(__name__)


@app.route("/", methods=['GET','POST'])
def hello():
	return "hello world !"

if __name__ == "__main__":
	app.run(host='127.0.0.1');
