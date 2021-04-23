# código para invocar la librería sqlite para python.
import sqlite3

# Se conecta la libería con el archivo específico ("usuarios" en este caso) y se define el cursor.
conn = sqlite3.connect('usuarios.db')
c = conn.cursor()


# Se crea una tabla nueva dentro del archivo "usuarios", con el nombre "primer" y se definen sus columnas: correo, instrumento, genero, edad.
def create_table():
   c.execute("CREATE TABLE IF NOT EXISTS primer(correo TEXT NOT NULL, instrumento TEXT NOT NULL, genero TEXT NOT NULL, edad INT)")

# Se presentan los input para que el usuario ingrese sus datos, que posteriormente se ingresarán a la base de datos.
mail = input("pon tu correo aquí: ")
instru = input("Aquí tu instrumento: ")
trato = input("aquí el trato que prefieres (femenino, masculino, neutro) ")
age = int(input("y tu edad, por favor: "))

# Datos de prueba
def data_entry():
   c.execute("INSERT INTO primer VALUES ('sacevedo058@gmail.com', 'guitarra', 'masculino', 19)")


# Se insertan los datos de los input a la base de datos.
data = "insert into primer(correo, instrumento, genero, edad) values('{}','{}','{}','{}');".format(mail, instru, trato, age)

# Se ejecuta el cursor y se muestran los usarios que hay.
c.execute(data)
print(c)
usuario = c.fetchall()
print(usuario)


# Se guardan los cambios y se cierra el sqlite3.
conn.commit()
c.close()
conn.close()

print("¡Listo! ¡has quedado registrado en la base de datos con éxito!")
