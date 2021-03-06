#!/usr/bin/env python3

import db
from flask import Flask, request, jsonify
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
    return "Just what do you think you are doing Dave?"

@app.route("/addReview", methods=["POST"])
def setDBVals():
    review = Review(request.form["url"], request.form["title"],
                    request.form["author"], request.form["rating"], request.form["reviewerID"])
    dbase.session.add(review)
    dbase.session.commit()
    return "Completed Successfully!\n"

@app.route("/getReviews/byURL", methods=["GET"])
def getDBVals():
    url = request.args.get("url")
    exact = request.args.get("exact")
    if exact == "True":
        res = Review.query.filter(Review.url == url)
    else:
        res = Review.query.filter(Review.url.startswith(url))
    jsonOut = '{"ratings" : ['
    for rev in res:
        reviewerRes = Reviewer.query.filter(Reviewer.reviewerID == rev.reviewerID)
        jsonOut += '{'
        jsonOut += '"rating" : "' + str(rev.rating)
        jsonOut += '","reviewer" : "Dr. ' + reviewerRes[0].lastName
        jsonOut += '"},'
    jsonOut = jsonOut[:-1]
    jsonOut += "]}"
    return jsonOut
    

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
    return response
        
