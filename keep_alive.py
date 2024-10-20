from flask import Flask,render_template
from threading import Thread

app = Flask(__name__)

@app.route('/')
def index():
    return "I'm Gay!"

def run():
  app.run(host='195.200.15.246',port=8080)

def keep_alive():  
    t = Thread(target=run)
    t.start()
