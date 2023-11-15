def fact(n):
    k=n
    f=1
    while(k>0):
        f*=k
        k-=1
    return f
print(fact(5))

def funfact(n,x):
    n*=fact(x)
    return n

print((funfact(10,4)))


def factorial_r(n):
    if (n==0):
        return 1
    else:
        return n*fact(n-1)
print(fact(3))


def hola(x,y):
    return x**y
    

h = hola(2,3)
print("Potencia es:")
print(hola(2,3))


def potencia_rec(x:float,e:int)->float:
    if (e==0):
        rta=1
    else:
        if(e>0):
            rta= x * (potencia_rec(x,e-1))
        else:
            rta= 1/ potencia_rec(x,-e)
    return rta


print(potencia_rec(2,-3))