import funciones as fun


def mcd(a,b,v=[]):
    t=0
    while (a%b)!=0:
        t=(a%b)
        v.append([a,int(a/b),b,t])
        a=b
        b=t
    if t!=0:
        t=t
    else:
        t=b;
    return t

def fmcd(x:str):
    v=[]
    arr=fun.to_vec(x,fun.arrlen(x,True))
    vmcd=arr[0]
    i=1
    while(i<fun.arrlen(x,True)):
        vmcd=mcd(vmcd,arr[i],v)
        i=i+1
    return (abs(vmcd),v)


def mcm(a,b):
    return (a*b)/mcd(a,b)



def fmcm(x:str):
    arr=fun.to_vec(x,fun.arrlen(x,True))
    vmcm=arr[0]
    i=1
    while(i<fun.arrlen(x,True)):
        vmcm=mcm(vmcm,arr[i])
        i=i+1
    return vmcm




##funciones adicionales para generar el TFA

class Dst:
    n=1
    poli=[]
    def __init__(self,n,poli):
        self.n=n
        self.poli=poli
    def __str__(self):
        return str(self.n)+"*"+str(self.poli)
    def __repr__(self):
        return str(self.n)+"*"+str(self.poli)
    def resolver(self):
        v=[]
        try:
            for i in range(len(self.poli)):
                v.append(Dst(self.n*self.poli[i].n,self.poli[i].poli))
        except:
            for i in range(len(self.poli)):
                v.append(Dst(self.n,[self.poli[i]]))
        return v
    def __eq__(self,other):
        return self.poli==other.poli
    def __lt__(self,other):
        return self.poli<other.poli
    def __add__(self,other):
        return Dst(self.n+other.n,self.poli)
    def repl(self,v):
        self.poli=v
def Ordval(x):
    v=[]
    for i in range(len(x)):
        v.append([Dst(1,[x[i][3]]),Dst(1,[x[i][0]]),Dst(-x[i][1],[x[i][2]])])
    return v
def resolver(res):
    temp=[]
    for i in range(len(res)):
        temp+=res[i].resolver()
    return temp
def ordenar(v):
    for i in range(len(v)):
        for j in range(i,len(v)):
            if(v[j]<v[i]):
                temp=v[j]
                v[j]=v[i]
                v[i]=temp
    return v

def toeq(v):
    cad=str(v[0])+"="
    for i in range(1,len(v)-1):
        cad+=str(v[i])+"+"
    return cad+str(v[len(v)-1])

def TFA(v):
#####paso 1, escoger el ultimo elemento de la lista####
#v=Ordval(fmcd("232,93")[1])
    cad=""
    v=Ordval(v)
    res=v[len(v)-1]
    v.remove(res)
    
    for i in range(len(v)):
        cad+=toeq(v[i])+"\n\n"
    
    #####Remplazar datos####
    cad+=toeq(res)+"\n\n\n"
    
    
    for i in range(len(v)):
        k=1
        while(k<len(res)):
            if(res[k]==v[len(v)-1-i][0]):
                res[k].repl([v[len(v)-1-i][1],v[len(v)-1-i][2]])    
                cad+=toeq(res)+"\n\n"
                res=resolver(res)
            k+=1
      
        cad+=toeq(res)+"\n\n"
    ######agrupar#######
    res=ordenar(res)
    
    pivote=Dst(0,[0])
    k=-1
    f=[]
    for i in range(len(res)):
        if pivote!=res[i]:
            pivote=res[i]
            k+=1
            f.append(res[i])
        else:
            f[k]+=res[i]
    cad+=toeq(f)
    return f,cad