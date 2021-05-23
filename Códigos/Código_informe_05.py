# Importar las librerías necesarias (en este caso tkinter y time)
import tkinter
# En el caso de tkinter, se importarán todas sus variables
from tkinter import *
import time
# Empezamos creando una interfaz raíz (root)
root = tkinter.Tk()
# Definimos las propiedades de la misma interfaz raíz
root.title("metrónomo")
root.geometry("750x500")
root.configure(bg="#ececec")

# Empezamos definiendo el comportamiento del metrónomo, la ecuación que usará para transformar el valor que se le dará al tiempo necesario, además de definir que el valor que obtendrá, lo obtendrá de el usuario que lo escribirá.
def play_metrónomo():
    seconds_per_metronome = 60 / int(metronome_speed.get())
    i = 0
    while True:
      # Defnimos el contador que mostrará la velocidad en forma de cuenta.
        print(i)
        i = i+1
        time.sleep(seconds_per_metronome)

# Creamos el botón "Start", el cual tiene el comando de ejecutar el metrónomo con el dato que el usuario brindó.
button = Button(root, text="Start", width=16, command=play_metrónomo)
button.place(x=325, y=100)

# Aquí creamos la casilla en la que se pondrá el tempo que el usuario desee.
metronome_speed = Entry(root, width=10)
metronome_speed.place(x=320, y=250)

# Escribimos los diferentes textos, como lo son el título, las especificaciones, entre otros.
Label(root, text="tempo:", font=("Sans sheriff", 15)).place(x=320, y=200)

title = Label(root, text="Metrónomo visual", font=("Sans seriff", 24))
title.place(x=250, y=15)

text_1 = Label(root, text="Para empezar el metrónomo, pon el tempo y da click en Start", font=("Sans seriff", 15))
text_1.place(x=50, y=350)

text_2 = Label(root, text="para finalizarlo, detén el programa", font=("Sans seriff", 15))
text_2.place(x=50, y=400)

# hacemos que la raíz esté en actualización constante para que se pueda mostrar una interfaz, y en la misma se pueda escribir diferentes parámetros e interactuar con los diferentes componentes.
root.mainloop()