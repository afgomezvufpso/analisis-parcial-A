import math

def esPrimo(n): 
    if n <= 1:
        return False
    for i in range(2, int(math.sqrt(n)) + 1): # O(n)
        if n % i == 0:
            return False
    return True

def cuantosNum(arr):
    count = 0
    for i in arr: # O(n)
        if esPrimo(i): 
            count += 1
    return count

array = [5, 7, 8, 9, 10, 13]

print(f"El intervalo de Isaac hay {cuantosNum(array)} primos")

# El algoritmo construido es O(n^2)
