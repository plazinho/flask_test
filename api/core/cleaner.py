import nltk
import re
from nltk.stem import WordNetLemmatizer

def clean_lemm_general(text_general):

    nltk.download('wordnet')
    def clean(text):

        text_clean_pre = text.lower()  # приводим все символы к нижнему регистру
        text_clean_pre = re.sub(r'\d+', '', text_clean_pre)  # удаляем все числа
        text_clean_pre = re.sub(r'[^\w\s]','', text_clean_pre)  # удаляем все знаки препинания
        text_clean_pre = re.sub(r'http\S+',"", text_clean_pre)
        text_clean_pre = re.sub(r'@\w+', '', text_clean_pre)
        text_clean_pre = re.sub(r'#\w+', '', text_clean_pre)
        return text_clean_pre

    text_clean_gen = [clean(i) for i in text_general.split()]
    text_lem = WordNetLemmatizer()
    lem_text = []
    for words in text_clean_gen:
        lem_text.append(' '.join([text_lem.lemmatize(word) for word in words.split()]))
    return ' '.join(lem_text)