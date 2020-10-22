import os
import codecs
import turtle
import str_helpers
import percent_helpers
from tkinter import filedialog
from itertools import cycle
import time

 
path = os.path.dirname(os.path.abspath(__file__)) + '\\'


# Window Object
window = turtle.Screen()
window.title('WhatsApp sms counter')
window.bgcolor('#040604') # same that Logo's border
window.setup(width= 1.0, height= 1.0)
window.addshape(path + 'logo.gif')
window.addshape(path + 'percent.gif')
window.addshape(path + 'msgs.gif')
window.addshape(path + 'pencil.gif')

#Logo & group name Object
logo = turtle.Turtle()
logo.hideturtle()
logo.penup()
logo.color('#f0f0f0')
logo.shape(path + 'logo.gif')
logo.setx((window.window_width()//6) + 30)
logo.sety((window.window_height()//4) -30)
logo.speed(1)

#Percent image
perct = turtle.Turtle()
perct.hideturtle()
perct.penup()
perct.shape(path + 'percent.gif')
perct.speed(0)

#Msgs image
msgs = turtle.Turtle()
msgs.hideturtle()
msgs.penup()
msgs.shape(path + 'msgs.gif')
msgs.speed(0)


#Msg print Objetc
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.color('#f0f0f0')
pen.goto(0, (window.window_height()//4) * -1)
pen.speed(0)

#Pie graphic Object
cake = turtle.Turtle()
cake.hideturtle()
cake.shape(path + 'pencil.gif')
cake.pencolor('#b0b0b0')
cake.penup()
cake.pensize(2)


### Vars and Const ###

results_tuple = None#[('Pablito', 46.92), ('Ezequiel Romio', 15.51), ('Andy Sur', 15.11), ('Guido', 9.15), ('Gera', 4.17), ('Brenda Vazquez', 9.15)]
CAKE_COLORS = cycle(['#52B04D', '#D5552C', '#2CA1D5', '#904BE2', '#B7E85D', '#B81611', '#12C275', '#F03F9D', '#146286', '#838342', '#CAACF3'])
CAKE_RADIUS = 150
LABEL_RADIUS = CAKE_RADIUS * 1.40

############# Functions ##############
def save():
  """On key press s """
  to_save_file = filedialog.asksaveasfile() #Opens file explorer
  to_save_file.write('Grupo de whatsApp "{}"\n\nFecha del Registro:\n\n'.format(group_name)) 
  to_save_file.write(str_helpers.print_date())  
  for k in percent_results:
    to_save_file.write(str(k) + ' ' + str(percent_results[k]) + '%\n')


def shut_down():
  """On key press Esc"""
  window.bye()

def bake():
  """Makes de pie chart"""
  cake.showturtle()
  cake_x_pos = (window.window_width() // 4) *-1
  cake.goto(cake_x_pos, -CAKE_RADIUS)
  cake.pendown()
  results_tuple = d.items()
  total = sum(fraction for _, fraction in results_tuple) # Rounds percent to 100 exactly
  for _, fraction in results_tuple:
    cake.fillcolor(next(CAKE_COLORS))
    cake.begin_fill()
    cake.circle(CAKE_RADIUS, fraction * 360 / total)
    position = cake.position()
    cake.goto(cake_x_pos, 0)
    cake.end_fill()
    cake.setposition(position)
    
  cake.penup()
  cake.sety(-LABEL_RADIUS)
  cake.color('#f0f0f0')

  """Makes the names around the de pie"""
  for label, fraction in results_tuple:
      cake.circle(LABEL_RADIUS, fraction * 360 / total / 2)
      cake.write(label, align="center", font=('Calibri', 20, 'normal'))
      cake.circle(LABEL_RADIUS, fraction * 360 / total / 2)
  cake.hideturtle()


def invalid_chat(cause):
  """Send a message and shutdown"""
  logo.speed(0)
  logo.setx(0)
  logo.sety(0)
  logo.hideturtle()
  if cause == 'cancel':
    logo.write('Good Bye!', align='center', font=('Calibri', 48, 'bold'))
    time.sleep(2)
  elif cause == 'invalid_format':
    logo.write('Formato de Archivo o de texto inválido!\nLo sentimos...', align='center', font=('Calibri', 48, 'bold'))
    time.sleep(5)
  window.bye()

#############################################################



##### Choose file and group name windows ####
group_name = window.textinput('Bienvenide', 'Ingrese un nombre para el GRUPO\nY luego seleccione el archivo de texto con el chat de WhatsApp')
if group_name is None: #if user press cancel or Escape
  group_name = 'Grupo sin nombre'


chat_file = filedialog.askopenfilename()

if not chat_file: # If user press cancel or Escape
  invalid_chat('cancel')

with codecs.open(chat_file, 'r', encoding='utf-8', errors='ignore') as f:
  d = str_helpers.line_reader(f)
#d = sorted(d.items(), key = lambda x: x[1], reverse = True)
percent_results = percent_helpers.msg_percent(d)

if not percent_results: # if its a invalid format
  invalid_chat('invalid_format')


logo.write(' @' + group_name, align='center', font=('Calibri', 48, 'bold'))
# Logo Coord correction after print group´s name 
logo.showturtle()
logo.setx(0)  
logo.sety(logo.ycor() + 30)


# Pen makes msg result
pen.write(str_helpers.prepare_result(d), align='center', font=('Calibri', 18, 'italic'))
msgs.setx(pen.xcor() - 20)
msgs.sety(pen.ycor() + 250)
msgs.showturtle()


# pen makes percent result
pen.setx((pen.xcor() + window.window_width()// 5))
pen.write(str_helpers.prepare_result(percent_results), align='center', font=('Calibri', 18, 'italic'))
perct.setx(pen.xcor() - 60)
perct.sety(pen.ycor() + 250)
perct.showturtle()


window.listen()
window.onkeypress(save, 's')
window.onkeypress(shut_down, 'Escape')

window.update()
bake()
window.update()

window.mainloop()