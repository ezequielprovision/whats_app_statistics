from datetime import datetime as dt
import calendar


def user_name_generator(text_line):
  aux = 0
  result = ""
  for x in text_line:
    if aux == 3:  ### AUX ACOUNTS NUMBER OF ' ', WHEN = 3, THE USER NAME STARTS  
      result += x
      if result[-1] == ":": ### IF RESULT = 'Gabriel Alberto:'
        result = result.strip(":") ### REMOVES THE ':'
        return result
    elif x == " ":
      aux += 1

  """
  try:
    result = re.search(r'\\d+/\\d+/\\d+\\ \\d+\\:\\d+ \\-\\ (.*)\\:', text_line).group(1)
  except: 
    result = None    
  return result
  """




def line_reader(f):
  number_list = list(map(str, range(10)))

  result = {}
  for line in f:
    if line[0] in number_list: #if line begins with another kind of character, dont enter to this code 
      user = user_name_generator(line)
      if user is not None:
        if user in result:
          result[user] += 1
        else:
          result[user] = 1
  
  return result




def prepare_result(d):
  result = ''
  for x in d:
    result += x + ': ' + str(d.get(x)) + '\n'
    #result += '{:20} {:3.2f}\n'.format(x, d.get(x))
  return result

# '{:20} {:3.2f}'.format(nombre, mensajes)



def print_date():
  """makes the string with date, es = espanish"""
  date = dt.now()
  calend = calendar.Calendar(6) # 6 = Week starts on Sunday
  iter_month = calend.itermonthdays(date.year, date.month)
  days_es = ['Domingo', 'Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado']
  months_es = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 'Diciembre']

  week_ix = 0
  for day in iter_month:
    if day == date.day:
      break
    week_ix += 1
    if week_ix == 7:
      week_ix = 0

  return '{}:{} hs del {} {} de {} del {}.\n\n'.format(date.hour, date.minute, days_es[week_ix], date.day, months_es[date.month - 1], date.year)
 
