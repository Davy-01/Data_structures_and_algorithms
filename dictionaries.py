import string

def word_frequency(sentence):
    sentence = sentence.translate(str.maketrans('', '', string.punctuation))

    sentence = sentence.lower()

    words = sentence.split()

    frequency_dict = {}