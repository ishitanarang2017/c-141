from flask import Flask, jsonify
import pandas as pd

movies_data = pd.read_csv('final.csv')

app = Flask(__name__)

# extracting important information from dataframe
all_movies = movies_data[["original_title" , "poster_link", "release_date" , "runtime" , "weighted_rating"]]

# variables to store data
likedmovies = []
dislikedmovies= []
didnotwatch = []

# method to fetch data from database
def assignval():
  mdata = {
      "original_title": all_movies.iloc[0,0],
      "poster_link":  all_movies.iloc[0,1],
      "release_date" : all_movies.iloc[0,2] or "n/a",
      "duration" :  all_movies.iloc[0,3],
      "rating" :  all_movies.iloc[0,4]/2
  }
  return mdata 


# /movies api
@app.route("/movies")
def getmovies():
  moviedata = assignval()
  return jsonify({
      "data":moviedata,
      "status": "success"
  })

# /like api
@app.route("/like",methods = ["POST"])
def likedmovie():
  global all_movies
  moviedata = assignval()
  likedmovies.append(moviedata)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
      "status":"success"
  })

# /dislike api
@app.route("/dislike",methods = ["POST"])
def dislikedmovie():
  global all_movies
  moviedata = assignval()
  dislikedmovies.append(moviedata)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
      "status":"success"
  })


# /did_not_watch api
@app.route("/did_not_watch",methods = ["POST"])
def didnotwatch():
  global all_movies
  moviedata = assignval()
  didnotwatch.append(moviedata)
  all_movies.drop([0],inplace = True)
  all_movies = all_movies.reset_index(drop = True)
  return jsonify({
      "status":"success"
  })


if __name__ == "__main__":
  app.run()