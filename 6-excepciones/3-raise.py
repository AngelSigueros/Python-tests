
# raise sirve para lanzar una excepción, esto permite centralizar la gestión de excepciones en un mismo punto
# de un programa, haciendo que las funciones que se invocan desde ese punto lancen excepciones en vez de gestionarlas

emails = ["dani@example.com", "alan@example.com", "aroa@example.com"]


def validate_email(email):
    if email in emails:
        raise Exception("Email ya registrado")
    else:
        print("Email válido")


try:
    validate_email("alan@example.com")
except Exception as e:
    print("Error capturado", e)

print("fin")
