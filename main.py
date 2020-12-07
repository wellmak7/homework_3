def division(numerator, denominator):
    try:
        div_result = numerator / denominator
    except ZeroDivisionError:
        return print ('Деление на ноль запрещено!')
    return div_result


numerator = int(input('Введите числитель: '))
denominator = int(input('Введите знаменатель: '))

print('Результат деления: ', division(numerator, denominator))
