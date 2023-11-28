from  math import gcd, lcm
import random

num1 = int(input("Mínimo número: "))
num2 = int(input("Máximo número: "))

for i in range(2):
    numrd1 = random.randint(num1, num2)
    numrd2 = random.randint(num1, num2)

print("Máximo común divisor: ", gcd(numrd1, numrd2))
print("Mínimo común múltiplo: ", lcm(numrd1, numrd2))
