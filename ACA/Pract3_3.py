def rectangle(a,b):
    area = a*b
    perimetr = (a+b)*2
    print("area is {}, perimetr is {}".format(area, perimetr))
a = input()
a=a.split()

if len(a) == 1:
    x, y= int(a[0]), int(a[0])
else:
    x, y = int(a[0]), int(a[1])
rectangle(x,y)
