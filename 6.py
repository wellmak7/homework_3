def upper_first_letter(word):

    word = word.split(" ")
    word_upper = []

    for el in word:
        el = el[0].upper() + el[1:]
        word_upper.append(el)

    word_upper = " ".join([str(i) for i in word_upper])

    return word_upper

input_word = input("Введите слово: ")
print(upper_first_letter(input_word))