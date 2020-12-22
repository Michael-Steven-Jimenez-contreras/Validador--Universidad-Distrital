import MCM_y_MCD as md

def clean_l(a:list):#organiza la lista poniendo el 1 al principio
    n=[1]
    for i in range(len(a)):
        if a[i]!=1:
            n.append(a[i])
    return n

def pfactor(n,primos=[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227, 229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281, 283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353, 359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421, 431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487, 491, 499, 503, 509, 521, 523, 541, 547]):#halla el primer factor primo de un numero n 
    f=2
    c=(primos[len(primos)-1]-1)/2 #es mas eficiente si se le da una lista para que elimine primos conocidos, cuando termina la lista necesita un numero impar desde el que partir para seguir buscando primos
    for i in range(len(primos)):
        if n%primos[i]==0:
            return int(primos[i])
    while(n%f!=0) and f<=int(pow(n,0.5)):#solo comprueba los numeros primos hasta la raiz de n
        f=2*c+1#todos los numeros primos diferentes de 2 son impares y tienen la forma 2c+1
        c=c+1
    if (int(n/f)!=(n/f)):#Cuando se pasa el limite de la raiz, lo ultimo que hace es fijar como factor de n a n
        f=n
    return int(f)

def factor(n,clear=False,a=[]):#pone en una lista los factores primos de un numero
    if clear:#si la opcion clear esta activa limpia la lista actual
        a=[]
    a.append(pfactor(n))#añade el primer factor de n
    if n>1:
        return factor(n/pfactor(n),False,a)#si n>1 entonces busca el factor de n/pfactor(n), ejem:(n=16,pfact(16)->16/2->8, entonces se llama a factor(8)) y se pasa la lista actual
    return clean_l(a)#devuelve la lista limpia y organizada

def factor2(a):#toma una lista de factores y los combierte en una expresion de multiplicaciones
    st=str(a[0])
    for i in range(len(a)-1):
        st=st+"*"+str(a[i+1])
    return st