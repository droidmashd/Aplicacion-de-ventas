from tkinter import *
import basededatos2
def deselecionar():
    check.deselect()
def deselecionar2():
    check2.deselect()
root = Tk()
bolea1 = BooleanVar()
bolea2 = BooleanVar()
root.title("Manejo de ventas")
informacion = Label(root, text="Ingresa el monto")
informacion.pack()
CampoDeTexto =  Entry(root )
CampoDeTexto.pack()
root.geometry("250x400")
check = Checkbutton(root, text="Efectivo", command=deselecionar2, variable=bolea1)
check.pack()

check2 = Checkbutton(root, text="Targeta", command=deselecionar, variable=bolea2)

check2.pack()
def aparecer():
    cantidad = CampoDeTexto.get()
    if (bolea1.get()):
        efectivo = "Efectivo"
    else:
        efectivo = "Targeta"
    
    
    Label(root, text="Buscar transaccion").pack()
    buscar = Entry(root)
    buscar.pack()
    Todo = Button(root, text="Buscar todo", cursor="hand2")
    Todo.pack()
    buscar = Button(root, text="Buscar", cursor="hand2")
    buscar.pack()
    
boton = Button(root, text="Enviar", command=aparecer, cursor="hand2")
boton.pack()



root.mainloop()