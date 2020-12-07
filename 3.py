def my_func(first_arg, second_arg, third_arg):
    sum_max_arg = first_arg + second_arg + third_arg - min(first_arg, second_arg, third_arg)
    return sum_max_arg

first_arg = int(input('Введите первый аргумент: '))
second_arg = int(input('Введите второй аргумент: '))
third_arg = int(input('Введите третий аргумент: '))

print("Сумма наибольших элементов: ", my_func(first_arg, second_arg, third_arg))