#Fifteen
from time import sleep
import random

K=20

def intro():
    """Titulo del juego"""
    print(f"< < < F  I  F  T  E  E  N > > >")

def reglas():
    """Muestra las reglas del juego"""
    print(f"\nReglas: ")
    sleep(0.75)
    print(f"Lograr ordenar los números generados de manera aleatoria en la menor cantidad de jugadas posibles.")
    sleep(0.75)
    print(f"El orden debe ser de menor a mayor, de izquierda a derecha y de arriba hacia abajo.")
    main()

def relleno():
    """"Agrega boludeces para que no sea tan monotono."""
    sleep(0.85)
    print("\nGenerando tablero . . .", end=" ")
    print("\n")
    sleep(2)

def grid_printer(grid, filas, columnas):
    """Muestra el tablero segun los parametros ingresados."""
    for i in range(int(filas)): 
        for j in range(int(columnas)):
            print(grid[i][j], end=" ")
        print(" ")

def move_up(grid, filas, columnas):
    """Mueve el cero hacia arriba"""
    zero_i=None #Inicializa una variable para la coordenada i
    zero_j=None #Inicializa una variable para la coordenada j
    for i in range(int(filas)): #Busca el cero y actualiza la i y la j
        for j in range(int(columnas)):
            if grid[i][j]==0:
                zero_i=i
                zero_j=j
            else:
                continue
    if (zero_i-1)>=0: #Mecanismo para evitar que el cero se salga del rango de la lista
        grid[zero_i][zero_j], grid[zero_i-1][zero_j]=grid[zero_i-1][zero_j], grid[zero_i][zero_j] #Intercambia las posiciones

def move_down(grid, filas, columnas):
    """Mueve el cero hacia abajo"""
    zero_i=None #Inicializa una variable para la coordenada i
    zero_j=None #Inicializa una variable para la coordenada j
    for i in range(int(filas)): #Busca el cero y actualiza la i y la j
        for j in range(int(columnas)):
            if grid[i][j]==0:
                zero_i=i
                zero_j=j
            else:
                continue
    if (zero_i+1)<int(filas): #Mecanismo para evitar que el cero se salga del rango de la lista
        grid[zero_i][zero_j], grid[zero_i+1][zero_j]=grid[zero_i+1][zero_j], grid[zero_i][zero_j] #Intercambia las posiciones

def move_left(grid, filas, columnas):
    """Mueve el cero hacia la izquierda"""
    zero_i=None #Inicializa una variable para la coordenada i
    zero_j=None #Inicializa una variable para la coordenada j
    for i in range(int(filas)): #Busca el cero y actualiza la i y la j
        for j in range(int(columnas)):
            if grid[i][j]==0:
                zero_i=i
                zero_j=j
            else:
                continue
    if (zero_j-1)>=0: #Mecanismo para evitar que el cero se salga del rango de la lista
        grid[zero_i][zero_j], grid[zero_i][zero_j-1]=grid[zero_i][zero_j-1], grid[zero_i][zero_j] #Intercambia las posiciones

def move_right(grid, filas, columnas):
    """Mueve el cero hacia la derecha"""
    zero_i=None #Inicializa una variable para la coordenada i
    zero_j=None #Inicializa una variable para la coordenada j
    for i in range(int(filas)): #Busca el cero y actualiza la i y la j
        for j in range(int(columnas)):
            if grid[i][j]==0:
                zero_i=i
                zero_j=j
            else:
                continue
    if (zero_j+1)<int(columnas): #Mecanismo para evitar que el cero se salga del rango de la lista
        grid[zero_i][zero_j], grid[zero_i][zero_j+1]=grid[zero_i][zero_j+1], grid[zero_i][zero_j] #Intercambia las posiciones

def win(moves_counter):
    print(f"Felicitaciones! Ganaste en un total de {moves_counter} movimientos!")
    sleep(1)
    print(f"Esta pantalla se cerrara automaticamente en 3 .")
    sleep(1)
    print(f"Esta pantalla se cerrara automaticamente en 2 . .")
    sleep(1)
    print(f"Esta pantalla se cerrara automaticamente en 1 . . .")
    sleep(1)
    exit()

def main():
        """Funcion principal con todas las funciones basicas y la estructura general del juego"""
        user_input=input("\nIniciar -> 1\nReglas -> 2\nSalir -> 3\n")
        if user_input=="1": #Primero inicializa todas las variables, listas, procesos internos, etc
            moves_counter=0 #Inicializa el contador de movimientos
            grid=[] #Inicializa un tablero vacio que se modificara a medida que se vayan realizando movimientos
            win_grid=[] #Inicializa un tablero donde guardara la lista en el orden correcto que se comparara con la la lista "grid" durante el transcurso del juego
            current_number=1 #Establece el numero inicial desde donde empieza a poner numeros en el tablero
            cant_filas=input("Con cuantas filas desea jugar?   ") #Pregunta cuantas filas quiere el usuario
            cant_columnas=input("Y con cuantas columnas?    ") #Pregunta cuantas columnas quiere el usuario
            if cant_filas=="1" or cant_columnas=="1": #Evita que el usuario ponga filas y/o columnas de valor 1
                print("\nEl número de filas o columnas ingresadas en inválido. Por favor ingrese un valor mayor a 1.")
                return main()
            relleno() #Flavor
            total_pieces=int(cant_filas)*int(cant_columnas) #El limite maximo de numeros que puede contener el tablero
            for rows in range(int(cant_filas)): #Crea el tablero
                rows=[]
                for columns in range(int(cant_columnas)):
                    if current_number<total_pieces:
                        rows.append(current_number)
                        current_number+=1
                    else:
                        rows.append(0) #Coloca un 0 al final si llego al limite maximo de fichas, en lugar del numero final
                grid.append(rows)
                win_grid.append(list(rows)) #Crea una nueva lista en win_grid
            for x in range(K): #Randomiza el tablero haciendo movimientos al azar K cantidad de veces. K es constante global
                random_factor=random.randint(1, K*10) #Randomiza un numero al azar que decide que movimiento se realizara. Multiplica por 10 la K para mas diversidad.
                if random_factor>=0 and random_factor<=50: #Para 0-50 mueve hacia arriba
                    move_up(grid, cant_filas, cant_columnas)
                elif random_factor>50 and random_factor<=100: #Para 51-100 mueve hacia abajo
                    move_down(grid, cant_filas, cant_columnas)
                elif random_factor>100 and random_factor<=150: #Para 101-150 mueve hacia la derecha
                    move_right(grid, cant_filas, cant_columnas)
                else:
                    move_left(grid, cant_filas, cant_columnas) #Para 151-200 mueve hacia la izquierda
            grid_printer(grid, cant_filas, cant_columnas) #Muestra el tablero
            while True: #Arranca el juego
                if grid==win_grid and moves_counter<=(K * 5): #Chequea si el tablero en curso es igual al tablero ganador y si se paso del limite de movimientos
                    win(moves_counter)
                elif moves_counter==(K*5):
                    print(f"Se ha excedido de la cantidad de movimientos permitidos para resolver el tablero.")
                    user_movement=input("\nJugar de nuevo -> 1\nSalir ->   2   ")
                    if user_movement=="1":
                        main()
                    elif user_movement=="2":
                        exit()
                elif grid!=win_grid and moves_counter<(K*5):
                    print(f"\nControles: w, a, s, d")
                    print(f"Movimientos realizados: {moves_counter}")
                    print(f"Movimientos máximos: {K*5}")
                    print(f"Salir: 2")
                    user_movement=input("\nIngrese un movimiento:   ") #Pide un movimiento
                    moves=list(user_movement) #Convierte los inputs en una lista
                    for move in moves: #Itera la lista y acciona segun los inputs ingresados
                        if move=="W" or move=="w":
                            move_up(grid, cant_filas, cant_columnas)
                            moves_counter+=1 
                        elif move=="S" or move=="s":
                            move_down(grid, cant_filas, cant_columnas)
                            moves_counter+=1
                        elif move=="D" or move=="d":
                            move_right(grid, cant_filas, cant_columnas)
                            moves_counter+=1
                        elif move=="A" or move=="a":
                            move_left(grid, cant_filas, cant_columnas)
                            moves_counter+=1
                        elif move=="2":
                            exit()
                        else: #Se ataja por si el usuario ingresa un movimiento no valido
                            sleep(0.5)
                            print("\nIntroduzca un movimiento válido.\n")
                            sleep(0.5)
                    grid_printer(grid, cant_filas, cant_columnas)
        elif user_input=="2": #Muestra las reglas
            reglas()
        elif user_input=="3": #Termina el script
            exit()
intro()
main()