import os
from datetime import date
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)

date = date.today()


@app.route("/")
@app.route("/home")
def home():
    # Landing page
    return render_template("index.html")


@app.route("/get_reviews", methods=["GET"])
def get_reviews():
    # Displays all reviews
    books = mongo.db.books.find()
    return render_template("allreviews.html", books=books)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username already exists.
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Informs user that the user name is already used
            flash("Username already taken, please choose another.")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "email": request.form.get("email"),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Put the user in session cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check to see if username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # hashed paassword matches?
            if check_password_hash(
                    existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}" .format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # invalid password
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            # invalid username
            flash("Invalid Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # grab the session user's username from the db
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        # Shows all reviews written by user
        books = mongo.db.books.find()
        return render_template("profile.html", books=books, username=username)

    return redirect(url_for("login"))


@app.route("/addreview", methods=["GET", "POST"])
def addreview():
    # This will add a new book review to the user db
    if 'user' in session:
        if request.method == "POST":
            # define our dict
            default_img = ("static/images/book.png")
            default_rating = "No Stars Awarded"
            book = {
                "title": request.form.get("title"),
                "author": request.form.get("author"),
                "genre": request.form.get("genre"),
                "buylink": request.form.get("buylink"),
                "imageurl": request.form.get("imageurl") or default_img,
                "synopsis": request.form.get("synopsis"),
                "review": request.form.get("review"),
                "createdby": session["user"],
                "rating": request.form.get("rating") or default_rating,
                "datecreated": date.strftime("%d %b %Y")
            }
            mongo.db.books.insert_one(book)
            flash("Book Successfully Added")
            return redirect(url_for("profile", username=session["user"]))

        return render_template("addreview.html")

    else:
        flash("You must log in first")
        return redirect(url_for("login"))


@app.route("/editreview/<booksid>", methods=["GET", "POST"])
def editreview(booksid):
    if request.method == "POST":
        # default values if fields are left blank
        default_url = ("https://www.bookdepository.com/")
        default_img = ("static/images/book.png")
        default_rating = "No Stars Awarded"
        update = {
            "title": request.form.get("title"),
            "author": request.form.get("author"),
            "genre": request.form.get("genre"),
            "published": request.form.get("published"),
            "cover": request.form.get("cover") or default_img,
            "buy": request.form.get("buy") or default_url,
            "synopsis": request.form.get("synopsis"),
            "review": request.form.get("review"),
            "rating": request.form.get("star") or default_rating,
            "created_by": session["user"],
            "date_created": date.strftime("%d %b %Y")
        }
        mongo.db.books.update({"_id": ObjectId(booksid)}, update)
        flash("Your review has been updated")
        return redirect(url_for("profile", username=session["user"]))

    books = mongo.db.books.find_one({"_id": ObjectId(booksid)})
    return render_template("editreview.html", books=books)


@app.route("/deletereview/<booksid>")
def deletereview(booksid):
    # Delete review
    mongo.db.books.remove({"_id": ObjectId(booksid)})
    flash("Review has been deleted")
    return redirect(url_for("profile", username=session["user"]))


@app.route("/deleteprofile/<userid>")
def deleteprofile(userid):
    # Delete user
    mongo.db.username.remove({"_id": ObjectId(userid)})
    flash("Account Deleted!!", "warning")
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    # remove user from session
    flash("You have been logged out.")
    session.pop("user")
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
