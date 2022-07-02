import csv

with open("final.csv", encoding="utf-8") as f:
    reader=csv.reader(f)
    data=list(reader)
    all_movies=data[1:]

likemovies=[]
notlikedmovies=[]
didnotmatch=[]

