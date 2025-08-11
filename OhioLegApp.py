from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "secret_key_for_session"

submissions = []

@app.route("/", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        age = request.form.get("age", "").strip()
        title = request.form.get("title", "").strip()
        hometown = request.form.get("hometown", "").strip()

        if not name:
            flash("Name is required.")
        if not title:
            flash("Title is required.")

        if not name or not title:
            return render_template("entry.html")

        entry = {"name": name, "age": age, "title": title, "hometown": hometown}
        submissions.append(entry)
        return redirect(url_for("confirmation", index=len(submissions) - 1))

    return render_template("entry.html")


@app.route("/confirmation/<int:index>")
def confirmation(index):
    entry = submissions[index]
    return render_template("confirmation.html", entry=entry, submissions=submissions)


if __name__ == "__main__":
    app.run(debug=True)
