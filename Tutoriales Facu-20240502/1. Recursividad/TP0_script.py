## TP Recursividad

#%% Ejercicio 1) Torre de Hanoi

def hanoi(n, i, j): # n discos deben ser movidos de la vara i a la vara j (3 varas)
    solution = []
    if n == 1:
        solution.extend([(n, i, j)])
    else:
        k = 6 - i - j # 1 + 2 + 3 = 6
        solution.extend(hanoi(n-1, i, k))
        solution.extend([(n, i, j)])
        solution.extend(hanoi(n-1, k, j))
    return solution

# ### b)

import matplotlib.pyplot as plt

len_hanoi = []
for i in range(1, 17):
    len_hanoi_i = len(hanoi(i, 1, 3)) 
    len_hanoi.append(len_hanoi_i)
   
plt.plot(list(range(1, 17)), len_hanoi, label = 'Hanoi moves')
plt.xlabel('N')
plt.ylabel('Number of moves')
plt.legend()

# ### d)

total_movimientos = 2**64 - 1
total_minutos_anio = 60*24*365
total_anios = total_movimientos / total_minutos_anio
print(f'Faltarían {total_anios} años hasta el fin del mundo')

# ### e)


# Si se tienen 65 varas para resolver el problema de 64 discos, la estrategia sería como sigue:
# 
# 1. Mover cada uno de los 63 discos más pequeños a su propia vara, uno por uno, lo que tomaría 63 movimientos.
# 2. Mover el disco más grande (el disco número 64) al poste objetivo, lo que tomaría 1 movimiento más.
# 3. Mover los 63 discos restantes sobre el disco más grande en el poste objetivo, lo que tomaría 63 movimientos adicionales.
# 
# En total, esto sumaría 63 (para los primeros n-1 discos) + 1 (para el disco más grande) + 63 (para mover los n-1 a la vara objetivo) = 127 = 64*2-1
# 

#%% Ejercicio 2) Fibonacci

# ### a)
def Fib1(n):
    if n <= 2:
        return 1
    return Fib1(n-1) + Fib1(n-2)

Fib1(6)

# ### b)

import math

def Fib2(n):
    sqrt_5 = math.sqrt(5)
    phi = (1 + sqrt_5) / 2
    psi = (1 - sqrt_5) / 2
    return int((phi**n - psi**n) / sqrt_5)

fib_table = [{"n": n, "Fib1": Fib1(n), "Fib2": Fib2(n)} for n in range(1, 21)]

fib_table


# ### c) 

import time
start_recursive = time.perf_counter_ns()
for i in range(1, 41):
    Fib1(i)
end_recursive = time.perf_counter_ns()
time_recursive = end_recursive - start_recursive

start_explicit = time.perf_counter_ns()
for i in range(1, 41):
    Fib2(i)

end_explicit = time.perf_counter_ns()
time_explicit = end_explicit - start_explicit

(time_recursive, time_explicit)  # tiempo en nanosegundos

f'{(time_recursive / time_explicit - 1)*100}%'

# ### d)

def Fib3(n):
    if n <= 2:
        return 1
    f1, f2 = 1, 1
    for _ in range(3, n + 1):
        f1, f2 = f2, f1 + f2
    return f2

def Fib4(n, memoria=None):
    if memoria is None:
        memoria = {1: 1, 2: 1}
    if n in memoria:
        return memoria[n]
    memoria[n] = Fib4(n-1, memoria) + Fib4(n-2, memoria)
    return memoria[n]


start_fib3 = time.perf_counter_ns()
for i in range(1, 41):
    Fib3(i)
end_fib3 = time.perf_counter_ns()
time_fib3 = end_fib3 - start_fib3

# Medimos el tiempo para Fib4
start_fib4 = time.perf_counter_ns()
for i in range(1, 41):
    Fib4(i)
end_fib4 = time.perf_counter_ns()
time_fib4 = end_fib4 - start_fib4

(time_fib3, time_fib4)  # tiempo en nanosegundos



#%% Ejercicio 3) MCD

# ### a)

def prime_factors(n):
    factors = []
    divisor = 2     # Comienza con el menor factor primo posible

    while divisor * divisor <= n: # Continúa hasta que el divisor sea mayor que la raíz cuadrada de 'n'
        while n % divisor == 0: # Mientras el divisor sea un factor de 'n', divide 'n' y guarda el divisor
            n = n // divisor   # Divide 'n' entre 'divisor' (quedas con un numero entero)
            factors.append(divisor)  # Añade el factor primo a la lista
        
        divisor += 1 # Incrementa el divisor para comprobar el siguiente número primo potencial

    # Si queda algún número mayor que 1, es un factor primo
    if n > 1:
        factors.append(n)  # Añade el último factor primo, si lo hay
    return factors


prime_factors(120)

# Definición de la función mcd1, que utiliza la descomposición en factores primos para calcular el MCD.
def mcd1(a, b):
    # Obtenemos los factores primos de ambos números
    a_factors = prime_factors(a)
    b_factors = prime_factors(b)
    
    # Encuentra los factores comunes
    common_factors = set(a_factors) & set(b_factors)
    
    # Calcula el MCD multiplicando los factores comunes elevados al menor exponente que aparecen en ambos números
    mcd = 1
    for factor in common_factors:
        cantidad_factor_en_a = a_factors.count(factor)
        cantidad_factor_en_b = b_factors.count(factor)
        minima_cantidad = min(cantidad_factor_en_a, cantidad_factor_en_b)
        mcd *= factor ** minima_cantidad
    return mcd


def mcd2(a, b):
    while b != 0:
        # El nuevo 'a' es 'b' y el nuevo 'b' es el resto de la división de 'a' entre 'b'
        a, b = b, a % b
    # Cuando 'b' se convierte en 0, 'a' contiene el MCD
    return a

mcd1_result = mcd1(48, 180)  # Utilizando descomposición en factores primos
mcd2_result = mcd2(48, 180)  # Utilizando el algoritmo de Euclides

mcd1_result, mcd2_result



# ### b)

a = 12345678901234567890
b = 98765432109876543210

# Medimos el tiempo para mcd1 (descomposición en factores primos)
start_mcd1 = time.perf_counter_ns()
mcd1(a, b)
end_mcd1 = time.perf_counter_ns()
time_mcd1 = end_mcd1 - start_mcd1

# Medimos el tiempo para mcd2 (algoritmo de Euclides)
start_mcd2 = time.perf_counter_ns()
mcd2(a, b)
end_mcd2 = time.perf_counter_ns()
time_mcd2 = end_mcd2 - start_mcd2

time_mcd1, time_mcd2


# ### c)


#%% Ejercicio 4) Números Romanos

def r2i(roman):

    roman_to_int = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    
    # Caso base: cadena vacía
    if not roman:
        return 0
    
    # Si la cadena tiene un solo carácter, devuelve su valor
    if len(roman) == 1:
        return roman_to_int[roman]
    
    # Caso de sustracción: numeral menor antes de uno mayor
    if roman_to_int[roman[0]] < roman_to_int[roman[1]]:
        return r2i(roman[1:]) - roman_to_int[roman[0]]
    
    # Caso de adición: numeral mayor o igual antes
    return roman_to_int[roman[0]] + r2i(roman[1:])

def i2r(numero):

    roman_numerals = [
        ('M', 1000), ('D', 500), ('C', 100), ('L', 50),
        ('X', 10), ('V', 5), ('I', 1)
    ]
    
    # Tuplas para casos de sustracción
    substractive_numerals = [('C', 100), ('X', 10), ('I', 1)]

    # Caso base: número es 0
    if numero == 0:
        return ""
    
    # Encuentra el mayor valor romano menor o igual que 'numero'
    for numeral, value in roman_numerals:
        if value <= numero:
            return numeral + i2r(numero - value)
        
        # Verifica si puede ser escrito como sustracción
        for substraction_numeral, substraction_value in substractive_numerals:
            # Evita la repetición de pares de sustracción
            if value * 0.1 <= substraction_value < value:
                substracted_value = value - substraction_value
                # Asegura un numeral de sustracción válido
                if 0 < substracted_value <= numero:
                    return substraction_numeral + numeral + i2r(numero - substracted_value)



r2i('MCX')


test_cases = [1, 3, 4, 7, 9, 10, 40, 49, 50, 90, 99, 100, 400, 500, 900, 1000, 1477, 1984, 2022, 3999]

i2r_test_results = [(number, i2r(number)) for number in test_cases]

r2i_test_results = [(roman, r2i(roman)) for _, roman in i2r_test_results]

combined_test_results = [(number, roman, converted) for ((number, roman), (_, converted)) in zip(i2r_test_results, r2i_test_results)]

combined_test_results


#%% Ejercicio 6) Química

elementos_quimicos = ['Actinium', 'Aluminum', 'Americium', 'Antimony', 'Argon', 'Arsenic'
     , 'Astatine', 'Barium', 'Berkelium', 'Beryllium', 'Bismuth', 'Bohrium'
     , 'Boron', 'Bromine', 'Cadmium', 'Calcium', 'Californium', 'Carbon'
     , 'Cerium', 'Cesium', 'Chlorine', 'Chromium', 'Cobalt', 'Copernicium'
     , 'Copper', 'Curium', 'Darmstadtium', 'Dubnium', 'Dysprosium', 'Einsteinium'
     , 'Erbium', 'Europium', 'Fermium', 'Flerovium', 'Fluorine', 'Francium'
     , 'Gadolinium', 'Gallium', 'Germanium', 'Gold', 'Hafnium', 'Hassium'
     , 'Helium', 'Holmium', 'Hydrogen', 'Indium', 'Iodine', 'Iridium', 'Iron'
     , 'Krypton', 'Lanthanum', 'Lawrencium', 'Lead', 'Lithium', 'Livermorium'
     , 'Lutetium', 'Magnesium', 'Manganese', 'Meitnerium', 'Mendelevium', 'Mercury'
     , 'Molybdenum', 'Moscovium', 'Neodymium', 'Neon', 'Neptunium', 'Nickel'
     , 'Nihonium', 'Niobium', 'Nitrogen', 'Nobelium', 'Oganesson', 'Osmium'
     , 'Oxygen', 'Palladium', 'Phosphorus', 'Platinum', 'Plutonium', 'Polonium'
     , 'Potassium', 'Praseodymium', 'Promethium', 'Protactinium', 'Radium', 'Radon'
     , 'Rhenium', 'Rhodium', 'Roentgenium', 'Rubidium', 'Ruthenium', 'Rutherfordium'
     , 'Samarium', 'Scandium', 'Seaborgium', 'Selenium', 'Silicon', 'Silver'
     , 'Sodium', 'Strontium', 'Sulfur', 'Tantalum', 'Technetium', 'Tellurium'
     , 'Tennessine', 'Terbium', 'Thallium', 'Thorium', 'Thulium', 'Tin', 'Titanium'
     , 'Tungsten', 'Uranium', 'Vanadium', 'Xenon', 'Ytterbium', 'Yttrium', 'Zinc'
     , 'Zirconium']

def encontrar_secuencia_mas_larga(elemento, elementos_quimicos_set, secuencia=[]):

    secuencia.append(elemento)

    # Buscar posibles candidatos para continuar la secuencia
    secuencia_set = set(secuencia)
    candidatos_posibles = elementos_quimicos_set - secuencia_set
    candidatos = [e for e in candidatos_posibles if e.startswith(elemento[-1].upper())]

    # Variable para guardar la secuencia más larga encontrada
    secuencia_mas_larga = list(secuencia)

    # Explorar cada candidato para continuar la secuencia
    for candidato in candidatos:
        nueva_secuencia = encontrar_secuencia_mas_larga(candidato, elementos_quimicos_set, list(secuencia))
        if len(nueva_secuencia) > len(secuencia_mas_larga):
            secuencia_mas_larga = nueva_secuencia

    # Devolver la secuencia más larga encontrada
    return secuencia_mas_larga


test_nombre_elemento = 'Magnesium'
test_secuencia = encontrar_secuencia_mas_larga(test_nombre_elemento, set(elementos_quimicos), secuencia=[])

test_secuencia  


#%% ## Ejercicio 7) Raíz Cuadrada
def raiz_cuadrada_recursiva(n, guess = 1.0):

    tolerancia = 10**(-12)
    if abs(n - guess**2) <= tolerancia:
        solution = guess
    else:
        solution = raiz_cuadrada_recursiva(n, (guess + n/guess)/2)
    return solution


test_numbers = [1, 2, 9, 16, 20, 25, 100, 163, 10000]

for n in test_numbers:
    print(f"N = {n}\n"
          f"Guess:{raiz_cuadrada_recursiva(n)}\n"
          f"Real: {n**(0.5)}")



