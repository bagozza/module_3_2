def print_params(a=1, b='строка', c=True):
    print(a, b, c)


values_list = [7, True, 'A']
values_dict = {'a': 9, 'b': True, 'c': 'False'}
values_list_2 = [54.32, 'Строка']
print_params()
print_params(b=25, c=[1, 2, 3])
print_params(**values_dict)
print_params(*values_list)
print_params(*values_list_2, 42)
