from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = "portfolio-secret-key"


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/skills")
def skills():
    return render_template("skills.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/education")
def education():
    return render_template("education.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        name = request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")

        if not name or not email or not message:
            flash("Please fill all required fields.", "error")
            return redirect("/contact")

        # Later we can save this into MySQL
        print("Name:", name)
        print("Email:", email)
        print("Subject:", subject)
        print("Message:", message)

        flash("Your message has been sent successfully!", "success")
        return redirect("/contact")

    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)