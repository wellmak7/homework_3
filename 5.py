def string_sum(string):
    string = string.split(" ")
    sum_el = 0

    try:
        for el in string:
            el = int(el)
            sum_el = sum_el + el
    except ValueError:
        return sum_el
    return sum_el

input_string = input('Введите числа через пробел: ')

print("Сумма чисел: ", string_sum(input_string))

second_input_string = input('Введите числа через пробел (подсчёт суммы завершится при введении символа, отличного от числа): ')

print("Сумма чисел: ", string_sum(input_string) + string_sum(second_input_string))