from flask import Flask, render_template
from datetime import date, timedelta
import random

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')
  
  
@app.route('/dado')
def dado():
  num = random.randint(1, 6)
  return render_template('dado.html',
                        num_dado = num)
  
@app.route('/dado/<n>')
def random_num(n):
  n = int(n)
  numeros = ""
  if n<=0 or n>10:
      return render_template('error.html')
  else:
      for i in range(n):
          ran = str(random.randint(1 ,6))
          if i < n-1:
              numeros += ran + ", "
          elif i == n-1:
              numeros += ran
  return render_template('random.html',
                        nums = numeros)

@app.route('/fecha')
def fecha():
  inicio = date(1970, 1, 1)
  final = date(2100, 12, 31)
  random_date = inicio + timedelta(seconds= int((final - 
  inicio).total_seconds() * random.random()))
  return render_template('fecha.html',
                        fecha = random_date)

@app.route('/fecha/<y>')
def fecha_año(y):
  y = int(y)
  if y < 1 or y > 9999:
    return render_template('error_fecha.html')
  fecha_año = date(y, 1, 1)
  return render_template('fecha_año.html',
                        fecha = fecha_año)

@app.route('/fecha/<y>/<x>')
def fecha_año_mes(y, x):
  y = int(y)
  x = int(x)
  if y < 1 or y > 9999 or x < 1 or x > 12:
    return render_template('error_fecha.html')
  fecha_año_mes = date(y, x, 1)
  return render_template('fecha_año_mes.html',
                        fecha = fecha_año_mes)
    
@app.route('/color')
def color():
  r = str(random.randint(0,255))
  g = random.randint(0,255)
  b = random.randint(0,255)
  color_random = f"rgb({r}, {g}, {b})"
  return render_template('color.html',
                        color=color_random)
app.run(host='0.0.0.0', port=81)