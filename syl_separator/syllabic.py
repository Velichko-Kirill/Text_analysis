# Подаём интересующие слова списком.
# test_words = ['корабль', 'кремль', 'маяк', 'трава', 'ответ', 'Представительство', 'Илья',
#              'дизъюнкция', 'ГЕКСАКОСИОЙГЕКСЕКОНТАГЕКСАФОБИЯ']

word = input('Enter your word please: ')


def count_syl(word):
    """
        Takes a word as an argument and return a list with syllable characteristics.
    """

    # We translate all the words into lower case and trim punctuation marks
    word = word.strip('.').strip(',').lower()

    vowels = ["а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]
    consonants = ["б", "в", "г", "д", "ж", "з", "к", "л", "м", "н", "п", "р", "с", "т", "ф", "х", "ц", "ч", "ш", "щ"]
    signs = ["ъ", "ь"]

    syllables = []  # General list for syllables
    syl = ''  # For syllable
    start = 0  # Start index
    length = len(word)

    while start < length:
        i = start

        while i < length - 1 and word[i] not in vowels:
            syl += word[i]
            i += 1

        # Meet the vowel and add it.

        if i == length - 1:
            if word[i] in consonants:
                syl += word[i]
                syllables[-1] += syl
                syl = ''
            else:
                syl += word[i]

        else:
            syl += word[i]

            # Next, check the following letters:

            if word[i + 1] not in vowels:
                if i < length - 2:
                    if word[i + 2] in consonants:
                        syl += word[i + 1]
                        if i < length - 3:
                            if word[i + 3] in signs:
                                syl += word[i + 2] + word[i + 3]
                if i < length - 2:
                    if word[i + 2] in signs:
                        syl += word[i + 1] + word[i + 2]

        syllables.append(syl)  # Add syllable in our list
        start += len(syl)
        if len(syl) == 0:
            del syllables[-1]
            break
        syl = ''  # 'Zero out' the syllable for subsequent iterations.

    print(syllables)
    syl_char = []
    for i in range(len(syllables)):
        if syllables[i][-1] in consonants or syllables[-1] in signs:
            syl_char.append('closed')
        elif syllables[i][-1] in vowels:
            syl_char.append('opened')

    return syl_char

print(count_syl(word))
