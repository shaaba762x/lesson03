#    Функция count_calls подсчитывающая вызовы остальных функций.
#     Функция string_info принимает аргумент - строку и возвращает кортеж из:
#     длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
#     Функция is_contains принимает два аргумента: строку и список,
#     и возвращает True, если строка находится в этом списке, False - если отсутствует.
#     Регистром строки при проверке пренебречь: UrbaN ~ URBAN.

calls = 0
a_result = False
string = 0
list_to_search = ['one', 'Two', 'ThRee', 'FOUR']
tuple_ = ()

def count_calls():
    global calls
    calls +=1
    return calls

def string_():
    global string
    string = str(input('Напишите по английски любое число (от 1 до 4)  :', ))
    return string

def string_info(string):
    global tuple_
    count_calls()
    len_str_ = str(len(string))
    string_B = string.upper()
    string_S = string.lower()
    tuple_ = (len_str_, string_B, string_S)
    return tuple_

def is_contains(string, list_to_search):
    count_calls()
    global a_result
    a_ = str(string).lower()
    b_ = str(list_to_search).lower()
    if a_ in b_:
        a_result = (True)
    else:
        a_result = (False)
        print('Написано не верно ', a_result)
    return a_result

while a_result == False:
    string_()
    string_info(string)
    is_contains(string, list_to_search)
    if a_result == True:
        continue
    else:
        print('-------------, ещё раз')
        continue

print(tuple_ )
print(a_result)
print(calls)




