from tkinter import *

root=Tk()

miFrame=Frame(root, width=1000, height=800)

miFrame.pack()

miImagen=PhotoImage(file="iconJS.png")

# miLabel = Label(miFrame, text="Hola alumnos de Python")
# miLabel.place(x=100, y=200)
#El bloque de arriba y de abajo es lo mismo abrebiado, abajo algunas propiedades más.
# Label(miFrame, text="Hola alumnos de Python", fg="red", font=("Comic Sans MS", 18)).place(x=100, y=200)

Label(miFrame, image=miImagen).place(x=100, y=200)

root.mainloop()