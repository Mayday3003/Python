"""
═══════════════════════════════════════════════════════════════════════════════
                    RETOS DE ALGORITMOS GREEDY
═══════════════════════════════════════════════════════════════════════════════

Resuelve cada reto usando una estrategia Greedy.
Para cada uno:
1. Identifica cuál es la "mejor decisión local"
2. Implementa el algoritmo
3. Analiza la complejidad
4. Determina si Greedy da la solución óptima

═══════════════════════════════════════════════════════════════════════════════
                              ENUNCIADOS
═══════════════════════════════════════════════════════════════════════════════
"""


# RETO 1: Máximo número de reuniones
# ─────────────────────────────────────────────────────────────────────────────
# Eres un gerente y tienes varias reuniones propuestas para hoy.
# Cada reunión tiene una hora de inicio y fin.
# Quieres asistir al MÁXIMO número de reuniones posible.
#
# Ejemplo:
#   reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]
#   Respuesta: 3 reuniones → [(9, 10), (10, 11), (12, 14)]
#
def max_reuniones(reuniones):
    """
    Args:
        reuniones: Lista de tuplas (hora_inicio, hora_fin)
    Returns:
        Lista de reuniones seleccionadas
    """
    pass


# RETO 2: Llenar camión con cajas
# ─────────────────────────────────────────────────────────────────────────────
# Tienes un camión con capacidad máxima de peso.
# Hay varias cajas, cada una con un peso y un valor.
# NO puedes partir las cajas (a diferencia de la mochila fraccionaria).
# Maximiza el valor total que puedes cargar.
#
# Nota: Este problema NO siempre se resuelve óptimamente con Greedy,
#       pero intenta una aproximación greedy y analiza cuándo falla.
#
# Ejemplo:
#   capacidad = 10
#   cajas = [(5, 10), (4, 40), (6, 30), (3, 50)]  # (peso, valor)
#   Greedy por valor/peso: selecciona (3,50) y (4,40) → valor = 90
#
def llenar_camion(capacidad, cajas):
    """
    Args:
        capacidad: Peso máximo del camión
        cajas: Lista de tuplas (peso, valor)
    Returns:
        Tupla (valor_total, cajas_seleccionadas)
    """
    pass


# RETO 3: Estaciones de gasolina
# ─────────────────────────────────────────────────────────────────────────────
# Vas a hacer un viaje en carretera. Tu tanque tiene capacidad para
# recorrer K kilómetros. Hay estaciones de gasolina en ciertas posiciones.
# Quieres hacer el MÍNIMO número de paradas para llegar al destino.
#
# Ejemplo:
#   distancia_total = 25
#   capacidad_tanque = 10  # km que puedes recorrer con tanque lleno
#   estaciones = [5, 8, 15, 22]  # posiciones de las estaciones
#   Respuesta: 2 paradas (en km 8 y km 22)
#
def min_paradas_gasolina(distancia_total, capacidad_tanque, estaciones):
    """
    Args:
        distancia_total: Distancia al destino
        capacidad_tanque: Km que puedes recorrer con tanque lleno
        estaciones: Lista de posiciones de estaciones
    Returns:
        Lista de posiciones donde parar, o -1 si es imposible
    """
    pass


# RETO 4: Asignar tareas a servidores
# ─────────────────────────────────────────────────────────────────────────────
# Tienes n tareas y m servidores idénticos.
# Cada tarea tiene un tiempo de ejecución.
# Quieres minimizar el tiempo total (cuando termina el último servidor).
#
# Estrategia: Asignar cada tarea al servidor que esté menos ocupado.
#
# Ejemplo:
#   tareas = [2, 3, 7, 1, 4, 5]
#   servidores = 3
#   Asignación óptima: 
#     Servidor 1: [7] → termina en 7
#     Servidor 2: [5, 2] → termina en 7
#     Servidor 3: [4, 3] → termina en 7
#   Tiempo total: 7
#
def asignar_tareas(tareas, num_servidores):
    """
    Args:
        tareas: Lista de tiempos de ejecución
        num_servidores: Número de servidores disponibles
    Returns:
        Tupla (tiempo_total, asignacion) donde asignacion es lista de listas
    """
    pass


# RETO 5: Comprimir intervalos
# ─────────────────────────────────────────────────────────────────────────────
# Dada una lista de intervalos, combina los que se superponen.
#
# Ejemplo:
#   intervalos = [(1,3), (2,6), (8,10), (15,18)]
#   Respuesta: [(1,6), (8,10), (15,18)]
#
#   intervalos = [(1,4), (4,5)]
#   Respuesta: [(1,5)]  # Se tocan en el punto 4
#
def comprimir_intervalos(intervalos):
    """
    Args:
        intervalos: Lista de tuplas (inicio, fin)
    Returns:
        Lista de intervalos combinados
    """
    pass


# RETO 6: Plataformas de tren (DIFÍCIL)
# ─────────────────────────────────────────────────────────────────────────────
# Una estación de tren tiene trenes que llegan y salen a diferentes horas.
# ¿Cuál es el MÍNIMO número de plataformas necesarias para que
# ningún tren tenga que esperar?
#
# Ejemplo:
#   llegadas =  [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
#   salidas  =  [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
#   Respuesta: 3 plataformas
#
#   Explicación: A las 11:00 hay 3 trenes simultáneos
#   (el de 9:40 sale a 12:00, el de 9:50 sale a 11:20, y llega uno a 11:00)
#
def min_plataformas(llegadas, salidas):
    """
    Args:
        llegadas: Lista de horas de llegada
        salidas: Lista de horas de salida
    Returns:
        Número mínimo de plataformas necesarias
    """
    pass


"""
¡DETENTE AQUÍ!
Intenta resolver los retos antes de ver las soluciones.
▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼
"""


# ═══════════════════════════════════════════════════════════════════════════
#                              SOLUCIONES
# ═══════════════════════════════════════════════════════════════════════════


# SOLUCIÓN RETO 1: Máximo número de reuniones
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ordenar por hora de fin y seleccionar la que termina primero.
# Esto es el clásico "Activity Selection Problem".
#
# Complejidad Temporal: O(n log n) por el ordenamiento
# Complejidad Espacial: O(n) para almacenar reuniones seleccionadas
# ¿Greedy es óptimo? SÍ, está demostrado matemáticamente.
#
def solucion_max_reuniones(reuniones):
    if not reuniones:
        return []
    
    # Ordenar por hora de fin
    reuniones_ordenadas = sorted(reuniones, key=lambda x: x[1])
    
    seleccionadas = [reuniones_ordenadas[0]]
    ultimo_fin = reuniones_ordenadas[0][1]
    
    for inicio, fin in reuniones_ordenadas[1:]:
        if inicio >= ultimo_fin:
            seleccionadas.append((inicio, fin))
            ultimo_fin = fin
    
    return seleccionadas


# SOLUCIÓN RETO 2: Llenar camión con cajas
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ordenar por ratio valor/peso y tomar las mejores que quepan.
#
# Complejidad Temporal: O(n log n) por el ordenamiento
# Complejidad Espacial: O(n) para almacenar cajas con ratio y seleccionadas
# ¿Greedy es óptimo? NO siempre. Este es el problema de la mochila 0/1,
# que requiere programación dinámica para solución óptima.
#
# Contraejemplo: capacidad=10, cajas=[(6,30), (5,25), (5,25)]
#   Greedy: toma (6,30) → no caben las otras → valor = 30
#   Óptimo: toma (5,25) y (5,25) → valor = 50
#
def solucion_llenar_camion(capacidad, cajas):
    # Agregar índice y ratio
    cajas_con_ratio = [(p, v, v/p, i) for i, (p, v) in enumerate(cajas)]
    cajas_con_ratio.sort(key=lambda x: x[2], reverse=True)
    
    valor_total = 0
    seleccionadas = []
    
    for peso, valor, ratio, idx in cajas_con_ratio:
        if peso <= capacidad:
            seleccionadas.append((peso, valor))
            valor_total += valor
            capacidad -= peso
    
    return valor_total, seleccionadas


# SOLUCIÓN RETO 3: Estaciones de gasolina
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ir lo más lejos posible antes de parar. Cuando ya no puedas
# llegar a la siguiente estación, para en la última que podías alcanzar.
#
# Complejidad Temporal: O(n) recorrido lineal de estaciones
# Complejidad Espacial: O(n) para almacenar paradas
# ¿Greedy es óptimo? SÍ
#



# Versión más simple y correcta:
def solucion_min_paradas_v2(distancia_total, capacidad, estaciones):
    estaciones = [0] + sorted(estaciones) + [distancia_total]
    paradas = []
    combustible = capacidad
    
    for i in range(1, len(estaciones)):
        distancia = estaciones[i] - estaciones[i-1]
        
        if distancia > capacidad:
            return -1  # Imposible
        
        if distancia > combustible:
            # Parar en la estación anterior
            paradas.append(estaciones[i-1])
            combustible = capacidad
        
        combustible -= distancia
    
    return paradas


# SOLUCIÓN RETO 4: Asignar tareas a servidores
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ordenar tareas de mayor a menor. Asignar cada tarea al
# servidor menos cargado (usando un heap).
#
# Complejidad Temporal: O(n log n + n log m) donde n=tareas, m=servidores
#   - O(n log n) para ordenar tareas
#   - O(n log m) para n inserciones en heap de m servidores
# Complejidad Espacial: O(m) para el heap de servidores
# ¿Greedy es óptimo? NO siempre, pero da buena aproximación.
#
import heapq

def solucion_asignar_tareas(tareas, num_servidores):
    if not tareas:
        return 0, [[] for _ in range(num_servidores)]
    
    # Ordenar tareas de mayor a menor (LPT - Longest Processing Time)
    tareas_ordenadas = sorted(enumerate(tareas), key=lambda x: -x[1])
    
    # Heap: (carga_actual, id_servidor, lista_tareas)
    servidores = [(0, i, []) for i in range(num_servidores)]
    heapq.heapify(servidores)
    
    for idx_original, tiempo in tareas_ordenadas:
        carga, id_servidor, lista = heapq.heappop(servidores)
        lista.append(tiempo)
        heapq.heappush(servidores, (carga + tiempo, id_servidor, lista))
    
    # Encontrar el tiempo máximo
    tiempo_total = max(s[0] for s in servidores)
    asignacion = [s[2] for s in sorted(servidores, key=lambda x: x[1])]
    
    return tiempo_total, asignacion


# SOLUCIÓN RETO 5: Comprimir intervalos
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ordenar por inicio. Si el siguiente intervalo se superpone
# con el actual, combinarlos. Si no, agregar el actual y empezar uno nuevo.
#
# Complejidad Temporal: O(n log n) por el ordenamiento
# Complejidad Espacial: O(n) para almacenar intervalos comprimidos
# ¿Greedy es óptimo? SÍ
#
def solucion_comprimir_intervalos(intervalos):
    if not intervalos:
        return []
    
    # Ordenar por inicio
    intervalos = sorted(intervalos, key=lambda x: x[0])
    
    resultado = [list(intervalos[0])]
    
    for inicio, fin in intervalos[1:]:
        ultimo = resultado[-1]
        
        if inicio <= ultimo[1]:  # Se superponen o tocan
            ultimo[1] = max(ultimo[1], fin)  # Extender
        else:
            resultado.append([inicio, fin])
    
    return [tuple(i) for i in resultado]


# SOLUCIÓN RETO 6: Plataformas de tren
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Ordenar todos los eventos (llegadas y salidas).
# Recorrer cronológicamente: +1 por llegada, -1 por salida.
# El máximo en cualquier momento es el número de plataformas.
#
# Complejidad Temporal: O(n log n) por el ordenamiento de eventos
# Complejidad Espacial: O(n) para almacenar la lista de eventos
# ¿Greedy es óptimo? SÍ
#
def solucion_min_plataformas(llegadas, salidas):
    # Crear eventos: (tiempo, tipo) donde tipo=1 es llegada, tipo=-1 es salida
    eventos = []
    for t in llegadas:
        eventos.append((t, 1))   # Llegada
    for t in salidas:
        eventos.append((t, -1))  # Salida
    
    # Ordenar por tiempo. Si empatan, procesar salidas primero (-1 < 1)
    eventos.sort(key=lambda x: (x[0], x[1]))
    
    plataformas_actuales = 0
    max_plataformas = 0
    
    for tiempo, tipo in eventos:
        plataformas_actuales += tipo
        max_plataformas = max(max_plataformas, plataformas_actuales)
    
    return max_plataformas


# ═══════════════════════════════════════════════════════════════════════════
#                           CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("VERIFICACIÓN DE SOLUCIONES")
    print("=" * 60)
    
    # Reto 1
    print("\n1. MÁXIMO REUNIONES")
    reuniones = [(9, 10), (9, 12), (10, 11), (11, 13), (12, 14)]
    print(f"   Reuniones: {reuniones}")
    print(f"   Seleccionadas: {solucion_max_reuniones(reuniones)}")
    
    # Reto 2
    print("\n2. LLENAR CAMIÓN")
    cajas = [(5, 10), (4, 40), (6, 30), (3, 50)]
    valor, selec = solucion_llenar_camion(10, cajas)
    print(f"   Cajas (peso, valor): {cajas}")
    print(f"   Capacidad: 10")
    print(f"   Valor obtenido: {valor}, Cajas: {selec}")
    
    # Reto 3
    print("\n3. ESTACIONES DE GASOLINA")
    paradas = solucion_min_paradas_v2(25, 10, [5, 8, 15, 22])
    print(f"   Distancia: 25, Tanque: 10km, Estaciones: [5, 8, 15, 22]")
    print(f"   Paradas necesarias: {paradas}")
    
    # Reto 4
    print("\n4. ASIGNAR TAREAS")
    tiempo, asig = solucion_asignar_tareas([2, 3, 7, 1, 4, 5], 3)
    print(f"   Tareas: [2, 3, 7, 1, 4, 5], Servidores: 3")
    print(f"   Tiempo total: {tiempo}")
    print(f"   Asignación: {asig}")
    
    # Reto 5
    print("\n5. COMPRIMIR INTERVALOS")
    intervalos = [(1,3), (2,6), (8,10), (15,18)]
    print(f"   Intervalos: {intervalos}")
    print(f"   Comprimidos: {solucion_comprimir_intervalos(intervalos)}")
    
    # Reto 6
    print("\n6. PLATAFORMAS DE TREN")
    llegadas = [9.00, 9.40, 9.50, 11.00, 15.00, 18.00]
    salidas = [9.10, 12.00, 11.20, 11.30, 19.00, 20.00]
    print(f"   Llegadas: {llegadas}")
    print(f"   Salidas:  {salidas}")
    print(f"   Plataformas necesarias: {solucion_min_plataformas(llegadas, salidas)}")
    
    print("\n" + "=" * 60)
    print("RESUMEN DE COMPLEJIDADES")
    print("=" * 60)
    print("""
    ┌────┬─────────────────────────┬─────────────┬─────────────┬───────────────┐
    │ #  │ Reto                    │ Tiempo      │ Espacio     │ ¿Greedy óptimo?│
    ├────┼─────────────────────────┼─────────────┼─────────────┼───────────────┤
    │ 1  │ Máximo reuniones        │ O(n log n)  │ O(n)        │ SÍ            │
    │ 2  │ Llenar camión (0/1)     │ O(n log n)  │ O(n)        │ NO siempre    │
    │ 3  │ Estaciones gasolina     │ O(n)        │ O(n)        │ SÍ            │
    │ 4  │ Asignar tareas          │ O(n log n)  │ O(m)        │ NO siempre    │
    │ 5  │ Comprimir intervalos    │ O(n log n)  │ O(n)        │ SÍ            │
    │ 6  │ Plataformas de tren     │ O(n log n)  │ O(n)        │ SÍ            │
    └────┴─────────────────────────┴─────────────┴─────────────┴───────────────┘
    """)
