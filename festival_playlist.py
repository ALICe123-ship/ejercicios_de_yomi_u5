nombres = []
artistas = []
duraciones = []
popularidades = []


def agregar_canciones():
    cantidad = int(input("\n¿Cuántas canciones deseas agregar?: "))

    for i in range(cantidad):
        print(f"\nCanción {i + 1}")

        nombre = input("Nombre de la canción: ")
        artista = input("Artista: ")
        duracion = float(input("Duración (minutos): "))
        popularidad = int(input("Popularidad (1-100): "))

        nombres.append(nombre)
        artistas.append(artista)
        duraciones.append(duracion)
        popularidades.append(popularidad)

    print("\nCanciones agregadas correctamente.")


def ver_reportes():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    total_canciones = len(nombres)
    duracion_total = sum(duraciones)

    indice_mayor = popularidades.index(max(popularidades))
    indice_menor = popularidades.index(min(popularidades))

    promedio = sum(popularidades) / len(popularidades)

    print("\n========== REPORTES ==========")
    print("Total de canciones:", total_canciones)
    print("Duración total:", round(duracion_total, 2), "minutos")

    print("\nCanción más popular:")
    print(nombres[indice_mayor], "-", artistas[indice_mayor], "- Popularidad:", popularidades[indice_mayor])

    print("\nCanción menos popular:")
    print(nombres[indice_menor], "-", artistas[indice_menor], "- Popularidad:", popularidades[indice_menor])

    print("\nPromedio de popularidad:", round(promedio, 2))


def buscar_canciones():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    print("\n1. Buscar por artista")
    print("2. Buscar por rango de popularidad")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        artista_buscado = input("Ingrese el nombre del artista: ")

        encontrado = False

        print("\nResultados:")

        for i in range(len(artistas)):
            if artistas[i].lower() == artista_buscado.lower():
                print(f"{nombres[i]} | {artistas[i]} | {duraciones[i]} min | Popularidad: {popularidades[i]}")
                encontrado = True

        if not encontrado:
            print("No se encontraron canciones.")

    elif opcion == "2":
        minimo = int(input("Popularidad mínima: "))
        maximo = int(input("Popularidad máxima: "))

        encontrado = False

        print("\nResultados:")

        for i in range(len(popularidades)):
            if minimo <= popularidades[i] <= maximo:
                print(f"{nombres[i]} | {artistas[i]} | {duraciones[i]} min | Popularidad: {popularidades[i]}")
                encontrado = True

        if not encontrado:
            print("No se encontraron canciones.")

    else:
        print("Opción no válida.")


def playlist_recomendada():
    if len(nombres) == 0:
        print("\nNo hay canciones registradas.")
        return

    promedio = sum(popularidades) / len(popularidades)

    print("\n===== PLAYLIST RECOMENDADA =====")
    print("Canciones con popularidad superior al promedio.\n")

    encontrada = False

    for i in range(len(popularidades)):
        if popularidades[i] > promedio:
            print(f"{nombres[i]} | {artistas[i]} | {duraciones[i]} min | Popularidad: {popularidades[i]}")
            encontrada = True

    if not encontrada:
        print("No hay canciones que superen el promedio.")


while True:
    print("\n========== FESTIVAL PLAYLIST ==========")
    print("1. Agregar canciones")
    print("2. Ver reportes")
    print("3. Buscar canciones")
    print("4. Playlist recomendada")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_canciones()

    elif opcion == "2":
        ver_reportes()

    elif opcion == "3":
        buscar_canciones()

    elif opcion == "4":
        playlist_recomendada()

    elif opcion == "5":
        print("\nGracias por utilizar Festival Playlist.")
        break

    else:
        print("\nOpción no válida.")