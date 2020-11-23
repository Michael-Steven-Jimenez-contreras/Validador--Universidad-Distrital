from tkinter import *#Label,Button,Toplevel,Entry,Tk,Checkbutton
import Converciones_dec_otr as cvn
import funciones as fun
import TFNum
import MCM_y_MCD as mc
import factores
from functools import partial

        
def ventana(titulo:str,tam:str,h:bool,v:bool):
    vent=Tk()
    vent.title(titulo)
    vent.geometry(tam)
    vent.resizable(width=h , height=v)
    return vent
def subventana(inst,titulo:str,tam:str,h:bool,v:bool):
    vent=Toplevel(inst)
    inst.withdraw()
    vent.title(titulo)
    vent.geometry(tam)
    vent.resizable(width=h , height=v)
    vent.protocol("WM_DELETE_WINDOW", partial(volver, inst,vent))
    return vent
def volver(org,inst):
    org.deiconify()
    inst.destroy()
    
def decbas(inst):
    
    def convertirdb(obj,a,b):
        obj.delete(0,100)
        t=cvn.d2bc(a,int(b))
        lon=fun.arrlen(t,True)
        obj.insert(0,fun.tohex(t,lon))
    

    cd=subventana(inst,"De sistema decimal a otro sistema","500x250",False,False)
    #objetos de la interfaz
    text=Entry(cd,font=("Calibri 12"))
    salida=Entry(cd,font=("Calibri 12"))
    sp=Entry(cd,font=("Calibri 12"),width=5)
    label1=Label(cd,text="Numero inicial:",width=15,height=5)
    label2=Label(cd,text="Numero convertido:",width=15,height=5)
    label3=Label(cd,text="Base:",width=5,height=5)
    backb=Button(cd,text="Volver al menu",width=12,height=2,command=lambda: volver(inst,cd))
    accept=Button(cd,text="aceptar",width=11,height=2,command=lambda: convertirdb(salida,text.get(),sp.get()))
    #ubicacion
    label1.grid(row=0,column=0,padx=1,pady=1)
    label2.grid(row=1,column=0,padx=1,pady=1)
    text.grid(row=0,columnspan=4,column=1,padx=5,pady=5)
    accept.grid(row=3,column=1,padx=1,pady=5)
    label3.grid(row=0,column=5,padx=1,pady=1)
    sp.grid(row=0,column=6,padx=5,pady=0)
    salida.grid(row=1,columnspan=4,column=1,padx=1,pady=1)
    backb.grid(row=3,column=0,padx=0,pady=1)
    cd.mainloop()
    

        
def basdec(inst):
    bd=subventana(inst,"de otro sistema numerico a sistema decimal","560x250",False,False)
    #objetos
    entrada=Entry(bd,font=("Calibri 12"))
    salida=Entry(bd,font=("Calibri 12"))
    base=Entry(bd,font=("Calibri 12"),width=5)
    label1=Label(bd,text="Entrada(ej:3 4.2 1):",width=15,height=5)
    label2=Label(bd,text="Base:",width=5,height=5)
    label3=Label(bd,text="Salida:",width=7,height=5)
    backb=Button(bd,text="Volver al menu",width=11,height=2,command=lambda: volver(inst,bd))
    accept=Button(bd,text="aceptar",width=5,height=2,command=lambda: convertirbd(salida,entrada.get(),base.get()))
    #ubicacion:
    label1.grid(row=0,column=0,padx=1,pady=1)
    entrada.grid(row=0,column=1,columnspan=4,padx=1,pady=1)
    label2.grid(row=0,column=5,padx=1,pady=1)
    base.grid(row=0,column=6,padx=1,pady=1)
    label3.grid(row=1,column=0,padx=1,pady=1)
    salida.grid(row=1,column=1,columnspan=4,padx=1,pady=1)
    backb.grid(row=2,column=0,padx=1,pady=1)
    accept.grid(row=2,column=1,padx=1,pady=1)
    def convertirbd(obj,a,b):
        obj.delete(0,100)
        obj.insert(0,TFNum.n2d(a,int(b)))

def oper(inst):
    op=subventana(inst,"Operaciones en otras bases","500x300",False,False)
    #objetos
    label1=Label(op,text="Primer numero:")
    label2=Label(op,text="Segundo numero:")
    label3=Label(op,text="Base:")
    label4=Label(op,text="Resultado:")
    entrada1=Entry(op,font=("Calibri 12"))
    entrada2=Entry(op,font=("Calibri 12"))
    base=Entry(op,font=("Calibri 12"),width=5)
    salida=Entry(op,font=("Calibri 12"))
    backb=Button(op,text="Volver al menu",width=11,height=2,command=lambda: volver(inst,op))
    
    boton1=Button(op,text="+",width=11,height=2,command=lambda: suma(entrada1.get(),entrada2.get(),base.get(),salida))
    boton2=Button(op,text="-",width=11,height=2,command=lambda: resta(entrada1.get(),entrada2.get(),base.get(),salida))
    boton3=Button(op,text="/",width=11,height=2,command=lambda: division(entrada1.get(),entrada2.get(),base.get(),salida))
    boton4=Button(op,text="*",width=11,height=2,command=lambda: multiplicacion(entrada1.get(),entrada2.get(),base.get(),salida))
    boton5=Button(op,text="%",width=11,height=2,command=lambda: residuo(entrada1.get(),entrada2.get(),base.get(),salida))
    #ubicacion
    label1.grid(row=0,column=0,padx=1,pady=5)
    entrada1.grid(row=0,column=1,columnspan=4,padx=1,pady=5)
    
    label2.grid(row=1,column=0,padx=1,pady=5)
    entrada2.grid(row=1,column=1,columnspan=4,padx=1,pady=5)
    
    label3.grid(row=0,column=5,padx=1,pady=5)
    base.grid(row=0,column=6,padx=1,pady=5)
    
    label4.grid(row=3,column=0,padx=1,pady=5)
    salida.grid(row=3,column=1,columnspan=4,padx=1,pady=5)
    
    boton1.grid(row=4,column=0,padx=1,pady=5)
    boton2.grid(row=4,column=1,padx=1,pady=5)
    boton3.grid(row=4,column=2,padx=1,pady=5)
    boton4.grid(row=4,column=3,padx=1,pady=5)
    boton5.grid(row=5,column=0,padx=1,pady=5)
    
    backb.grid(row=6,column=0,padx=1,pady=5)
    def suma(p,q,base,obj):
        a=float(TFNum.n2d(p,int(base)))+float(TFNum.n2d(q,int(base)))
        obj.delete(0,100)
        insertard(str(cvn.d2bc(str(a),int(base))), obj)
        
    def resta(p,q,base,obj):
        a=float(TFNum.n2d(p,int(base)))-float(TFNum.n2d(q,int(base)))
        obj.delete(0,100)
        insertard(str(cvn.d2bc(str(a),int(base))), obj)
        
    def multiplicacion(p,q,base,obj):
        a=float(TFNum.n2d(p,int(base)))*float(TFNum.n2d(q,int(base)))
        obj.delete(0,100)
        insertard(str(cvn.d2bc(str(a),int(base))), obj)
        
    def division(p,q,base,obj):
        a=float(TFNum.n2d(p,int(base)))/float(TFNum.n2d(q,int(base)))
        obj.delete(0,100)
        insertard(str(cvn.d2bc(str(a),int(base))), obj)
    
    def residuo(p,q,base,obj):
        a=float(TFNum.n2d(p,int(base)))%float(TFNum.n2d(q,int(base)))
        obj.delete(0,100)
        insertard(str(cvn.d2bc(str(a),int(base))), obj)
        
    def insertard(a,obj):
        lon=fun.arrlen(a,True)
        obj.insert(0,fun.tohex(a,lon))
    
def mcmmcd(inst):
    vent=subventana(inst,"Operaciones en otras bases","500x150",False,False)
    #objetos
    entrada=Entry(vent,font=("Calibri 12"))
    salida1=Entry(vent,font=("Calibri 12"))
    salida2=Entry(vent,font=("Calibri 12"))
    aceptar=Button(vent,text="aceptar",width=11,height=2,command=lambda: mcmyd(entrada.get(),salida1,salida2))
    backb=Button(vent,text="Volver al menu",width=11,height=2,command=lambda: volver(inst,vent))
    label1=Label(vent,text="Entrada(ej 5,2,5)")
    label2=Label(vent,text="MCD")
    label3=Label(vent,text="MCM")
    #Ubicacion
    label1.grid(row=0,column=0,padx=0,pady=5)
    entrada.grid(row=0,column=1,columnspan=2,padx=0,pady=5)
    
    label2.grid(row=1,column=0,padx=0,pady=5)
    salida1.grid(row=1,column=1,padx=0,pady=5)
    label3.grid(row=1,column=2,padx=0,pady=5)
    salida2.grid(row=1,column=3,padx=0,pady=5)
    
    backb.grid(row=2,column=0,padx=0,pady=5)
    aceptar.grid(row=2,column=1,padx=0,pady=5)
    
    def mcmyd(p,mcm,mcd):
        mcm.delete(0,100)
        mcd.delete(0,100)
        mcm.insert(0,mc.fmcd(p))
        mcd.insert(0,mc.fmcm(p))

def facto(inst):
    vent=subventana(inst,"Factores","500x200",False,False)
    
    label1=Label(vent,text="Entrada(ej 34)")
    entrada=Entry(vent,font=("Calibri 12"))
    label2=Label(vent,text="Factores")
    salida1=Entry(vent,font=("calibri 12"))
    label3=Label(vent,text="E.suma de primos")
    salida2=Entry(vent,font=("calibri 12"))
    val=BooleanVar()
    completo=Checkbutton(vent,text="Completo?",variable=val)
    aceptar1=Button(vent,text="aceptar",width=11,height=2,command=lambda: fac(entrada,salida1))
    aceptar2=Button(vent,text="aceptar",width=11,height=2,command=lambda: sprm(entrada,salida2,val))
    
    backb=Button(vent,text="Volver al menu",width=11,height=2,command=lambda: volver(inst,vent))
    
    label1.grid(row=0,column=0,padx=0,pady=5)
    entrada.grid(row=0,column=1,columnspan=4,padx=0,pady=5)
    label2.grid(row=1,column=0,padx=0,pady=5)
    salida1.grid(row=1,column=1,columnspan=4,padx=0,pady=5)
    aceptar1.grid(row=1,column=5,padx=5,pady=5)
    
    label3.grid(row=2,column=0,padx=0,pady=5)
    salida2.grid(row=2,column=1,columnspan=4,padx=0,pady=5)
    aceptar2.grid(row=2,column=5,padx=5,pady=5)
    completo.grid(row=2,column=6,padx=0,pady=5)
    
    backb.grid(row=3,column=0,padx=0,pady=5)
    
    def sprm(p,sump,completo):
        sump.delete(0,100)
        sump.insert(0,fun.elim(fun.elim(fun.elim(str(factores.suma_de_primos(int(p.get()),completo.get())),"["),"]"),"'"))
    def fac(p,fact):
        fact.delete(0,100)
        fact.insert(0,factores.factor2(factores.factor(int(p.get()),True)))   

def op_menu():
    vent=ventana("Validador","530x380",False,False)
    #objetos de la interfaz
    #aut=Label(vent,text="Por: Michael Jimenez Contreras 20201020108")
    mater=Label(vent,text="Teoria de numeros G-83")
    seccion1=Label(vent,text="Conversiones y operaciones en otras bases:")
    cdo=Button(vent,text="De sistema decimal a otra base",width=25,height=5,command=lambda: decbas(vent))
    TFN=Button(vent,text="De otra base a sistema decimal",width=25,height=5,command=lambda: basdec(vent))
    opnum=Button(vent,text="Operaciones en otras bases",width=55,height=5,command=lambda: oper(vent))
    
    seccion2=Label(vent,text="Otras operaciones")
    bmcm=Button(vent,text="MCM y MCD de un conjunto",width=25,height=5,command=lambda: mcmmcd(vent))
    factors=Button(vent,text="Factores de un numero",width=25,height=5,command=lambda: facto(vent))
    #ubicacion
    #aut.grid(row=0,column=0,padx=0,pady=5)
    mater.grid(row=1,column=0,padx=0,pady=5)
    seccion1.grid(row=2,column=0,padx=0,pady=5)
    cdo.grid(row=3,column=0,padx=5,pady=5)
    TFN.grid(row=3,column=1,padx=5,pady=5)
    opnum.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
    
    seccion2.grid(row=5,column=0,padx=0,pady=5)
    bmcm.grid(row=6,column=0,padx=5,pady=5)
    factors.grid(row=6,column=1,padx=5,pady=5)
    vent.mainloop()

if __name__=='__main__':
    op_menu()