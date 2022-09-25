from math import sqrt
print("Введите номер примера")
inp = int(input())
if inp == 1:
    x0=[1,1,0,0,0]
    a=[2,-1,1,0,1]
    b=[0,1,3,0,-2]
else:
    x0=[1,1,0,0]
    a=[1,2,3,-1]
    b=[-1,2,0,3]
beta = 0.125
l1 = 0
l2 =2
l0 = [l1, l2]
xk =  x0
eps =0.001
iteracii = 0
def J(x):
    j=0
    for i in range(len(x)):
        j+=(x[i]-a[i])**2
    return j

def J_x(x):
    j_shtrix=[]
    for i in range(len(x)):
        j_shtrix.append(2*(x[i] - a[i]))
    return j_shtrix

def normab_2(x):
    norma_b = 0
    for i in range(len(b)):
        norma_b += b[i]**2
    return norma_b

def b_x(x):
    bx = 0
    for i in range(len(b)):
        bx += b[i]*x[i]
    return bx

def normax_2(x):
    norma_x =0
    for i in range(len(x)):
        norma_x += x[i]**2
    return norma_x 

def g_1(x):
    norma_x = normax_2(x)
    bx = b_x(x)
    g1 = norma_x - 2*bx
    return g1

def g_2(x):
    g_2 =0
    bx = b_x(x)
    norma_b = normab_2(x)
    g2 = norma_b - bx
    return g2

def g1_shtrix(x):
    g1_shtrix=[]
    for i in range(len(b)):
        g1_shtrix = x[i]-b[i]
    g1_shtrix = 2*g1_shtrix    
    return g1_shtrix     

def g2_shtrix(x):
    g2shtrix = []
    for i in range(len(b) ):
        g2shtrix.append(- b[i])
    return g2shtrix

def L_x(xk):
    l_x=[]
    for i in range(len(x0)): 
        t = 2*(xk[i] - a[i]) +l1*2*(xk[i] - b[i]) - l2*b[i]
        l_x.append(t)
    return l_x

def L_l(xk):
    l_l=[]
    g1 = g_1(xk)
    g2 = g_2(xk)   
    l_l = [g1, g2]
    return l_l

x_k = []
l_k = []
xk = x0
xk_minus1 =[]
xk_1 = []
lk_1 = []
x_k_1 = []
l_k_1 = []
lk = l0
l_x = L_x(xk)

while True :
    for i in range(len(xk)):
        x_k_1.append(xk[i] - beta * l_x[i])
    x_k = x_k_1
    x_k_1 = []
    l_l = L_l(xk)
    for i in range(len(l0)):
        l_k_1.append(lk[i] + beta * l_l[i])
    l_k = l_k_1
    l_k_1 =[]
    if l_k[i] < 0:
        l_k[i] = 0
    xk_k_1=[]
    l_x = L_x(x_k)
    xk_minus1 = xk
    for i in range(len(x0)):   
        xk_1.append(xk[i] - beta * l_x[i])
    xk= xk_1
    xk_1 = []
    l_l = L_l(x_k)
    for i in range(len(lk)):
        lk_1.append( lk[i] + beta * l_l[i])
    lk = lk_1
    lk_1=[]
    j_raznost_1 = J(xk)
    j_raznost_2 = J(xk_minus1)
    j_raznost = j_raznost_1 - j_raznost_2
    if j_raznost < 0:
        j_raznost= - j_raznost
    norma_shtrix =normax_2(xk)
    norma_shtrix= sqrt(norma_shtrix)
    for i in range(len(xk)):
        xk_k_1.append(xk[i]- xk_minus1[i])
    norma_xk_k_1 = normax_2(xk_k_1)
    norma_xk_k_1 = sqrt(norma_xk_k_1)
    iteracii+=1
    if j_raznost <= eps or norma_shtrix <= eps or norma_xk_k_1 <= eps :
        break
xk_k=[]

for i in range(len(xk)):
    xk_k.append(int(xk[i]*10000) / 10000)
print("Решение")
print(xk_k)
print("Количество итераций = ", iteracii)


