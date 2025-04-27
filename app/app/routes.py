from flask import Blueprint, render_template

main = Blueprint("main", __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/blog")
def blog():
    posts = [
        {"title": "Welcome to Lablan Technologies", "content": "We build tech for the future."},
        {"title": "Update: New AI Project", "content": "We're launching a new AI initiative next month."}
    ]
    return render_template("blog.html", posts=posts)
