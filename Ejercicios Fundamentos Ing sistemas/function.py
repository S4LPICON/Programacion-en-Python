def es_deficiente(n:int)->bool:
    s = 0
    k = 1
    while(k<=n/2):
        if ((n % k)== 0):
            s = s + k
        else:
            pass
        k = k+1
    if (s<n):
        rta = True
    else:
        rta = False
    return rta

def sumar_intervalo(a,b):
    s=0
    k=a
    while (k<=b):
        if (es_deficiente(k)==True):
            s=s+k
        else:
            pass
        k+=1
    return s


print(sumar_intervalo(100,1000))


print (es_deficiente(10))