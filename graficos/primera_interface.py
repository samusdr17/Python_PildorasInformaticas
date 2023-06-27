from tkinter import *

raiz=Tk()

raiz.title("Ventana de pruebas")

# raiz.resizable(True,False) #redimensionar o no la ventana, parametros(with, heigth)

raiz.iconbitmap("OneDrive.ico")

# raiz.geometry("650x350") #parametros(with, height)

raiz.config(bg="blue") #bg->background


raiz.config(bd=45)

raiz.config(relief="groove")

raiz.config(cursor="hand2")





miFrame=Frame()

miFrame.pack()

# miFrame.pack(fill="y", expand="True")

# miFrame.pack(side="bottom", anchor="s")

miFrame.config(bg="red")

miFrame.config(width="650", height="350")

miFrame.config(bd=35)

miFrame.config(relief="sunken")

miFrame.config(cursor="pirate")

miFrame.config(relief="groove")

raiz.mainloop()