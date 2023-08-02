from flask import Flask, render_template, request
from lib import pslo_work
import datetime

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route('/', methods = ['GET', 'POST'])
def pslo():
    orig = request.form.get('pstype')
    result = pslo_work.pslo(orig, "enxa", 0, 0, 0, "", "", "", 0, False, 0, False)
    pshis += orig + " → " + result + " | " + datetime.datetime.now().strftime('%H:%M:%S') + "\n"
    return render_template("index.html", pslo_result = result, history = pshis, pstype_input = orig)

if __name__ == "__main__":
    app.run()