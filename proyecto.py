from tkinter import *
import basededatos2  #Importamos un modulo que maneja la base de datos
def deselecionar(): 
    check.deselect() #Estas funciones sirven para no poder seleccionar dos checks 
def deselecionar2():
    check2.deselect()
root = Tk()
d = 1
bolea1 = BooleanVar() #Variables para almacenar valores boleanos de tkinter
bolea2 = BooleanVar()
root.title("Manejo de ventas")
informacion = Label(root, text="Ingresa el monto") #Un label
informacion.pack()
CampoDeTexto =  Entry(root)
CampoDeTexto.pack()
root.geometry("250x600")
check = Checkbutton(root, text="Efectivo", command=deselecionar2, variable=bolea1) #Los check para elegir entre efectivo o credito
check.pack()

check2 = Checkbutton(root, text="Targeta", command=deselecionar, variable=bolea2)

check2.pack()
def aparecer():
    global d
    d += 1
    Informacion = int(CampoDeTexto.get()) 
    if(bolea1.get()):
        Metodo = "Efectivo"
    else:
        Metodo = "Targeta"

    basededatos2.añadirdatos(cantidad= Informacion, metodo = Metodo) #Usa una funcion del modulo exportado para añadir datos
    if (d == 2):
        Label(root, text="Buscar transaccion").pack()
        busca = Entry(root)
        busca.pack()
        def todo(): #busca datos, y despues eliminar todo el textarea y lo actualiza
            texto = basededatos2.buscartodo()
            text_area.delete(1.0, END)
            text_area.insert(1.0, texto)
        Todo = Button(root, text="Buscar todo", cursor="hand2", command=todo, background="#002EFF", foreground="#ffffff")
        Todo.pack()
        def buscarr():
            id = int(busca.get())
            resultado =  basededatos2.buscartransacion(id)
            text_area.delete(1.0, END)
            text_area.insert(1.0, resultado)

        buscar = Button(root, text="Buscar", cursor="hand2", command=buscarr, background="#002EFF", foreground="#ffffff")
        buscar.pack()
        text_area = Text(root, width=20, height=20)
        
        text_area.pack()
        
        eliminarEntry = Entry(root)
        eliminarEntry.pack()
       
        def eliminar():
            id = int(eliminarEntry.get())
            basededatos2.eliminar(id)
        eliminar = Button(root, text="Eliminar", command=eliminar, background="#F50743", bd=10)
        eliminar.pack()
        
    
boton = Button(root, text="Enviar", command=aparecer, cursor="hand2", background="#002EFF", foreground="#ffffff")
boton.pack()



root.mainloop()

