from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np
df3=pd.read_csv("final.csv")
df3=df3[df3["tags"].notna()]
vector=CountVectorizer(stop_words= "english")
matrix=vector.fit_transform(df3["tags"])

sim_score= cosine_similarity(matrix,matrix)
df3= df3.reset_index()
indice= pd.Series(df3.index, index=df3["title_x"])


def getRecommendations(title, cosine_sim):
  idx= indice[title]
  sim_score= list(enumerate(cosine_sim[idx]))
  sim_score= sorted(sim_score, key=lambda x:x[1], reverse=True)
  print(sim_score)
  print(sim_score)
  movies=sim_score[1:11]
  movie_indices=[i[0] for i in movies]

  return df3[["title_x", "posterlink", "release_date", "runtime", "vote_average", "overview"]].iloc[movie_indices].tolist()

