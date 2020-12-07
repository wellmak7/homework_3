def user_data(name, surname, birth_year, city, email, phone):
    print('Имя: ', name, 'Фамилия: ', surname, 'Год рождения: ', birth_year,
          'Город: ', city, 'Почта: ', email, 'Телефон: ', phone)

name = input('Введите имя: ')
surname = input('Введите фамилию: ')
birth_year = input('Год рождения: ')
city = input('Город: ')
email = input('Почта: ')
phone = input('Телефон: ')

user_data(name, surname, birth_year, city, email, phone)