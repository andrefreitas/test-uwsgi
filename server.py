from flask import Flask
import ldclient
from ldclient.config import Config
import os

app = Flask(__name__)

LD_SDK_KEY = os.getenv('LD_SDK_KEY')

@app.route("/")
def index():
    import uwsgi # fails in flask
    print("Threads: ", uwsgi.opt.get('threads'))
    ldclient.set_config(Config(LD_SDK_KEY ))
    ld_client = ldclient.get()
    return "Hello world"

if __name__ == "__main__":
    app.run()