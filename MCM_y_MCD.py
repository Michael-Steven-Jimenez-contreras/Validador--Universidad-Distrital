import funciones as fun


def fmcd(x:str):
    arr=fun.to_vec(x,fun.arrlen(x,True))
    vmcd=arr[0]
    i=1
    while(i<fun.arrlen(x,True)):
        vmcd=fun.mcd(vmcd,arr[i])
        i=i+1
    return vmcd

def fmcm(x:str):
    arr=fun.to_vec(x,fun.arrlen(x,True))
    vmcm=arr[0]
    i=1
    while(i<fun.arrlen(x,True)):
        vmcm=fun.mcm(vmcm,arr[i])
        i=i+1
    return vmcm
