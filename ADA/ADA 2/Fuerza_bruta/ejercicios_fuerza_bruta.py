"""
═══════════════════════════════════════════════════════════════════════════════
              EJERCICIOS DE FUERZA BRUTA - ANÁLISIS DE COMPLEJIDAD
═══════════════════════════════════════════════════════════════════════════════

Resuelve cada ejercicio usando fuerza bruta (la solución más directa).
Luego analiza la complejidad de tu solución.

═══════════════════════════════════════════════════════════════════════════════
                              ENUNCIADOS
═══════════════════════════════════════════════════════════════════════════════
"""


# EJERCICIO 1: Elemento mayoritario
# ─────────────────────────────────────────────────────────────────────────────
# Dado un arreglo de enteros, encontrar el elemento que aparece más de n/2 veces.
# Se garantiza que siempre existe un elemento mayoritario.
#
# Ejemplo:
#   entrada: [3, 3, 4, 2, 3, 3, 5, 3, 3]
#   salida: 3 (aparece 6 veces, n/2 = 4.5)
#
def elemento_mayoritario(arr:list[int])->int:        
    pass


# EJERCICIO 2: Subarreglo de suma máxima
# ─────────────────────────────────────────────────────────────────────────────
# Dado un arreglo de enteros (puede tener negativos), encontrar el subarreglo
# contiguo con la suma más grande. Retornar la suma.
#
# Ejemplo:
#   entrada: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
#   salida: 6 (el subarreglo [4, -1, 2, 1] tiene suma 6)
#
def suma_maxima_subarreglo(arr):
    max_sum = 0
   
    for i in range(len(arr)):
        for j in range(0,len(arr)-1,-1):
         max_sum += arr[i]
        
       
    pass


# EJERCICIO 3: Tres elementos que sumen cero
# ─────────────────────────────────────────────────────────────────────────────
# Dado un arreglo de enteros, determinar si existen tres elementos distintos
# (por posición) cuya suma sea exactamente 0. Retornar True/False.
#
# Ejemplo:
#   entrada: [-1, 0, 1, 2, -1, -4]
#   salida: True (porque -1 + 0 + 1 = 0)
#
def tres_suman_cero(arr):
    pass


# EJERCICIO 4: Cadena con todos los caracteres únicos
# ─────────────────────────────────────────────────────────────────────────────
# Dada una cadena, determinar si todos sus caracteres son únicos
# (no se repite ninguno). NO usar estructuras de datos adicionales.
#
# Ejemplo:
#   entrada: "abcdef"  → True
#   entrada: "abcaef"  → False (la 'a' se repite)
#
def caracteres_unicos(texto):
    pass


# EJERCICIO 5: Potencia de un número (recursivo)
# ─────────────────────────────────────────────────────────────────────────────
# Calcular base^exponente usando recursión por fuerza bruta.
# No usar el operador ** ni la función pow().
#
# Ejemplo:
#   entrada: base=2, exponente=10
#   salida: 1024
#
def potencia(base, exponente):
    pass


"""
¡DETENTE AQUÍ!
Intenta resolver los ejercicios antes de ver las soluciones.
▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼ ▼
"""


# ═══════════════════════════════════════════════════════════════════════════
#                              SOLUCIONES
# ═══════════════════════════════════════════════════════════════════════════


# SOLUCIÓN 1: Elemento mayoritario
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Para cada elemento, contamos cuántas veces aparece recorriendo
# todo el arreglo. Si aparece más de n/2 veces, es el mayoritario.
#
# Complejidad: O(n²)
#   - El ciclo externo recorre n elementos
#   - Para cada uno, el ciclo interno cuenta ocurrencias en n elementos
#   - Total: n × n = O(n²)
# Espacio: O(1) - solo usamos variables simples
#
def solucion_elemento_mayoritario(arr):
    n = len(arr)
    for candidato in arr:
        conteo = 0
        for elemento in arr:
            if elemento == candidato:
                conteo += 1
        if conteo > n // 2:
            return candidato
    return None


# SOLUCIÓN 2: Subarreglo de suma máxima
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Probamos TODOS los subarreglos posibles. Para cada par de
# índices (i, j), calculamos la suma del subarreglo arr[i..j].
#
# Complejidad: O(n³)
#   - Primer ciclo: elige el inicio i → n opciones
#   - Segundo ciclo: elige el fin j → hasta n opciones
#   - Tercer ciclo: suma los elementos entre i y j → hasta n operaciones
#   - Total: n × n × n = O(n³)
# Espacio: O(1)
#
def solucion_suma_maxima_subarreglo(arr):
    n = len(arr)
    max_suma = arr[0]
    
    for i in range(n):             # inicio del subarreglo
        for j in range(i, n):      # fin del subarreglo
            suma = 0
            for k in range(i, j + 1):  # sumar elementos de i a j
                suma += arr[k]
            max_suma = max(max_suma, suma)
    
    return max_suma


# SOLUCIÓN 3: Tres elementos que sumen cero
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Probamos TODAS las combinaciones de tres elementos usando
# tres ciclos anidados.
#
# Complejidad: O(n³)
#   - Tres ciclos anidados, cada uno recorre hasta n elementos
#   - Total: n × n × n = O(n³)
# Espacio: O(1)
#
def solucion_tres_suman_cero(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                if arr[i] + arr[j] + arr[k] == 0:
                    return True
    return False


# SOLUCIÓN 4: Cadena con todos los caracteres únicos
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: Comparamos cada carácter con todos los que vienen después.
# Si encontramos dos iguales, retornamos False.
#
# Complejidad: O(n²)
#   - Ciclo externo: recorre n caracteres
#   - Ciclo interno: compara con los restantes (hasta n)
#   - Total: n × n = O(n²)
# Espacio: O(1) - no usamos estructuras adicionales (como pide el enunciado)
#
def solucion_caracteres_unicos(texto):
    n = len(texto)
    for i in range(n):
        for j in range(i + 1, n):
            if texto[i] == texto[j]:
                return False
    return True


# SOLUCIÓN 5: Potencia de un número (recursivo)
# ─────────────────────────────────────────────────────────────────────────────
# Estrategia: base^exp = base × base^(exp-1)
# Reducimos el exponente en 1 en cada llamada recursiva hasta llegar a 0.
#
# Ejemplo: 2^4 = 2 × 2^3 = 2 × 2 × 2^2 = 2 × 2 × 2 × 2^1 = 2 × 2 × 2 × 2 × 2^0
#                                                              = 2 × 2 × 2 × 2 × 1
#                                                              = 16
#
# Complejidad: O(n) donde n = exponente
#   - Se hacen exactamente n llamadas recursivas (una por cada decremento)
# Espacio: O(n) - cada llamada recursiva ocupa espacio en el call stack
#
def solucion_potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * solucion_potencia(base, exponente - 1)


# ═══════════════════════════════════════════════════════════════════════════
#                           CÓDIGO DE PRUEBA
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    print("=" * 60)
    print("VERIFICACIÓN DE SOLUCIONES")
    print("=" * 60)
    
    # Ejercicio 1
    print("\n1. Elemento mayoritario")
    print(f"   [3,3,4,2,3,3,5,3,3] → {solucion_elemento_mayoritario([3,3,4,2,3,3,5,3,3])}")
    print(f"   [1,1,1,2,2] → {solucion_elemento_mayoritario([1,1,1,2,2])}")
    
    # Ejercicio 2
    print("\n2. Suma máxima de subarreglo")
    print(f"   [-2,1,-3,4,-1,2,1,-5,4] → {solucion_suma_maxima_subarreglo([-2,1,-3,4,-1,2,1,-5,4])}")
    print(f"   [1,2,3,4] → {solucion_suma_maxima_subarreglo([1,2,3,4])}")
    
    # Ejercicio 3
    print("\n3. Tres elementos que sumen cero")
    print(f"   [-1,0,1,2,-1,-4] → {solucion_tres_suman_cero([-1,0,1,2,-1,-4])}")
    print(f"   [1,2,3,4,5] → {solucion_tres_suman_cero([1,2,3,4,5])}")
    
    # Ejercicio 4
    print("\n4. Caracteres únicos")
    print(f"   'abcdef' → {solucion_caracteres_unicos('abcdef')}")
    print(f"   'abcaef' → {solucion_caracteres_unicos('abcaef')}")
    
    # Ejercicio 5
    print("\n5. Potencia (recursivo)")
    print(f"   2^10 → {solucion_potencia(2, 10)}")
    print(f"   3^4  → {solucion_potencia(3, 4)}")
    
    print("\n" + "=" * 60)
    print("RESUMEN DE COMPLEJIDADES")
    print("=" * 60)
    print("""
    ┌────┬──────────────────────────┬──────────┬──────────┐
    │ #  │ Ejercicio                │ Tiempo   │ Espacio  │
    ├────┼──────────────────────────┼──────────┼──────────┤
    │ 1  │ Elemento mayoritario     │ O(n²)    │ O(1)     │
    │ 2  │ Suma máxima subarreglo   │ O(n³)    │ O(1)     │
    │ 3  │ Tres suman cero          │ O(n³)    │ O(1)     │
    │ 4  │ Caracteres únicos        │ O(n²)    │ O(1)     │
    │ 5  │ Potencia (recursivo)     │ O(n)     │ O(n)     │
    └────┴──────────────────────────┴──────────┴──────────┘

    Nota: Todas estas son soluciones de fuerza bruta. Existen
    soluciones más eficientes para cada problema.
    """)
