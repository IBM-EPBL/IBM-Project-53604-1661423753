from flask import Flask,render_template

app = Flask(__name__)



@app.route("/")
def home():
    return  render_template("home.html")

@app.route("/about",methods=["POST","GET"])
def about():
    return render_template('about.html')

@app.route("/signin",methods=["POST","GET"])
def login():
    return render_template('login.html')

@app.route("/signup",methods=["POST","GET"])
def register():
    return render_template('register.html')


if __name__ == '_main_':
        app.run(debug=True)
