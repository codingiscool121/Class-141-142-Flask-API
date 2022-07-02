from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
df3=pd.read_csv("final.csv")

#mean of average voters 
C=df3["vote_average"].mean()

#minimum vote=250
#quantile->% so 90% of vote
m=df3["vote_count"].quantile(0.9)

#loc=particular row/column
qmovies=df3.copy().loc[df3["vote_count"]>=m]
# print(qmovies.tail())
# print(qmovies.shape)

def weight_rating(x):
  v= x["vote_count"]
  R=x["vote_average"]
  return (v/(v+m)*R)+(m/(v+m)*C)

  #creating new column score
  #apply=applying the weight rating function to the qmovies
qmovies["score"]= qmovies.apply(weight_rating, axis=1)

qmovies=qmovies.sort_values("score", ascending=False)
# qmovies.head()

output=qmovies[["title_x", "posterlink", "release_date", "runtime", "vote_average", "overview"]].head(20).values.tolist()
print(output)

