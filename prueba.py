__author__ = 'nonamed'

#!/usr/bin/python
import MySQLdb
import csv
import datetime
import os.path

ruta_guardado = 'realizados/'

fecha = datetime.datetime.strftime(datetime.datetime.now(), '%Y_%m_%d_%H_%M_%S')

directorio = fecha

print fecha

db = MySQLdb.connect(host="localhost", # your host, usually localhost
                     user="root", # your username
                      passwd="evaperona", # your password
                      db="leads") # name of the data base

with open ("buscar.csv", "rw") as buscar_csvfile:
    args=[]
    for email in csv.reader(buscar_csvfile):
        args.append(email)

sql='SELECT id,email FROM leads WHERE email IN (%s)'
in_p=', '.join(map(lambda x: '%s', args))
sql = sql % in_p
cur = db.cursor()
cur.execute(sql, args)
resultado = cur.fetchall()

sql='SELECT id,email FROM leads WHERE email NOT IN (%s)'
in_p=', '.join(map(lambda x: '%s', args))
sql = sql % in_p
cur = db.cursor()
cur.execute(sql, args)
resultado_no_encontrados = cur.fetchall()

lista_no_encontrados = []

for id in resultado_no_encontrados:
    lista_no_encontrados.apperesultadond(id)

lista_resultado = []
for id in resultado:
    lista_resultado.append(id)

if not os.path.exists(os.path.join(ruta_guardado,directorio)):
    os.makedirs(os.path.join(ruta_guardado,directorio))
ruta_final = (os.path.join(ruta_guardado,directorio))
with open (os.path.join(ruta_final,'resultado_%s' % fecha),'wb') as fichero_salida:
    fichero_final = csv.writer(fichero_salida)
    for item in lista_resultado:
        fichero_final.writerow(item)

with open (os.path.join(ruta_final,'no_encontrados_%s' % fecha),'wb') as fichero_salida_no_encontrados:
    fichero_final = csv.writer(fichero_salida_no_encontrados)
    for item in lista_no_encontrados:
        fichero_final.writerow(item)


