import math as m

#1. T1(n) = 3n^2 + 50n
def t1(i):
    return 3*(i**2) + 50*i

#2. T2(n) = 8nlog2(n) + 200
def t2(i):
    return 8*i*m.log2(i) + 200

#3. T3(n) = 0.2n^3
def t3(i):
    return 0.2 * i**3

#4. T4(n) = 2^n
def t4(i):
    return 2**i

def cruce(f,g):
    for i in range(1,1000000):
        if(f(i) > g(i)):
            return i
    return None

# Compararé: Insertion sort vs Merge sort
# Sabiendo que: 
#               T1(n) es un insertion sort
#               T2(n) es un merge sort
# Pregunta: En que punto o a partir de que valor(i) el merge sort se comporta mas rapido? o es mejor?
#
#                   T1(n) < T2(n)
#              3n^2 + 50n < 8nlog2(n) + 200

print(f"El merge sort es mas rapido a partir del num: {cruce(t1,t2)}")

#Segun lo aplicado es mas rapido a partir del 5