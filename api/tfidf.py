from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_distances

from api.preprocessing import songs_artists

tfidf = TfidfVectorizer(ngram_range=(1, 1))
print(songs_artists.values())
tfidf_representation = tfidf.fit_transform(songs_artists.values())
artists_similarity = 1 - pairwise_distances(tfidf_representation, metric="cosine")
print(len(artists_similarity))
print(artists_similarity)

