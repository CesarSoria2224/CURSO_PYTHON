playlis = {} # diccionario vacio
playlis['campo de caciones'] = [] # lista de canciones vacias
def app():

    agregar_playlist = True
    while agregar_playlist:
        nombre_playlist = input('escribe el nombre de la playlist \n')

        if nombre_playlist:
            playlis['nombre'] = nombre_playlist

            agregar_playlist = False
            print(playlis)
            agregar_cancio()


def agregar_cancio():
    agregar_cancion = True
    while agregar_cancion:

        nombre_playlist = playlis['nombre']
        pregunta = f"agrega canciones a la playlist \n"
        pregunta += 'escribe "X" para de agregar canciones \n'

        cancion = input(pregunta)
app()