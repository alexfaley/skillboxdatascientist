import common_info
def execute():
  common_info.print_common_info(__name__)

  username =  input('Введите имя пользователя: ')
  filename =  input('Введите имя файла: ')
  print('C:/'+username+'/docs/folder/'+filename)
  