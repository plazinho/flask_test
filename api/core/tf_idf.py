from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
from api.core.cleaner import songs_artists

tfidf = TfidfVectorizer(ngram_range=(1, 4))
tfidf_representation = tfidf.fit_transform(songs_artists.values())

artists_similarity = cosine_similarity(tfidf_representation)

pd.DataFrame(artists_similarity, index=songs_artists.keys(), columns=songs_artists.keys()).to_csv("../../api/data/TF_IDF.csv")
