from flask import Flask, abort, redirect, render_template, request, url_for

from posts import posts

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html", posts=posts)

@app.route("/success")
def success():
    return 'Successful Page'

@app.route("/post/<int:id>")
def post(id):
    post = posts[id - 1]
    if not post:
        abort(404)
    return render_template("post.html", post=post)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        if not name:
            abort(406, "Name is required")

        if not email:
            abort(406, "Email is required")

        return redirect(url_for("success"))

    return """
        <form method='POST'>
            <input type='text' name='name' />
            <input type='text' name='email' />
            <input type='submit' />
        </form>
    """

@app.route("/take_json", methods=["POST"])
def take_json():
    data = request.get_json()
    print(data.get('language'))

    return "JSON Test"



if __name__ == '__main__':
    app.run(debug=True)
