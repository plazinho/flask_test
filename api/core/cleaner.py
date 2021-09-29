import os
import re

import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import RegexpTokenizer

nltk.download('wordnet')
nltk.download('stopwords')

reg_tok = RegexpTokenizer('\w+')
stop_nltk = stopwords.words('english')
wn_lemmatizer = WordNetLemmatizer()


def clean_and_lemmatize(text: str, tokenizer=reg_tok, stopw=stop_nltk, lemmatizer=wn_lemmatizer) -> str:
    """
    Предобработка текстов песен исполнителя
    :param text: принимает на вход строку - файл с текстами всех песен исполнителя.
    :param tokenizer: токенизатор
    :param stopw: стоп-слова
    :param lemmatizer: лемматизатор
    :return: возвращает строку, состоящую из обработанных слов
    """
    # cleaning
    text = text.lower()
    text = re.sub(r'http\S+', " ", text)
    text = re.sub(r'@\w+', ' ', text)
    text = re.sub(r'#\w+', ' ', text)
    text = re.sub(r'\d+', ' ', text)
    text = re.sub(r'<.*?>', ' ', text)

    # tokenining
    text = tokenizer.tokenize(text)

    # filtering from stopwords
    #    text = [word for word in text if not word in stopw] # try with or without stopwords

    # lemmatization
    text = ' '.join([lemmatizer.lemmatize(word) for word in text])
    return text


songs_artists = dict()
for artist in os.listdir('../../api/data/raw_data'):
    try:
        with open(f"../../api/data/raw_data/{artist}", encoding='utf-8', newline='') as f:
            lyrics = f.read()
            songs_artists[artist[:-4]] = clean_and_lemmatize(lyrics)
    except:
        print(f"Some exception for '{artist}'")
