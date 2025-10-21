import math as m

#1. T1(n) = 3n^2 + 50n
def t1(n):
    return 3*(n**2) + 50*n

#2. T2(n) = 8nlog2(n) + 200
def t2(n):
    return 8*n*m.log2(n) + 200

#3. T3(n) = 0.2n^3
def t3(n):
    return 0.2*(n**3)

#4. T4(n) = 2^n
def t4(n):
    return 2**n

def cruce(f,g):
    for i in range(1,100000):
        if f(i) > g(i):
            return i
    return None

# Compararé: Insertion sort vs Merge sort
# Sabiendo que: 
#               T1(n) es un insertion sort (O(n^2))
#               T2(n) es un merge sort (O(n log n))
# Pregunta: ¿A partir de qué valor de n el merge sort se comporta mejor?
#
# Busco el punto donde:
#                   T1(n) > T2(n)
#           es decir, donde el costo del insertion supera al del merge.

print(f"El merge sort es más eficiente a partir de n ≈ {cruce(t1,t2)}")