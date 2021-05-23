# Importamos todas las variables de la librería tkinter
from tkinter import *


# Creamos un "lienzo", es decir una raíz desde tkinter
root = Tk()
# Definimos título, ícono, tamaño, y si es redimensionable.
root.title("EALEA")
root.geometry("1080x720")
root.resizable(1,1)
root.iconbitmap("Cuone logo.ico")


# Creamos el título con sus diferentes propiedades.
title = Label(root, text="¡BIENVENID@!", font=("Gothic", 30), fg="#07031A")
title.place(x=400, y=10)


# Se crea el widget "YO", el  cual representa un menú desplegable con diferentes opciones para ingresar, todas ellas tienen que ver con el desarrollo personal del curso.
yo = Frame()
yo.pack(side="left", anchor="n", fill="y")
yo.config(bg="#07031A", width="100", height="100", bd=5)

# Empezamos a introducir dichas opciones por medio de "Labels", cuadros de texto, que insertamos en el widget "YO".
Label(yo, text="YO", font=("Gothic", 25), bg="#07031A", fg="white").place(x=25, y=25)
Label(yo, text="Progreso", font=("Sans seriff", 15), bg="#07031A", fg="white").place(x=0, y=125)
Label(yo, text="Cursos", font=("Sans seriff", 15), bg="#07031A", fg="white").place(x=0, y=175)
Label(yo, text="Mis Inst.", font=("Sans seriff", 15), bg="#07031A", fg="white").place(x=0, y=225)
Label(yo, text="Mi Perfil", font=("Sans seriff", 15), bg="#07031A", fg="white").place(x=0, y=275)
Label(yo, text="Mis Herr.", font=("Sans seriff", 16), bg="#07031A", fg="white").place(x=0, y=320)


# Creamos otro widget, en este caso será solo como subtítulo.
text_place = Frame(root)
text_place.config(bg="#07031A", width="350", height="100")
text_place.place(x=350, y=150)

# Estos son los dos subtítulos que habrá, expuestos como "Labels".
txt1 = Label(text_place, text="A la interfaz de aprendizaje", bg="#07031A", fg="white", font=("Sans seriff", 15))
txt1.place(x=50, y=10)

txt2 = Label(text_place, text="¡¡Donde aprenderás muchas cosas!!", bg="#07031A", fg="white", font=("Sans seriff", 15))
txt2.place(x=20, y=50)


# Se crea el último widget, a modo de menú de "extras", un menú también lateral, pero del lado derecho, en el cual, las opciones serán sobre información extra, lugares para que el usuario descubra. 
options_place = Frame(root)
options_place.config(bg="white", width="200", height="720", bd=3, relief="groove")
options_place.pack(side="right", fill="y")

# Se insertan las opciones extra anteriormente mencionados.
Label(options_place, text="         +          ", font=("Sans seriff", 25), bg="white", fg="#07031A", relief="groove").place(x=0, y=0)
Label(options_place, text="   más cursos    ", font=("Sans seriff", 20), bg="white", fg="#07031A", relief="groove").place(x=0, y=40)
Label(options_place, text="más instrumentos    ", font=("Sans seriff", 18), bg="white", fg="#07031A", relief="groove").place(x=0, y=83)
Label(options_place, text="         otros        ", font=("Sans seriff", 20), bg="white", fg="#07031A", relief="groove").place(x=0, y=120)
Label(options_place, text="    comunidad    ", font=("Sans seriff", 20), bg="white", fg="#07031A", relief="groove").place(x=0, y=160)
Label(options_place, text="   ¿preguntas?   ", font=("Sans seriff", 20), bg="white", fg="#07031A", relief="groove").place(x=0, y=200)
Label(options_place, text="        ayuda        ", font=("Sans seriff", 20), bg="white", fg="#07031A", relief="groove").place(x=0, y=240)
Label(options_place, text="      opciones      ", font=("Sans seriff", 20), bg="white", fg="#07031A", relief="groove").place(x=0, y=280)


# Se cierra la raíz.
root.mainloop()