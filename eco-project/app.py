from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = "eco-secret-key"

challenges = [
    "Take a 5-minute shower.",
    "Use no plastic today.",
    "Turn off unused lights.",
    "Bring a reusable bag.",
    "Recycle at least 3 items.",
    "Drink from a reusable water bottle.",
    "Eat one plant-based meal.",
    "Unplug unused devices."
]

@app.route("/", methods=["GET", "POST"])
def home():
    if "done" not in session:
        session["done"] = False

    challenge = session.get("challenge")

    if request.method == "POST":
        action = request.form.get("action")

        if action == "new":
            challenge = random.choice(challenges)
            session["challenge"] = challenge
            session["done"] = False

        elif action == "done":
            session["done"] = True

    return render_template(
        "index.html",
        challenge=challenge,
        done=session["done"]
    )

if __name__ == "__main__":
    app.run(debug=True)