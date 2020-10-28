from tkinter import Label,Button,Toplevel,Entry,Tk
import Converciones_dec_otr as cvn
import funciones as fun
import TFNum
from functools import partial


def volver(org,inst):
    org.deiconify()
    inst.destroy()
    
def decbas(inst):
    cd=Toplevel(inst)
    inst.withdraw()
    cd.title("De sistema decimal a otro sistema")
    cd.geometry("500x250")
    cd.resizable(width=False , height=False)
    cd.protocol("WM_DELETE_WINDOW", partial(volver, inst,cd))
    #objetos de la interfaz
    text=Entry(cd,font=("Calibri 12"))
    salida=Entry(cd,font=("Calibri 12"))
    sp=Entry(cd,font=("Calibri 12"),width=5)
    backb=Button(cd,text="Volver al menu",width=12,height=2,command=lambda: volver(inst,cd))
    accept=Button(cd,text="aceptar",width=11,height=2,command=lambda: convertirdb(salida,text.get(),sp.get()))
    label1=Label(cd,text="Numero inicial:",width=15,height=5)
    label2=Label(cd,text="Numero convertido:",width=15,height=5)
    label3=Label(cd,text="Base:",width=5,height=5)
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
def convertirdb(obj,a,b):
    obj.delete(0,100)
    t=cvn.d2bc(a,int(b))
    lon=fun.arrlen(t,True)
    obj.insert(0,fun.tohex(t,lon))
    
    
def basdec(inst):
    bd=Toplevel(inst)
    inst.withdraw()
    bd.title("de otro sistema numerico a sistema decimal")
    bd.geometry("560x250")
    bd.resizable(width=False , height=False)
    bd.protocol("WM_DELETE_WINDOW", partial(volver, inst,bd))
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
    op=Toplevel(inst)
    inst.withdraw()
    op.title("Operaciones en otras bases")
    op.geometry("500x200")
    op.resizable(width=False , height=False)
    op.protocol("WM_DELETE_WINDOW", partial(volver, inst,op))
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
    
    backb.grid(row=5,column=0,padx=1,pady=5)
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
def insertard(a,obj):
    lon=fun.arrlen(a,True)
    obj.insert(0,fun.tohex(a,lon))
def op_menu():
    vent=Tk()
    vent.title("Validador")
    vent.geometry("530x300")
    vent.resizable(width=False , height=False)
    #objetos de la interfaz
    aut=Label(vent,text="Por: Michael Jimenez Contreras 20201020108")
    mater=Label(vent,text="Teoria de numeros G-83")
    seccion1=Label(vent,text="Conversiones y operaciones en otras bases:")
    cdo=Button(vent,text="De sistema decimal a otra base",width=25,height=5,command=lambda: decbas(vent))
    TFN=Button(vent,text="De otra base a sistema decimal",width=25,height=5,command=lambda: basdec(vent))
    opnum=Button(vent,text="Operaciones en otras bases",width=55,height=5,command=lambda: oper(vent))
    #ubicacion
    aut.grid(row=0,column=0,padx=0,pady=5)
    mater.grid(row=1,column=0,padx=0,pady=5)
    seccion1.grid(row=2,column=0,padx=0,pady=5)
    cdo.grid(row=3,column=0,padx=5,pady=5)
    TFN.grid(row=3,column=1,padx=5,pady=5)
    opnum.grid(row=4,column=0,columnspan=2,padx=5,pady=5)
    vent.mainloop()
    
if __name__=='__main__':    
    op_menu()