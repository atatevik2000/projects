a=input()
b=a[1:-1].split(',')
slovar = dict()
print(b)
for i in b:
    slovar[i]=a.count(i)
print(slovar)