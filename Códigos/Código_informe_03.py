normales = ["alrendonc@unal.edu.co", "gawad@unal.edu.co", "lgilr@unal.edu.co"]
premium = ["alejorendoncardona@gmail.com", "sacevedo@gmail.com", "lauragilrzlds@gmail.com"]
usuario = input("Pon aquí tu correo electrónico, por favor... ")
instrumento = input("Dinos... ¿qué instrumento tocas? (Pon solo 1, por favor) ")

genero = input("¿Cómo te gustaría que te llamemos? (masculino, feminino, neutro)")


if usuario in normales:
  if genero == "masculino":
    print("¡Bienvenido! estás en el plan normal, ¡aquí podrás encontrar el mini-curso que llevas en progreso y otros cursos que te podrían interesar!, basados en que tocas", instrumento)
  elif genero == "femenino":
    print("¡Bienvenida! estás en el plan normal, ¡aquí podrás encontrar el mini-curso que llevas en progreso y otros cursos que te podrían interesar!, basados en que tocas", instrumento)
  elif genero == "neutro":
    print("¡Bienvenid@! estás en el plan normal, ¡aquí podrás encontrar el mini-curso que llevas en progreso y otros cursos que te podrían interesar!, basados en que tocas", instrumento)

elif usuario in premium:
  print("¡Hola de nuevo! eres premium, ¡te estabamos esperando para seguir con el curso!, o bien, para presentarte otras posibilidades que tienes para estudiar, basados en que tocas", instrumento)
else:
  print("Lo sentimos, pero no te encontramos en nuestro repertorio, ¿te gustaría registrarte? ")
