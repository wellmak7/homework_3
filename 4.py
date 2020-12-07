def my_func(first_num, second_num):

    degree_result = first_num**second_num
    return degree_result

def my_func_2(first_num, second_num):
    degree_result = 1 / first_num

    for i in range (1, abs(second_num)):
        degree_result = degree_result / first_num

    return degree_result

first_arg = int(input('Введите первое положительное число (основание): '))
second_arg = int(input('Введите второе отрицательное число (показатель степени): '))

if (first_arg > 0) & (second_arg < 0):

    print("Возведение в степень: ", my_func(first_arg, second_arg))
    print("Возведение в степень: ", my_func_2(first_arg, second_arg))
else:
    print('Не соблюдены условия ввода!')