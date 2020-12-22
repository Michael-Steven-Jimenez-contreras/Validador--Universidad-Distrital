import funciones as fun


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

def fmcd(x:str):
    arr=fun.to_vec(x,fun.arrlen(x,True))
    vmcd=arr[0]
    i=1
    while(i<fun.arrlen(x,True)):
        vmcd=mcd(vmcd,arr[i])
        i=i+1
    return abs(vmcd)

def fmcm(x:str):
    arr=fun.to_vec(x,fun.arrlen(x,True))
    vmcm=arr[0]
    i=1
    while(i<fun.arrlen(x,True)):
        vmcm=mcm(vmcm,arr[i])
        i=i+1
    return vmcm

