# import os
# DATABASE_URL = os.getenv("postgres://u5dp727eq2oi62:p8ba350aa80a5611c6773b313fa181148da40eccc6e7b1764bcf9390caccad094@c9mq4861d16jlm.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d9okhhtcahgaeo")

from flask import Flask, render_template
app = Flask(__name__) # You pass the special variable __name__ that holds the name of the current Python module. It’s used to tell the instance where it’s located—you need this because Flask sets up some paths behind the scenes.

'''
Once you create the app instance, you use it to handle incoming web requests and send responses to the user.
@app.route is a decorator that turns a regular Python function into a Flask view function, which converts the function’s
return value into an HTTP response to be displayed by an HTTP client, such as a web browser.
You pass the value '/' to @app.route() to signify that this function will respond to web requests for the URL /, which is the main URL.
'''

@app.route('/')
def index():
    return render_template("index.html")


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/groups")
def groups():
    return render_template("groups.html")

@app.route("/chores")
def chores():
    return render_template("chores.html")

@app.route("/calender")
def calender():
    return render_template("calender.html")

@app.route("/messages")
def messages():
    return render_template("messages.html")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
