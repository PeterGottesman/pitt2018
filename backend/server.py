#!/usr/bin/env python3

import db
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
print(db.getURI())
app.config["SQLALCHEMY_DATABASE_URI"] = db.getURI()
dbase = SQLAlchemy(app)

class Reviewer(dbase.Model):
    __tablename__ = "reviewers"
    reviewerID = dbase.Column("reviewerID", dbase.Integer, primary_key=True)
    lastName = dbase.Column("lastName", dbase.String)
    firstName = dbase.Column("firstName", dbase.String)
    specialty = dbase.Column("specialty", dbase.String)
    experience = dbase.Column("experience", dbase.String)
    authentication = dbase.Column("authentication", dbase.Integer)

    def __init__(self, lastName, firstName, specialty, experience, authentication):
        self.lastName = lastName
        self.firstName = firstName
        self.specialty = specialty
        self.experience = experience
        self.authentication = authentication

class Review(dbase.Model):
    __tablename__ = "reviews"
    ratingID = dbase.Column("ratingID", dbase.Integer, primary_key=True)
    url = dbase.Column("url", dbase.String)
    title = dbase.Column("title", dbase.String)
    author = dbase.Column("author", dbase.String)
    rating = dbase.Column("rating", dbase.Integer)
    reviewerID = dbase.Column("reviewerID", dbase.Integer)

    def __init__(self, url, title, author, rating, reviewerID):
        self.url = url
        self.title = title
        self.author = author
        self.rating = rating
        self.reviewerID = reviewerID

        
@app.route("/")
def hello():
    return "What are you doing Dave?"

@app.route("/addReview", methods=["POST"])
def setDBVals():
    json = request.get_json()
    if not json:
        return "Must send json\n"
    review = Review(json.get("url"), json.get("title"),
                    json.get("author"), json.get("rating"), json.get("reviewerID"))
    dbase.session.add(review)
    dbase.session.commit()
    return "Completed Successfully!\n"

@app.route("/getReviews", methods=["GET"])
def getDBVals():
    # url = request.args("url")
    res = Review.query.filter(Review.url.startswith(url)).all()
    for rev in res:
        print(rev.ratingID, rev.url, rev.title, rev.author, rev.rating, rev.reviewerID)
    return "yo!\n"
    
def reviewerExists(reviewerID):
    pass
    


# def main():


# main()
