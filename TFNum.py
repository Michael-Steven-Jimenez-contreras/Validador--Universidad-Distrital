import numpy as np
import funciones as fun
hexa={
      'A':"10",
      'B':"11",
      'C':"12",
      'D':"13",
      'E':"14",
      'F':"15",
      'G':"16",
      'H':"17",
      'I':"18",
      'J':"19",
      'K':"20",
      'a':"10",
      'b':"11",
      'c':"12",
      'd':"13",
      'e':"14",
      'f':"15",
      'g':"16",
      'h':"17",
      'i':"18",
      'j':"19",
      'k':"20"
      }
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
        if a=='A' or a=='B' or a=='C' or a=='D' or a=='E' or a=='F' or a=='G' or a=='H' or a=='I' or a=='J' or a=='K' or a=='a' or a=='b' or a=='c' or a=='e' or a=='e' or a=='f' or a=='g' or a=='h' or a=='i' or a=='j' or a=='k':
            a=hexa.get(a)
        arr[i]=int(a)
    return arr

def n2d(x,base):
    if(fun.containt(x,'.')==False):
        x=x+".0"
    val=0
    ent=fun.arrlen(fun.obtent(x),False)-1
    i=ent
    arr=np.array(range(fun.arrlen(x,True)))
    arr=to_vec(x,fun.arrlen(x,True))
    while ent>-fun.arrlen(fun.obdec(x),False)-1:
        val=val+arr[i-ent]*pow(base,ent)
        ent=ent-1
    return val
#print("Introdusca un numero(valor del simbolo, A=10 en hexadecimal) con espacios entre cada simbolo, excepto entre la parte decimal y entrera, debe colocar un punto sin espacios")
#x=input(">>")
#print("Digite la base del numero")
#base=int(input(">>"))
#print(n2d(x,base))