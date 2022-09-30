
n=5
def diag(n):
    c=0
    for i in range(n):
        for j in range(n):

            if j==0 or j==n-1:
                print("*", end = '\t')
            elif j == i:
                print("*", end = '\t')
            else:
                print(" ", end = '\t')
        print()

    print()

def diag_kv(n):
    for i in range(n):
        for j in range(n):
            if (i == 0 or i == n-1) or (j==0 or j==n-1):
                print("*", end = '\t')
            elif j == i:
                print("*", end = '\t')
            else:
                print(" ", end = '\t')
        print()
        

diag(n)
print()
print()
diag_kv(n)
