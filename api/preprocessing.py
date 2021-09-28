import os
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer
import re
nltk.download('wordnet')
reg_tok = RegexpTokenizer('\w+')
stop_nltk = stopwords.words('english')
wn_lemmatizer = WordNetLemmatizer()


def clean_and_lemmatize(text, tokenizer=reg_tok, stopw=stop_nltk, lemmatizer=wn_lemmatizer):
    # cleaning
    text = text.lower()
    text = re.sub(r'http\S+', " ", text)
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub(r'#\w+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'<.*?>', ' ', text)
    text = tokenizer.tokenize(text)

    # filtering
    text = [word for word in text if not word in stopw]

    # lemmatization
    text = ' '.join([lemmatizer.lemmatize(word) for word in text])
    return text


songs_artists = dict()
for i in os.listdir('C:/Users/apofi/flask_test/api/data'):
    try:
        with open(f"C:/Users/apofi/flask_test/api/data/{i}", encoding='utf-8', newline='') as f:
            lyrics = f.read()
            songs_artists[i[:-4]] = clean_and_lemmatize(lyrics)
    except:
        print(i)
