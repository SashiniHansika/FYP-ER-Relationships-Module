import nltk
from nltk.corpus import stopwords
# from utils.file_manipulation import input_text
from pre_process import pronouns_resolution

stopWords = set(stopwords.words('english'))
lemmatizer = nltk.WordNetLemmatizer()
stemmer = nltk.PorterStemmer()
new_input_text = pronouns_resolution.pronouns_resolution()


def text_into_sentence():
    nltk.sent_tokenize(new_input_text)
    print("***************************")
    print(new_input_text)
    return nltk.sent_tokenize(new_input_text)


def sentences_into_word(sentence):
    word = nltk.word_tokenize(sentence)
    return word
