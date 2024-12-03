import random
import os

NUMERO_PARTICIPANTES = 5
matriz_inicial = [
    [1,0,0,0,0],
    [2,0,0,0,0],
    [3,0,0,0,0],
    [4,0,0,0,0],
    [5,0,0,0,0]
]

def limpiar_consola():
    input("presione cualquier tecla para continuar......")
    os.system('cls')


def generar_numero_random(minimo:int,maximo:int)->int:
    respuesta = random.randint(minimo,maximo)
    return respuesta


def menu()->int:
    respuesta = int(input("\tMi Menu\n1. Cargar Notas\n2. Mostrar Votos\n3. Ordenar votos por nota promedio\n4. Peores 3\n5. Mayores promedio\n6. Jurado malo\n7. Sumatoria\n8. Definir ganador\n9. Salir-->: "))
    return respuesta
              

def generar_matriz():
    matriz = [
    [1,7,7,7,140.8],
    [2,5,4,4,16.2],
    [3,8,9,3,40.12],
    [4,10,10,1,120.2],
    [5,1,9,10,78.15]
] 

    return matriz


def contar_votos_totales(matriz):
  """
  Contabiliza el total de votos en una matriz.

  Parametros:
    matriz: Una matriz donde cada fila representa un candidato y cada columna
            (excepto la primera) representa los votos de un jurado. La primera
            columna contiene el numero de participante y la ultima el promedio.

  Retorna:
    El número total de votos contabilizados.
  """

  # Número de jurados (columnas sin contar el nro de participante ni el promedio)
  numero_jurados = len(matriz[0]) - 2  # todas las filas tienen la misma longitud

  # Inicializar el contador de votos totales
  votos_totales = 0

  # Iterar sobre cada candidato (cada fila de la matriz)
  for i in range(len(matriz)):
    # Inicializar el contador de votos para el candidato actual
    suma_votos = 0

    # Iterar sobre cada jurado (cada columna, excepto la primera y la ulitma)
    for j in range(1, numero_jurados + 1):
      # Sumar los votos del jurado actual al total del candidato
      suma_votos += matriz[i][j]

    # Sumar los votos del candidato actual al total general
    votos_totales += suma_votos

  # Retornar el total de votos contabilizados
  return votos_totales


def generar_promedio(matriz):
  """
  Calcula el promedio de votos por candidato y lo agrega como última columna en la matriz.

  Parametros:
    matriz: Una matriz donde cada fila representa un candidato. Las columnas (excepto la primera)
            contienen los votos de cada juez. La última columna se utilizará para almacenar el promedio.

  Retorno:
    La matriz modificada con los promedios calculados.
  """

  # Calcula el total de votos emitidos por todos los jueces
  total_votos = contar_votos_totales(matriz)

  # Obtiene el número de jueces (columnas sin contar la de nombres y promedios)
  numero_jueces = len(matriz[0]) - 2

  # Itera sobre cada candidato (cada fila de la matriz)
  for i in range(len(matriz)):
    # Inicializa la suma de votos para el candidato actual
    suma_votos = 0

    # Suma los votos de todos los jueces para el candidato actual
    for j in range(1, numero_jueces + 1):
      suma_votos += matriz[i][j]

    # Calcula el promedio de votos para el candidato actual en porcentaje
    promedio = (suma_votos * 100) / total_votos

    # Almacena el promedio calculado en la última columna de la fila del candidato
    matriz[i][-1] = promedio

  # Retorna la matriz modificada con los promedios
  return matriz


def cargar_votos(matriz):
  """
  Carga la matriz con votos aleatorios y calcula los promedios.

  Parametro:
    matriz: Una matriz vacía o pre-inicializada con el nro de candidatos en la primera columna.

  Retorna:
    La matriz completa con votos aleatorios y los promedios calculados para cada candidato.
  """

  # Obtiene el número de jurados (columnas sin contar la de nombres y promedios)
  numero_jurados = len(matriz) - 2

  # Itera sobre cada candidato (cada fila de la matriz)
  for i in range(len(matriz)):
    # Itera sobre cada jurado (cada columna, excepto la primera)
    for j in range(1, numero_jurados + 1):
      # Genera un número aleatorio entre 0 y 100 y lo asigna a la celda correspondiente
      matriz[i][j] = generar_numero_random(0, 100)

  # Calcula los promedios de votos para cada candidato y los agrega a la matriz
  matriz = generar_promedio(matriz)

  # Retorna la matriz completa con los votos y promedios
  return matriz


def pedir_numero(minimo, maximo):
  """
  Solicita al usuario un número entero dentro de un rango específico y lo valida.

  Parametros:
    minimo: El límite inferior del rango.
    maximo: El límite superior del rango.

  Retorno:
    El número entero ingresado por el usuario si es válido, de lo contrario, solicita nuevamente.
  """
  while True:
    # Solicita al usuario que ingrese un número
    numero_str = input(f"Ingrese un número entre {minimo} y {maximo}: ")

    # Inicializa una bandera para indicar si el número es válido
    es_valido = True

    # Itera sobre cada dígito del número ingresado
    for digito in numero_str:
      # Verifica si el dígito es un número del 0 al 9
      if not ('0' <= digito <= '9'):
        # Si encuentra un carácter que no sea un número, marca el número como inválido
        es_valido = False
        break  # Sale del bucle ya que no es necesario seguir verificando

    # Si el número es válido (solo contiene dígitos numéricos)
    if es_valido:
      # Convierte el número de cadena a entero
      numero = int(numero_str)

      # Verifica si el número está dentro del rango especificado
      if minimo <= numero <= maximo:
        # Si el número está dentro del rango, lo devuelve
        return numero
      else:
        # Si el número está fuera del rango, muestra un mensaje de error
        print("El número ingresado está fuera del rango.")
    else:
      # Si el número contiene caracteres no numéricos, muestra un mensaje de error
      print("Por favor, ingrese un número entero válido.")


def mostrar_voto(matriz):
    """
    Imprime los resultados de un participante de manera formateada.

    Parametro:
        matriz (list): Una lista de listas donde cada fila representa del participante y
                      las columnas contienen:
                      - Índice 0: Número de identificación.
                      - Índices 1 a 3: Votos de cada jurado.
                      - Último índice: Porcentaje total de votos.

    Retorna:
        None: La función imprime los resultados directamente.
    """

    # Calcula el número de jurados considerando que las dos últimas columnas
    # contienen información adicional (número de participante y porcentaje).
    numero_jurados = len(matriz) - 2

    # Imprime el número de participante
    print(f"Participante Nro {matriz[0]}:")

    # Itera sobre los votos de cada jurado
    for i in range(1, numero_jurados + 1):
        print(f"VOTO JURADO {i}: {matriz[i]}")

    # Imprime el porcentaje total de votos con dos decimales
    print(f"PORCENTAJE DE LOS VOTOS: {matriz[-1]:.2f}%")
    # Imprime una línea en blanco para separar los resultados de cada participante
    print()


def mostrar_votos(matriz: list) -> None:
    """
    Esta función se encarga de iterar sobre una matriz (lista de listas) y mostrar cada uno de los votos que contiene.

    Parametros:
        matriz: Una lista de listas, donde cada sublista representa un participante.

    Retorno:
        None: La función no devuelve ningún valor, solo imprime los votos por pantalla.
    """

    for i in range(len(matriz)):
        """
        En cada iteración, se llama a la función `mostrar_voto` para mostrar el voto actual.
        """
        mostrar_voto(matriz[i])


def ordenar_matriz_menor_a_mayor(matriz):
    """
    Esta función ordena una matriz de forma ascendente, comparando el último elemento de cada fila.

    Parametros:
        matriz: Una lista de listas que representa la matriz a ordenar.

    Returns:
        None: La función modifica la matriz original, por lo que no devuelve ningún valor.
    """

    numero_filas = len(matriz)  # Obtenemos el número de filas de la matriz

    # Bucle externo: Iteramos sobre cada fila, excepto la última (ya que se compara con la siguiente)
    for i in range(numero_filas):
        # Bucle interno: Comparamos elementos de la fila actual con los de las siguientes filas
        for j in range(0, numero_filas - i - 1):
            # Si el último elemento de la fila j es menor que el de la fila j+1, intercambiamos las filas
            if matriz[j][-1] < matriz[j+1][-1]:
                # Bucle para intercambiar los elementos de ambas filas
                for k in range(len(matriz[j])):
                    aux = matriz[j][k]
                    matriz[j][k] = matriz[j+1][k]
                    matriz[j+1][k] = aux


def ordenar_votos_por_orden(matriz, orden):
    """
    Esta función ordena una matriz de votos de forma ascendente o descendente, 
    comparando el último elemento de cada fila.

    Parametro:
        matriz: Una lista de listas que representa la matriz de votos a ordenar.
        orden: Una cadena que indica el orden de ordenamiento ('asc' para ascendente, 'desc' para descendente).

    Retorno:
        La matriz ordenada según el criterio especificado.
    """

    numero_filas = len(matriz)  # Obtenemos el número de filas de la matriz

    # Bucle externo: Iteramos sobre cada fila, excepto la última (ya que se compara con la siguiente)
    for i in range(numero_filas):
        # Bucle interno: Comparamos elementos de la fila actual con los de las siguientes filas
        for j in range(0, numero_filas - i - 1):
            # Condicional para ordenar de forma ascendente o descendente
            if (orden == 'asc' and matriz[j][-1] > matriz[j+1][-1]) or (orden == 'desc' and matriz[j][-1] < matriz[j+1][-1]):
                # Bucle para intercambiar los elementos de ambas filas
                for k in range(len(matriz[j])):
                    aux = matriz[j][k]
                    matriz[j][k] = matriz[j+1][k]
                    matriz[j+1][k] = aux

    return matriz  # Devolvemos la matriz ordenada


def encontrar_peores_3(matriz):
    """
    Esta función encuentra y devuelve las 3 filas con los valores más bajos en el último elemento.

    Parametro:
        matriz: Una lista de listas que representa la matriz a evaluar.

    Retorno:
        Una lista con las 3 primeras filas de la matriz ordenada, 
        correspondientes a las que tienen los valores más bajos en el último elemento.
    """

    numero_filas = len(matriz)  # Obtenemos el número de filas de la matriz

    # Ordenamos la matriz de menor a mayor según el último elemento de cada fila
    # Este bloque de código es el mismo que el algoritmo de burbujeo
    for i in range(numero_filas):
        for j in range(0, numero_filas - i - 1):
            if matriz[j][-1] > matriz[j+1][-1]:
                for k in range(len(matriz[j])):
                    aux = matriz[j][k]
                    matriz[j][k] = matriz[j+1][k]
                    matriz[j+1][k] = aux

    # Devolvemos las primeras 3 filas de la matriz ordenada (los 3 peores valores)
    return matriz[:3]


def calcular_promedio_total(matriz):
    """
    Calcula el promedio total de una matriz, ignorando la primera columna y ultima.

    Parametros:
        matriz: Una lista de listas que representa una matriz de participantes. 
                la primera columna contiene el nro de participante
                y no debe ser incluida en el cálculo del promedio.

    Retorna:
        El promedio total de todos los valores numéricos en la matriz, 
        excluyendo la primera columna.
    """

    filas = len(matriz)  # Obtener el número de filas de la matriz
    columnas = len(matriz[0]) - 2  # Obtener el número de columnas de los votos de los jueces (ignora la primera y la ultima columna)
    total_notas = 0  # Inicializar el acumulador para la suma de todas las notas

    # Iterar sobre cada fila y cada columna de datos (excluyendo la primera)
    for i in range(filas):
        for j in range(1, columnas + 1):
            total_notas += matriz[i][j]  # Sumar el valor actual a la suma total

    # Calcular el promedio dividiendo la suma total entre el número total de valores
    promedio = total_notas / (filas * columnas)
    return promedio


def calcular_un_promedio(matriz, fila):
    """
    Calcula el promedio de una fila específica en una matriz, ignorando la primera y ultima columna.

    Prametros:
        matriz: Una lista de listas que representa un participante. 
                la primera columna contiene el nro de participante 
                y no debe ser incluida en el cálculo del promedio.
        fila: El índice de la fila cuyo promedio se desea calcular.

    Retorna:
        El promedio de los valores en la fila especificada.
    """

    suma = 0  # Inicializamos la suma de las notas en 0
    num_notas = len(matriz[0]) - 2  # Obtenemos el número de jueces (columnas de datos) en cada fila

    # Iteramos sobre cada columna de datos (excluyendo la primera) de la fila especificada
    for i in range(1, num_notas + 1):
        suma += matriz[fila][i]  # Sumamos el valor de la celda a la suma total

    # Calculamos el promedio dividiendo la suma total entre el número de jueces
    promedio = suma / num_notas
    return promedio


def encontrar_arriba_del_promedio(matriz, promedio_total):
    """
    Encuentra y muestra los votos que superan el promedio total.

    Prametros:
        matriz: Una lista de listas que representa una matriz de participantes.
                la primera columna contiene el nro de participante 
        promedio_total: El promedio total de todos los votos.

    Retorna:
        True si se encontró al menos un voto por encima del promedio, False en caso contrario.
    """

    retorno = False  # Inicializamos una bandera para indicar si se encontró algún voto por encima del promedio

    # Iteramos sobre cada fila (cada voto) de la matriz
    for i in range(len(matriz)):
        # Comparamos el valor del voto actual (último elemento de la fila) con el promedio total
        if matriz[i][-1] > promedio_total:
            # Si el voto es mayor que el promedio, lo mostramos en pantalla
            mostrar_voto(matriz[i])
            # Cambiamos el valor de retorno a True para indicar que se encontró al menos un voto
            retorno = True

    return retorno


def encontrar_jurado_malo(matriz):
    """
    Esta función identifica al jurado con el promedio de notas más bajo.

    Prametros:
        matriz: Una matriz donde cada fila representa un participante y cada columna
                (excepto la primera) representa la nota otorgada por un jurado. 
                Hay 3 jurados y la primera columna contiene identificadores de los participantes.

    Retorna:
        None: La función imprime por pantalla el jurado con el promedio más bajo 
              y sus respectivos promedios.
    """

    numero_jurados = len(matriz[0]) - 2  # Calcula el número de jurados (columnas de notas)
    sum_votos_jurado_1 = 0  # Inicializa la suma de los votos del jurado 1
    sum_votos_jurado_2 = 0  # Inicializa la suma de los votos del jurado 2
    sum_votos_jurado_3 = 0  # Inicializa la suma de los votos del jurado 3

    # Itera sobre cada participante (fila) y suma los votos de cada jurado
    for i in range(len(matriz)):
        for j in range(1, numero_jurados + 1):
            if j == 1:
                sum_votos_jurado_1 += matriz[i][j]
            elif j == 2:
                sum_votos_jurado_2 += matriz[i][j]
            elif j == 3:
                sum_votos_jurado_3 += matriz[i][j]

    # Calcula los promedios de cada jurado
    promedio_jurado_1 = sum_votos_jurado_1 / NUMERO_PARTICIPANTES
    promedio_jurado_2 = sum_votos_jurado_2 / NUMERO_PARTICIPANTES
    promedio_jurado_3 = sum_votos_jurado_3 / NUMERO_PARTICIPANTES

    # Compara los promedios y muestra al jurado con el promedio más bajo
    if promedio_jurado_1 < promedio_jurado_2 and promedio_jurado_1 < promedio_jurado_3:
       print(f"el jurado nro 1 tiene el promedio de notas mas bajo: {promedio_jurado_1}%\n Jurado 2: {promedio_jurado_2}%\n Jurado 3: {promedio_jurado_3}%")
    elif promedio_jurado_2 < promedio_jurado_1 and promedio_jurado_2 < promedio_jurado_3:
       print(f"el jurado nro 2 tiene el promedio de notas mas bajo: {promedio_jurado_2}%\n Jurado 1: {promedio_jurado_1}%\n Jurado 3: {promedio_jurado_3}%")
    elif promedio_jurado_3 < promedio_jurado_1 and promedio_jurado_3 < promedio_jurado_2:
       print(f"el jurado nro 3 tiene el promedio de notas mas bajo: {promedio_jurado_3}%\n Jurado 1: {promedio_jurado_1}%\n Jurado 2: {promedio_jurado_2}%")
    

def contar_votos_participante(matriz):
    """
    Esta función calcula la suma total de votos para un participante.

     Prametros:
        matriz: Una lista que representa los votos de un participante. 
                el primer elemento de la lista es el nro de participante
                y los demás elementos son los votos de cada jurado.
                el ultimo elemento es el promedio.

    Retorna:
        La suma total de los votos del participante.
    """

    suma = 0  # Inicializamos un acumulador para sumar los votos
    numero_de_jurados = len(matriz) - 2  # Calculamos el número de jurados (ignorando el nro de participante y el promedio)

    # Iteramos sobre los votos de cada jurado 
    for i in range(1, numero_de_jurados + 1):
        suma += matriz[i]  # Sumamos el voto actual al total
    # Retornamos la suma total del participante
    return suma


def hacer_sumatoria(matriz, numero):
    """
    Esta función busca participantes en una matriz de votos que hayan obtenido 
    un número específico de votos.

    Parametro:
        matriz: Una matriz donde cada fila representa los votos de un participante.
        numero: El número de votos que se busca.

    Retorna:
        None: La función imprime los datos del participante si encuentra alguno
              que coincida con el número de votos especificado. Si ningún participante
              alcanza ese número, imprime un mensaje de error.
    """

    # Calculamos los votos totales para cada participante
    votos_participante_1 = contar_votos_participante(matriz[0])
    votos_participante_2 = contar_votos_participante(matriz[1])
    votos_participante_3 = contar_votos_participante(matriz[2])
    votos_participante_4 = contar_votos_participante(matriz[3])
    votos_participante_5 = contar_votos_participante(matriz[4])

    # Comparamos los votos totales de cada participante con el número buscado
    if votos_participante_1 == numero:
        mostrar_voto(matriz[0])
    if votos_participante_2 == numero:
        mostrar_voto(matriz[1])
    if votos_participante_3 == numero:
        mostrar_voto(matriz[2])
    if votos_participante_4 == numero:
        mostrar_voto(matriz[3])
    if votos_participante_5 == numero:
        mostrar_voto(matriz[4])
    # Si ningún participante alcanza el número de votos especificado, se imprime un error
    if votos_participante_1 != numero and votos_participante_2 != numero and votos_participante_3 != numero and votos_participante_4 != numero and votos_participante_5 != numero:
        print("error")
            

def definir_ganador(matriz):
    """
    Esta función identifica al ganador en una matriz de resultados.

    Parametros:
        matriz: Una matriz donde cada fila representa un participante y la última
                columna contiene el promedio.

    Retorna:
        Una lista que representa al ganador.

    Descripción:
    La función ordena la matriz de forma descendente según la puntuación en la última columna.
    El primer elemento de la matriz ordenada (índice 0) será el ganador.

    Pasos:
    1. Se obtiene el número de filas de la matriz (número de participantes).
    2. Se realiza un algoritmo de ordenamiento por burbujeo para ordenar las filas de la matriz
       de forma descendente según la puntuación.
    3. El primer elemento de la matriz ordenada se asigna a la variable `ganador` y se devuelve.
    """

    numero_filas = len(matriz)  # Obtener el número de participantes

    # Ordenar la matriz por puntuación de forma descendente (burbujeo)
    for i in range(numero_filas):
        for j in range(0, numero_filas - i - 1):
            if matriz[j][-1] < matriz[j+1][-1]:  # Si el siguiente elemento tiene mayor puntuación
                # Intercambiar las filas completas
                for k in range(len(matriz[j])):
                    aux = matriz[j][k]
                    matriz[j][k] = matriz[j+1][k]
                    matriz[j+1][k] = aux

    # El primer elemento de la matriz ordenada es el ganador
    ganador = matriz[0]

    return ganador



def ejecutar_menu():
    matriz = generar_matriz()
    while True:
        respuesta = menu()

        if respuesta == 1:
            matriz = cargar_votos(matriz)
            print("\n\tLOS VOTOS FUERON EMITIDOS\n")
            mostrar_votos(matriz)


        elif respuesta == 2:
            print("\tVOTOS DE LOS JURADOS\n")
            mostrar_votos(matriz)


        elif respuesta == 3:
            orden = "desc"
            ordenar_votos_por_orden(matriz,orden)
            if orden == "desc":
                print("\n\tORDEN DESCENDIENTE")
                mostrar_votos(matriz)
            elif orden == "asc":
                print("\n\tORDEN ACENDIENTE")
                mostrar_votos(matriz)


        elif respuesta == 4:
            matriz_peroes_3 = encontrar_peores_3(matriz)
            print("\tPEORES 3 CONCURSANTES\n")
            mostrar_votos(matriz_peroes_3)


        elif respuesta == 5:
            promedio_total = calcular_promedio_total(matriz)
            print(f"\n\tpromedio total: {promedio_total}%")
            retorno = encontrar_arriba_del_promedio(matriz, promedio_total)
            if retorno == False:
                print("\nno se encontraron participantes que superen el promedio total")


        elif respuesta == 6:
            encontrar_jurado_malo(matriz)


        elif respuesta == 7:
            numero = pedir_numero(3,300)
            print(numero)
            print(f"\n\tLos participantes que que coiciden con {numero} son:\n")
            hacer_sumatoria(matriz,numero)


        elif respuesta == 8:
            ganador = definir_ganador(matriz)
            print("\tEl participante ganador es: ")
            mostrar_voto(ganador)


        elif respuesta == 9:
            print("saliendo...")
            break
        limpiar_consola()



