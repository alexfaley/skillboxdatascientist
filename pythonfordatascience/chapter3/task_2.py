import common_info
def execute():
  common_info.print_common_info(__name__)

  red, green, blue = 'Red', 'Green', 'Blue'
  print(red,green,blue,red+green+blue,blue,green+blue)