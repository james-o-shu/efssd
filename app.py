import os

from flask import Flask, abort, flash, redirect, render_template, request, url_for

from forms import RegistrationForm
from posts import posts

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY") or "your-secrets-are-safe"


@app.route("/")
def home():
    return render_template("index.html.j2", posts=posts)

@app.route("/success")
def success():
    return 'Successful Page'

@app.route("/post/<int:id>")
def post(id):
    post = posts[id - 1]
    if not post:
        abort(404)
    return render_template("post.html.j2", post=post)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST":
        if form.validate_on_submit():
            flash(
                f'username ({form.username.data}) and email ({form.email.data}) submitted'
            )

            # name = request.form.get("name")
            # email = request.form.get("email")
            # if not name:
            #     abort(406, "Name is required")

            # if not email:
            #     abort(406, "Email is required")
            #
            return redirect(url_for("success"))
        else:
            print(form.errors)

    return render_template("register.html.j2", form=form)

@app.route("/take_json", methods=["POST"])
def take_json():
    data = request.get_json()
    print(data.get('language'))

    return "JSON Test"



if __name__ == '__main__':
    app.run(debug=True)
