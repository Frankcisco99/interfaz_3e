import tkinter
from tkinter import ttk

ventana = tkinter.Tk()
ventana.title("Codigos de error")

#titulo 
titulo = ttk.Label(ventana,text="Ingresa el codigo", font="Calibri 24 bold")
titulo.pack(pady= 10, padx=10)

entrada_texto = ttk.Entry(ventana)
entrada_texto.pack(pady=10,padx=10)

btn_buscar = ttk.Button(ventana, text="Buscar codigo")
btn_buscar.pack(pady=10, padx=10)

desc_error = ttk.Label(ventana, text="")
desc_error.pack(pady=10)
ventana.mainloop()
