from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
# set a secret key for security purposes
app.secret_key = 'april python class is the coolest'

# our index route will handle rendering our form


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    session['username'] = request.form['name']
    session['userlocation'] = request.form['location']
    session['userlanguage'] = request.form['language']
    session['usercomments'] = request.form['comments']
    return redirect("/result")

# adding this method


@app.route("/result")
def show_user():
    print("Showing the User Info From the Form")
    print(request.form)
    return render_template("result.html")

# clearing out session


@app.route("/clear")
def clear_session():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
