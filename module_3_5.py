def get_multiplied_digits(number):
    number = int(number)
    str_number = str(number)
    first = int(str_number[0])
    if len(str_number)>1:
        if int(str_number[-1]) == 0:
            return get_multiplied_digits(int(str_number[0:-1]))
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first

result = get_multiplied_digits('4025088')
print(result)



# result = get_multiplied_digits(40203) # запускает функцию с параметрами def get_multiplied_digits(*number)
# def get_multiplied_digits(4, 0, 2, 0, 3)
# работа функции
# str_number = str(number) # присваивает переменной str_number строчное значение параметров функции
# те должно быть так str_number = 40203
# first = int(str_number[0]) # - переменной first присваевается целочисленное значение строчной переменной
# str_number = 40203 , те должно быть 4
# где, Святая Корова, у меня ошибка
# что я не так понимаю?



