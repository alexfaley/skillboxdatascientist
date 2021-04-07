import common_info
def execute():
  common_info.print_common_info(__name__)

  departure = input('Откуда хотите вылететь: ')
  arrive = input('Откуда хотите прилететь: ')
  print('Ваш рейс: ',departure+'-'+arrive)
  
