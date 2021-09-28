import pandas as pd

from api.tfidf import artists_similarity
from api.preprocessing import songs_artists

df = pd.DataFrame(artists_similarity, index=songs_artists.keys(), columns=songs_artists.keys())
