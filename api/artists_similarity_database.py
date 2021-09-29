import pandas as pd

from api.core.tf_idf import artists_similarity
from api.core.cleaner import songs_artists

df = pd.DataFrame(artists_similarity, index=songs_artists.keys(), columns=songs_artists.keys())
