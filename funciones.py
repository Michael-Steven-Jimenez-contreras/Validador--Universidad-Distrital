import numpy as np
def containt(x,a):
    val=False
    for i in range(len(x)):
        val=(val or x[i]==a)
    return val

def elim(x,a):
    c=""
    for i in range(len(x)):
        if x[i]!=a:
            c=c+x[i]
    return c

def repl(x,a,b):
    c=""
    for i in range(len(x)):
        if x[i]!=a:
            c=c+x[i]
        else:
            c=c+b
    return c

def obtent(x):
    i=0
    a=""
    x=x+" "
    while x[i]!='.' and i<(len(x)-1):
        a=a+x[i]
        i=i+1
    
    return a
def obdec(x):
    i=0
    a=""
    x=x+" "
    while x[i]!='.' and i<len(x)-1:
        i=i+1
    while i<len(x)-1:
        a=a+x[i]
        i=i+1
    return a
def arrlen(x,dat):
    i=0
    n=1
    if dat==False:
        while i<len(x):
            if x[i]==' ':
                n=n+1
            i=i+1
    else:
        while i<len(x):
            if x[i]==' ' or x[i]=='.' or x[i]==',':
                n=n+1
            i=i+1
    return n
dechexa={#se llama hexa pero va hasta 20
    "10":'A',
    "11":'B',
    "12":'C',
    "13":'D',
    "14":'E',
    "15":'F',
    "16":'G',
    "17":'H',
    "18":'I',
    "19":'j',
    "20":'k'
    }
def tohex(x,longit):
    st=""
    k=-1
    a=""
    x=x+" "
    for i in (range(longit-1)):
        k=k+1
        a=""
        while x[k]!=' ' and x[k]!=',':
            a=a+x[k]
            k=k+1
        if a=="10" or a=="11" or a=="12" or a=="13" or a=="14" or a=="15" or a=="16" or a=="17" or a=="18" or a=="19" or a=="20":
            a=dechexa.get(a)
        st=st+a+" "
    return st
def mcd(a,b):
    t=0
    while (a%b)!=0:
        t=(a%b)
        a=b
        b=t
    if t!=0:
        t=t
    else:
        t=b;
    return t
def mcm(a,b):
    return (a*b)/mcd(a,b)

def to_vec(x,longit):
    arr=np.array(range(longit))
    k=-1
    a=""
    x=x+" "
    for i in (range(longit)):
        k=k+1
        a=""
        while x[k]!=' ' and x[k]!='.' and x[k]!=',':
            a=a+x[k]
            k=k+1
        arr[i]=int(a)
    return arr