import common_info
def execute():
	common_info.print_common_info(__name__)
	a = input('Введите первое слово: ')
	b = input('Введите второе слово: ')
	print(a,b)
	a , b = b, a
	print(a,b)