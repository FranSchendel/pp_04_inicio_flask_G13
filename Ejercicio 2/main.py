from flask import Flask, render_template
import sqlite3
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/listado')
def listado():
  db = sqlite3.connect('co_emissions.db')
  a = db.execute("""SELECT Country, Value, Year
  FROM emissions
  WHERE Series = "pcap"
  ORDER BY Value DESC
  """)
  i = 1
  top = []
  while i <= 10:
    top.append(a.__next__())
    i += 1
  return render_template('listado.html',
                        listado = top)

@app.route('/listado/top')
def listado_top():
  db = sqlite3.connect('co_emissions.db')
  a = db.execute("""SELECT Country, Value, Year
  FROM emissions
  WHERE Series = "total"
  ORDER BY Value DESC
  """)
  i = 1
  top = []
  while i <= 10:
    top.append(a.__next__())
    i += 1
  return render_template('listado_top.html',
                        listado = top)

@app.route('/listado/top/<pais>')
def listado_pais(pais):
  db = sqlite3.connect('co_emissions.db')
  c = db.execute("""SELECT Country
  FROM emissions     
  """)
  paises = []
  for fila in c:
    paises.append(fila)
  for l in range(len(paises)):
    if pais not in paises[l][0]:
      error = True
    else:
      error = False
      break
  if error:
    return render_template("error.html")
    
  a = db.execute(f"""SELECT Country, Value, Year
  FROM emissions
  WHERE Country = '{pais}'
  ORDER BY Value DESC
  """)
  i = 1
  top = []
  while i <= 10:
    top.append(a.__next__())
    i += 1
  return render_template('listado_pais.html',
                        listado = top)
@app.route('/ayuda')
def ayuda():
  return render_template('ayuda.html')

app.run(host='0.0.0.0', port=81)