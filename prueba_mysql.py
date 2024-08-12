import mysql.connector

mibd = mysql.connector.connect(
    host = 'localhost',
    user = 'root'
)

# Se crea una instancia de la clase 'cursor' el cual se usa para ejecutar comandos SQL.
cursor = mibd.cursor()

# Se ejecuta un comando SQL.
cursor.execute("SHOW DATABASES")
 
for x in cursor:
  print(x)