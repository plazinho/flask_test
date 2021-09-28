from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from api.preprocessing import songs_artists

tfidf = TfidfVectorizer(ngram_range=(1, 4))
tfidf_representation = tfidf.fit_transform(songs_artists.values())
artists_similarity = cosine_similarity(tfidf_representation)
