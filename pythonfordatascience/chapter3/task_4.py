import common_info
def execute():
  common_info.print_common_info(__name__)

  name = input('Введите ваше имя: ')
  surname = input('Введите вашу фамилию: ')
  city = input('Введите ваш город: ')
  print('='*15)
  print('Вас зовут', name,surname)
  print('Ваш город',city)