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

print((funfact(1000000,4000)))