import MCM_y_MCD as md
import factores

def esPrimo(n):
    return factores.pfactor(n)==n#un numero primo es el que su primer factor diferente de 1 es el mismo

def primo(n,c=1):#busca en n-avo numero primo
    i=0
    k=2
    a=2
    while i<=n:
        if esPrimo(k):
            i=i+1#añade 1 a la cuenta de primos
            a=k#fija a al primo encontrado
        k=2*c+1
        c=c+1
    return a

def primo1(n,c=1):#hace una lista ordenada de primos hasta el n-avo numero primo
    a=[]
    i=0
    while(len(a)<=n):
        a.append(primo(i,c))
        i=i+1
    if c!=1:
        a.remove(2)
    return a


def psum(n):#busca la primera expresion de un numero como suma de primos
    st=""
    i=0
    while i<n:
        if esPrimo(n-primo(i)):#cuando el n-factor(i) es primo, es porque es el otro primo tal que sumandose a primo de i da n
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
        if esPrimo(n-primo(i)):#comprueba que si n-primo(i) es primo, entonces ese forma parte de la combinacion donde n=primo(i)+(n-primo(i))
            st.append(str(primo(i))+"+"+str(n-primo(i)))#añade a la lista de sumas de primos a los dos numeros hallados
        i=i+1
    return st

def suma_de_primos(n,complete=False):#actua de intermediario entre la ventana que llama a la funcion y las dos funciones para expresiones de sumas de primos
    if complete==True and n<6000:
        return csum(n)
    elif n<100000000000:
        return psum(n)
    
def divsP(n):#halla los divisores primos de un numero
    divp=[]
    for i in range(n):
        if esPrimo(i) and n%i==0:
            divp.append(i)
    return divp

def fact(n):#factorial de un numero n
	if n>1:
		return n*fact(n-1)
	else:
		return 1

def can(n,p,l=1):#aparicion de un p primo con un exponente en n factorial
    if pow(p,l)<=n:
        return int(n/pow(p,l))+can(n,p,l+1)
    else:
        return 0
    
def sigma(n):#la suma de los divisores de un numero
    a=divsP(n)
    s=0
    for i in range(len(a)):
        s=s+a[i]
    return s+n
def tau(n):#cuenta la cantidad de divisores de un numero
    return len(divsP(n))

def fi(n):#cuenta los numeros menores a n con los que tenga mcd=1
    a=0
    for i in range(1,n):
        if md.mcd(i,n)==1:
            a+=1
    return a