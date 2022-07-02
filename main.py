from flask import Flask, jsonify
import csv
from contentBased import getRecommendations
from demographic import output 
from storage import all_movies, didnotmatch, likemovies, notlikedmovies


app = Flask(__name__)


@app.route("/")

def index():
    return "Homepage"

@app.route("/get_movies")
def get_movies():
    movies_all={
        "title": all_movies[0][8],
        "posterlinks":all_movies[0][27],
        "duration":all_movies[0][15],
        "overview":all_movies[0][9],
        "releasedate":all_movies[0][13],
        "rating":all_movies[0][20]
    }
    return jsonify({
        "data" : movies_all,
        "status" : "good"
    })

@app.route("/liked_moves",methods=["POST"])

def moviesLiked():
    movie=all_movies[0]
    likemovies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"cool"
    }),200

@app.route("/notliked",methods=["POST"])
def notLiked():
    movie=all_movies[0]
    notlikedmovies.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"cool"
    }),200

@app.route("/not_matched",methods=["POST"])
def didnotmatch():
    movie=all_movies[0]
    didnotmatch.append(movie)
    all_movies.pop(0)
    return jsonify({
        "status":"cool"
    }),200

@app.route("/popular_movies",methods=["GET"])

def popularMovie():
    movie=[]
    for i in output:
        d={
        "title": i[0],
        "posterlinks": i[1],
        "duration": i[3],
        "overview": i[5],
        "releasedate": i[2],
        "rating": i[4]
        }
    movie.append(d)
    return jsonify({
        "data": movie, 
        "status":"success"
    })



if __name__ == "__main__" :
    app.run(debug = True)