def clean_l(a:list):#organiza la lista poniendo el 1 al principio
    n=[1]
    for i in range(len(a)):
        if a[i]!=1:
            n.append(a[i])
    return n

def pfactor(n):#halla el primer factor primo de un numero n 
    f=2
    while(int(n/f)!=(n/f)) and f<=int(pow(n,0.5)):#solo comprueba los numeros primos hasta la raiz de n
        f=f+1
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

def primo(n):#busca en n-avo numero primo
    i=0
    k=2
    a=1
    while i<=n:
        if pfactor(k)==k:#un numero primo es el que su primer factor diferente de 1 es el mismo
            i=i+1#añade 1 a la cuenta de primos
            a=k#fija a al primo encontrado
        k=k+1
    return a

def primo1(n):#hace una lista ordenada de primos hasta el n-avo numero primo
    a=[]
    i=0
    while(len(a)<=n):
        a.append(primo(i))
        i=i+1
    return a


def psum(n):#busca la primera expresion de un numero como suma de primos
    st=""
    i=0
    while i<n:
        if((n-primo(i))==pfactor(n-primo(i))):#cuando el n-factor(i) es igual a su pfactor, entonces n-factor(i) es primo
            st=str(primo(i))+"+"+str(n-primo(i))
            return st
        i=i+1
    return st


def csum(n):#busca todas las expresiones de un numero como suma de numeros primos
    st=[]
    i=0
    while i<n and primo(i)<n:
        if primo(i)>n or primo(i)>(n-primo(i)):#se asegura que el i-avo primo sea mayor al (n-primo(i))-avo primo , lo cual indica que a partir de ese punto se va a repetir las expresiones
                return st
        if((n-primo(i))==pfactor(n-primo(i))):#comprueba que si n-primo(i) es primo, entonces ese forma parte de la combinacion donde n=primo(i)+(n-primo(i))
            st.append(str(primo(i))+"+"+str(n-primo(i)))
        i=i+1
    return st

def suma_de_primos(n,complete=False):#actua de intermediario entre la ventana que llama a la funcion y las dos funciones para expresiones de sumas de primos
    if complete==False and n<10000:
        return psum(n)
    else:
        return csum(n)