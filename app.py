from decimal import Decimal, getcontext
getcontext().prec = 50

def calcular_interacciones_y_suma(interacciones, cantidad_inicial):
    """Calcula las interacciones y la suma total."""
    valores = []  
    suma_total = 0 
    for i in range(1, interacciones + 1):
        valores.append(cantidad_inicial)
        suma_total += cantidad_inicial
        print(f"{i} {cantidad_inicial:.10f}")
        cantidad_inicial *= 2 
    print(f"Suma total: {suma_total:.10f}")

def calcular_distribucion(cantidad_total, interacciones):
    """Distribuye la cantidad total entre interacciones."""
    valores = []  
    cantidad_restante = Decimal(cantidad_total)
    for i in range(interacciones, 0, -1):
        valor = cantidad_restante / 2 
        valores.insert(0, valor)  
        cantidad_restante -= valor
    for i, valor in enumerate(valores, start=1):
        print(f"{i} {valor:.10f}")
    suma_verificada = sum(valores)
    print(f"Suma verificada: {suma_verificada:.10f}")


def calcular_max_interacciones():
    """Calcula automáticamente el máximo número de interacciones posibles y muestra la tabla."""
    fondos_disponibles = Decimal(input("Introduce los fondos disponibles: "))
    multiplicador = Decimal(input("Introduce el multiplicador: "))
    probabilidad_perder = Decimal(input("Introduce la probabilidad de perder (por ejemplo, 0.56): "))

    limite_probabilidad_input = input("Introduce el límite de probabilidad (por ejemplo, 0.00001100): ")
    limite_probabilidad = Decimal(limite_probabilidad_input) if limite_probabilidad_input else Decimal("0.00001100")
    print(f"Límite de probabilidad utilizado: {limite_probabilidad}")

    interacciones = 0
    probabilidad_total = Decimal(1)
    apuesta_actual = limite_probabilidad

    print(f"{'I Interacción':<15}{'AA Apuesta':<15}{'PT Probabilidad acumulada':<25}{'FT Fondos restantes':<20}")
    print("-" * 80)

    while fondos_disponibles >= apuesta_actual and fondos_disponibles>0:
        interacciones += 1
        print(f"I{interacciones:<14}|AA{apuesta_actual:.10f}|PT{probabilidad_total:.10f}|FD{fondos_disponibles:.10f}")
        fondos_disponibles -= apuesta_actual
        apuesta_actual *= multiplicador
        probabilidad_total *= probabilidad_perder

        if apuesta_actual > fondos_disponibles:
            apuesta_actual = fondos_disponibles

    print("-" * 80)
    print(f"El número máximo de interacciones posibles es: {interacciones}")
    print(f"La probabilidad acumulada después de estas interacciones es: {probabilidad_total:.10f}")
    print(f"Fondos restantes: {fondos_disponibles:.10f}")
    
def victorias_totales():
    try:
        victorias = int(input("Introduce las victorias: "))
        derrotas = int(input("Introduce las derrotas: "))

        if victorias == 0:
            print("No puedes tener 0 victorias. Intenta nuevamente.")
            return

        total_lanzamientos = victorias + derrotas
        lanzamientos_por_victoria = total_lanzamientos / victorias

        print(f"En promedio, ganas cada {lanzamientos_por_victoria:.2f} lanzamientos.")
    except ValueError:
        print("Por favor, introduce valores numéricos válidos.")



def menu():
    """Menú principal para seleccionar funciones."""
    while True:
        print("\n--- MENÚ ---")
        print("1. Calcular interacciones y suma")
        print("2. Calcular distribución de la cantidad total")
        print("3. Calcular el número máximo de interacciones posibles")
        print("4. Calcular victorias")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                interacciones = int(input("Introduce el número de interacciones: "))
                cantidad_inicial = float(input("Introduce la cantidad inicial: "))
                calcular_interacciones_y_suma(interacciones, cantidad_inicial)
            elif opcion == 2:
                cantidad_total = Decimal(input("Introduce la cantidad total: "))
                interacciones = int(input("Introduce el número de interacciones: "))
                calcular_distribucion(cantidad_total, interacciones)
            elif opcion == 3:
                calcular_max_interacciones()
            elif opcion == 4:
                victorias_totales()
            elif opcion == 5:
                print("¡Hasta luego!")
                break
            else:
                print("Opción no válida. Por favor, intente nuevamente.")
        except ValueError:
            print("Entrada no válida. Por favor, introduzca un número válido.")
menu()
