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



# def buscar_datos(*args, **kwargs):
#     for key, value in kwargs.items():
#         # Verificar si los nombres y apellidos coinciden exactamente
#         if all(value.get(k) == v for k, v in zip(["primer_nombre", "segundo_nombre", "primer_apellido", "segundo_apellido"], args)):
#             return key  # Devolver la clave si hay una coincidencia exacta
#     return None  # Devolver None si no se encuentra ninguna coincidencia

# database = {
#     "persona1": {
#         "primer_nombre": "Pablo",
#         "segundo_nombre": "Diego",
#         "primer_apellido": "Ruiz",
#         "segundo_apellido": "Picasso"
#     },

#     "persona2": {
#         "primer_nombre": "Antonella",
#         "segundo_nombre": "Natalia",
#         "primer_apellido": "Manatrizio",
#         "segundo_apellido": "Caraganopulos"
#     }

# }

# resultado = buscar_datos("Pablo", "Diego", "Ruiz", "Picasso", **database)
# print(resultado)  # Debería imprimir "persona1" porque coincide con los nombres y apellidos proporcionados

# resultado = buscar_datos("Manatrizio", "Antonella", **database)
# print(resultado) 



def buscar_datos(*args, **kwargs):
    for key, value in kwargs.items():
        # Verificar si los nombres y apellidos coinciden independientemente del orden
        if all(arg in value.values() for arg in args):
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
        "primer_nombre": "Elio",
        "primer_apellido": "Anci"
    },
    "persona3": {
        "nombre1": "Elias",
        "nombre2": "Marcos",
        "nombre3": "Luciano",
        "apellido1": "Marcelo",
        "apellido2": "Gonzalez"
    },
    "persona4": {
        "primer_nombre": "Juan",
        "primer_apellido": "Pérez"
    }
}

# Buscar una persona con un nombre y un apellido, sin importar el orden
resultado = buscar_datos("Pérez", "Juan", **database)
print(resultado)  # Debería imprimir "persona4" porque coincide con el nombre y apellido proporcionados, independientemente del orden
