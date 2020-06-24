"""
Вам нужно написать морфологический анализатор выдуманного языка. 

В языке есть только имена и глаголы. Формообразование происходит так: к основе слова прибавляется суффикс. 

У имен есть только два падежа. Номинатив, у него нет своего суффикса, форма номинатива равна основе. Косвенный падеж
образуется с помощью суффикса "тыдыщ". Других грамматических показателей у существительных нет. Таким образом, у
именной основы тътгжш может быть только две формы: номинатив тътгжш и форма косвенного падежа тътгжштыдыщ.

У глаголов есть только категория времени. Форма настоящего времени не имеет выраженного показателя и равна
основе глагола. Показатель прошедшего времени "эго". Показатель будущего времени "рио".
Таким образом, слово "шыъгземйрио" -- это глагол "шыъгземй" в форме будущего времени.
"""

import json

with open("dict_S.json", "r") as read_file:
    dict_S = json.load(read_file)

with open("dict_V.json", "r") as read_file:
    dict_V = json.load(read_file)

test_text = open('Test_text.txt', 'r').read()


class Analysis:
    """
        Morphological analysis of the word.
    """

    def __init__(self, word):

        self.word = word
        self.wordClass = self.get_word_class(word)
        self.case = self.get_case(word)
        self.tense = self.get_tense(word)
        self.basis = self.get_basis(word)
        self.suffix = self.get_suffix(word)

    def get_basis(self, word):

        basis = None

        if word in dict_S or word in dict_V:
            basis = word
        elif word[-5:] == 'тыдыщ' and word.replace(word[-5:], '') in dict_S:
            basis = word.replace(word[-5:], '')

        elif (word[-3:] == 'эго' or word[-3:] == 'рио') and word.replace(word[-3:], '') in dict_V:
            basis = word.replace(word[-3:], '')
        else:
            basis = ''

        return basis

    def get_suffix(self, word):

        if word[-5:] == 'тыдыщ' and word.replace(word[-5:], '') in dict_S:
            suffix = word[-5:]
        elif (word[-3:] == 'эго' or word[-3:] == 'рио') and word.replace(word[-3:], '') in dict_V:
            suffix = word[-3:]
        else:
            suffix = ''

        return suffix

    def get_case(self, word):

        suffix = self.get_suffix(word)

        if self.wordClass == 'noun':
            if suffix == 'тыдыщ':
                case = 'oblique'
            else:
                case = 'nominative'
        else:
            case = 'Case is not defined for this word'

        return case

    def get_tense(self, word):

        suffix = self.get_suffix(word)

        if self.wordClass == 'verb':

            if suffix == 'рио':
                tense = 'future'
            elif suffix == 'эго':
                tense = 'past'
            elif suffix == '':
                tense = 'present'
        else:
            tense = 'tense is not defined for this word'

        return tense

    def get_word_class(self, word):

        word_class = 'ERROR! Unexpected class of word.'

        if word in dict_S:
            word_class = 'noun'
        elif word in dict_V:
            word_class = 'verb'

        elif self.get_suffix(word) == 'тыдыщ' and self.get_basis(word) in dict_S:
                word_class = 'noun'

        elif self.get_suffix(word) == 'рио' or self.get_suffix(word) == 'эго':
            if self.get_basis(word) in dict_V:
                word_class = 'verb'

        return word_class


'''
# Exception message:

my_word = Analysis(text[1])
print(my_word.word, my_word.wordClass)
print(my_word.case)
'''


test_text = dict_S[15] + 'тыдыщ' + ' ' + dict_V[12] + 'рио ' + dict_V[100] + '  ' + dict_S[
    100] + ' трялялятыдыщ' + ' риорио' + ' '


text = test_text.split(' ')
print('Test text: \n', test_text, '\n')
print('Analysis: \n')

for my_word in text:
    target_word = Analysis(my_word)
    print('target word: ', target_word.word, '\nword class: ', target_word.wordClass)

    if target_word.basis:
        print('word basis: ', target_word.basis)

    if target_word.wordClass == 'verb':
        print('tense: ', target_word.tense)

    if target_word.wordClass == 'noun':
        print('case: ', target_word.case)

    if target_word.suffix != '':
        print('suffix: ', target_word.suffix)

    print()
