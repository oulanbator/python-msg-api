from flask import Flask

app = Flask(__name__)

@app.route("/msg")
def hello_world():
    return "Hellowww"

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=80)