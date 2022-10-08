from math import *
num = int(input())
k = True
for i in range(2,num-1):
    if num % i == 0:
        k = False
        break
if k:
    print("Is PRIME")
else:
    print("is not PRIME")