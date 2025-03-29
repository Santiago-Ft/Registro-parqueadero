import tkinter as Ventana

class Formulario:
    def __init__(self):
        self.Registro=[]
        self.dato={}
        self.ventana=""
        self.entrycolor=""
        self.entrymarca=""
        self.entryplaca=""
        self.entryusuario=""
        pass
    def Iniciar(self):
        self.ventana=Ventana.Tk()
        self.labelplaca=Ventana.Label(self.ventana,text="Digite la placa del carro").pack()
        self.entryplaca=Ventana.Entry(self.ventana)
        self.entryplaca.pack(pady=10)
        self.labelcolor=Ventana.Label(self.ventana,text="Digite el color del carro").pack()
        self.entrycolor=Ventana.Entry(self.ventana)
        self.entrycolor.pack(pady=10)
        self.labelmarca=Ventana.Label(self.ventana,text="Digite la marca del carro").pack()
        self.entrymarca=Ventana.Entry(self.ventana)
        self.entrymarca.pack(pady=10)
        self.labelusuario=Ventana.Label(self.ventana,text="Digite el tipo del usuario").pack()
        self.entryusuario=Ventana.Entry(self.ventana)
        self.entryusuario.pack(pady=10)
        self.botonenviar=Ventana.Button(self.ventana,text="Guardar",command=self.enviar).pack(pady=10)
        self.botonlimpiar=Ventana.Button(self.ventana,text="Limpiar",command=self.limpiar).pack(pady=10)
        self.botonver=Ventana.Button(self.ventana,text="Ver datos",command=self.datos).pack(pady=10)
        self.ventana.geometry("400x400")
        self.ventana.title("Registro parqueadero")
        self.ventana.resizable(False,False)
        self.ventana.mainloop()
    def enviar(self):
        if self.verificar():
            mensaje=Ventana.Label(self.ventana,text="Faltan campos por rellenar...").pack()
            print("Faltan campos por rellenar...")
        else:
            self.dato["Placa:"]=self.entryplaca.get()
            self.dato["Color:"]=self.entrycolor.get()
            self.dato["Marca:"]=self.entrymarca.get()
            self.dato["Usuario:"]=self.entryusuario.get()
            self.entryplaca.delete(0,'end')
            self.entrycolor.delete(0,'end')
            self.entrymarca.delete(0,'end')
            self.entryusuario.delete(0,'end')
            print("Guardado exitoso")
        pass
    def limpiar(self):
        self.entryplaca.delete(0,'end')
        self.entrycolor.delete(0,'end')
        self.entrymarca.delete(0,'end')
        self.entryusuario.delete(0,'end')
        print("Campos eliminados")
        pass
    def datos(self):
        self.Registro.append(self.dato)
        self.labelRegistro=Ventana.Label(self.ventana,text=self.Registro).pack()
        print(self.Registro)
        pass
    def verificar(self):
        cont1=self.entryplaca.get().strip()
        cont2=self.entrycolor.get().strip()
        cont3=self.entrymarca.get().strip()
        cont4=self.entryusuario.get().strip()
        if cont1=="" and cont2=="" and cont3=="" and cont4=="":
            return True
        else:
            return False

objFormulario=Formulario().Iniciar()
