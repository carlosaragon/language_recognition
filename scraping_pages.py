import re
import wikipedia as wiki
from unidecode import unidecode
import numpy as np
import pandas as pd
import config


def process(page_content, max_word_length):
    words = re.sub(r'[^a-zA-Z ]', '', page_content)
    lower = words.lower()
    word_list = lower.split()
    short_words = []
    for word in word_list:
        if len(word) <= max_word_length:
            short_words.append(word)
    return short_words

def generate_dictionary(tag, max_word_length):

    wiki.set_lang(tag)
    for topic in config.language_tags[tag]:
        page = wiki.WikipediaPage(topic)
        content = page.content
        content = unidecode(content)
        lst = process(content, max_word_length)

    return lst


def convert_dic_to_vector(dic, max_word_length):
    new_list = []
    for word in dic:
        vec = ''
        n = len(word)
        for i in range(n):
            current_letter = word[i]
            ind = ord(current_letter)-97
            placeholder = (str(0)*ind) + str(1) + str(0)*(25-ind)
            vec = vec + placeholder
        if n < max_word_length:
            excess = max_word_length-n
            vec = vec + str(0)*26*excess
        new_list.append(vec)
    print(len(new_list))
    return new_list


def create_output_vector(tag_index, number_of_languages):
    out = str(0)*tag_index + str(1) + str(0)*(number_of_languages-1-tag_index)
    return out


word_data = []
language_data = []
master_dic = []

count = 0

for tag in config.language_tags.keys():
    print('generating dictionary for ' + tag)
    dic = generate_dictionary(tag, config.max_letters)
    for word in dic:
        master_dic.append(word)
    vct = convert_dic_to_vector(dic, config.max_letters)
    for vector in vct:
        word_data.append(vector)
    output_vct = create_output_vector(count, len(config.language_tags))
    for i in range(len(vct)):
        language_data.append(output_vct)
    count += 1

arr = []
for i in range(len(word_data)):
    entry = []
    entry.append(master_dic[i])
    for digit in language_data[i]:
        entry.append(float(digit))
    for digit in word_data[i]:
        entry.append(float(digit))
    arr.append(entry)


arr = np.array(arr)
np.save('arr.npy', arr)
df = pd.DataFrame(arr)
df.to_csv('data.csv')
