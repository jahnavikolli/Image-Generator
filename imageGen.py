from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = '324f110817440d7f9dad1effd3e0b70b'


@app.route("/")

@app.route("/home")
def home():
    return "<p>Hello, World!</p>"

if __name__ == '__main__':
   app.run()