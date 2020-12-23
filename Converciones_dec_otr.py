import funciones as fun
def d2bc(x,n):
    if n<=1:
        n=10
    if(fun.containt(x,'.')==False):
        x=x+".0"
    n=n+0
    ent=int(float(x))
    dec=float(x)-ent

    val=""

    i=0
    while dec>0 and i<20:
        val=val+" "+str(int(dec*n))
        dec=(dec*n)-int(dec*n)
        i=i+1;
    if i>0:
        val="."+val
    while ent!=0:
        val=str(ent%n)+" "+val
        ent=int(ent/n)
    #print(x,"=",val)
    return val
#d2b()


