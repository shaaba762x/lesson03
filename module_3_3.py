def  print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_params()
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [1, 'Строка', False]
values_dict = {'a' : 25, 'b' : 'Колонка', 'c' : True}
print_params(*values_list)
print_params(**values_dict)

values_list_2 = [44, 'Космос']
print_params(*values_list_2, 42)