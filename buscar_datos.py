#consigna
# Construir una funcion que permita recibir los nombres y apellidos de una persona, para verificar si se encuentra en la base de datos. La
# función debería retornar el "id" o la key del diccionario que contiene a una persona con todos los nombres y apellidos pasados como
# parametros a la funcion buscar_datos()
# Ejemplo:
# Si busco una persona cuyo nombre sea "Pablo Diego Ruiz Picasso", entonces, la llamada a la función será:
# buscar_datos("Pablo", "Diego","Ruiz","Picasso", **database)
# Donde cada uno de los primeros argumetos serán los nombres y apellidos (no necesariamente ordenados) y el último parametro, indicado con
# asteriscos, sería la base de datos.
# En base a esta llamada a la función, se debería retornar el valor de la key del diccionario que contiene los valores "Pablo, Diego, Ruiz,
# Picasso"
# buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database) -> 1
# Donde 1 es la key que identifica al diccionario correspondiente que contiene todos esos valores (ni mas ni menos)

# diccionario de palabras clave python
# *args: Significa "todos los argumentos posicionales". 
# Cuando pones un asterisco delante de args, estás diciendo que la función puede recibir
# cualquier cantidad de argumentos, y esos argumentos se guardarán en una tupla llamada args.
# Por ejemplo, si llamas a la función con funcion(1, 2, 3), args será igual a (1, 2, 3).
# **kwargs: Significa "todos los argumentos de palabra clave". Cuando pones dos asteriscos delante
# de kwargs, estás diciendo que la función puede recibir cualquier cantidad de argumentos de palabra
# clave, y esos argumentos se guardarán en un diccionario llamado kwargs. Por ejemplo, si llamas a la
# función con funcion(a=1, b=2, c=3), kwargs será igual a {"a": 1, "b": 2, "c": 3}.
# Entonces, *args maneja argumentos posicionales y **kwargs maneja argumentos de palabra clave.
# Estas son formas convenientes de manejar una variedad de argumentos en una función, lo que hace 
# que la función sea más flexible y pueda aceptar diferentes tipos de datos sin tener que especificarlos
# todos de antemano.


def buscar_datos(*args, **kwargs):
    # Convertir todos los argumentos a minúsculas
    args_lower = [arg.lower() if arg is not None else None for arg in args]
    for key, value in kwargs.items():
        # Convertir todos los valores del diccionario a minúsculas
        value_lower = {k: v.lower() if v is not None else None for k, v in value.items()}
        # Verificar si los nombres y apellidos coinciden independientemente del orden
        if all(arg in value_lower.values() for arg in args_lower):
            return key  # Devolver la clave si hay una coincidencia exacta
    return None  # Devolver None si no se encuentra ninguna coincidencia



database = {
    "persona1": {
        "primer_nombre": "Pablo",
        "segundo_nombre": "Diego",
        "primer_apellido": "Ruiz",
        "segundo_apellido": "Picasso"
    },
    "persona2": {
        "primer_nombre": "Maria",
        "primer_apellido": "Ruiz"
    },
    "persona3": {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Mendez",
        "apellido2": "Gonzalez"
    },
    "persona4": {
        "primer_nombre": "Juan",
        "primer_apellido": "Pérez"
    },

    "persona5": {
    "primer_nombre": "Antonella",
    "segundo_nombre": "Natalia",
    "primer_apellido": "Manatrizio",
    "segundo_apellido": "Caraganopulos"
    }
}

# Buscar una persona con un nombre y un apellido, sin importar el orden
resultado = buscar_datos("Pérez", "Juan", **database)
print(resultado)  # Imprime "persona4" porque coincide con el nombre y apellido proporcionados, independientemente del orden

# Probando solo con un nombre
resultado = buscar_datos("Elias", **database)
print(resultado)

#Probando con minusculas
resultado = buscar_datos("elias", **database)
print(resultado)

#Probando con mayusculas
resultado = buscar_datos("CARAGANOPULOS", **database)
print(resultado)