from keras.models import Sequential
from keras.layers import Dense
from config import convert_dic_to_vector
from config import max_letters, language_tags
import numpy as np

network = Sequential()
network.add(Dense(200, input_dim=26*max_letters-1, activation='sigmoid'))
network.add(Dense(150, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(100, activation='sigmoid'))
network.add(Dense(len(language_tags), activation='softmax'))
network.load_weights('weights.hdf5')
network.compile(loss='binary_crossentropy',
                optimizer='sgd', metrics=['accuracy'])


print('Bem vindo! Esse é o sistema de predição de idioma!')

while True:
    dic = []
    valid = False
    print('Os idiomas disponiveis atualmente são: ')
    print('Alemão, Ingles, Frances, Tcheco e Sueco')
    while not valid:
        word = input('Entre com uma palavra para prever o idioma dela:\n')
        if len(word) <= max_letters:
            word = word.lower()
            valid = True
        else:
            print('A alavra deve ter menos de ' +
                  str(max_letters + 1) + ' caracteres')
    dic.append(word)
    vct_str = convert_dic_to_vector(dic, max_letters)
    vct = np.zeros((1, 26 * max_letters-1))
    count = 0
    for digit in vct_str[0]:
        vct[0, count-1] = int(digit)
        count += 1
    prediction_vct = network.predict(vct)

    langs = list(language_tags.keys())
    for i in range(len(language_tags)):
        lang = langs[i]
        score = prediction_vct[0][i]
        print(lang + ': ' + str(round(100*score, 2)) + '%')
    print('\n')
