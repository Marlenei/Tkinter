import tkinter as tk
import time
from tkinter import *
from tkcalendar import Calendar



ventana = tk.Tk()
ventana.title('Reloj simple')

ventana.geometry('400x200') 

reloj = tk.Label(ventana, font =('Arial', 20), bg = 'blue', fg = 'white')
def hora():
    tiempo_actual = time.strftime('%H:%M:%S')
    reloj.config(text = tiempo_actual) 
    ventana.after(1000, hora)

reloj.pack(anchor='ne')

hora()

barra_menu = tk.Menu(ventana) 
ventana.config(menu=barra_menu)
#------ MENU 1-----
menu_principal = tk.Menu(barra_menu) 
barra_menu.add_cascade(label = 'Principal', menu=menu_principal)
submenu = tk.Menu(menu_principal) 
menu_principal.add_command(label = 'Ventana secundaria',command=lambda:mostrar_ventana_secundaria(ventana)) 

#----------VENTANA SECUNDARIA
def mostrar_ventana_secundaria(ventana):
    ventana_secundaria = Toplevel(ventana)
    ventana_secundaria.title("Ventana Secundaria")
    ventana_secundaria.geometry("500x600")
    boton_cerrar = tk.Button(ventana_secundaria, text="Cerrar", command=ventana_secundaria.destroy)
    boton_cerrar.pack(pady=20)

#----------MENU 2----------
menu_2do = tk.Menu(barra_menu) 
barra_menu.add_cascade(label = 'Opciones', menu=menu_2do)
submenu = tk.Menu(menu_2do) 
menu_2do.add_command(label = 'Calendario',command=lambda:mostrar_calendario(ventana)) 
menu_2do.add_command(label = 'Opción 2') 

#---------------SALIR 
salida = tk.Menu(barra_menu) 
barra_menu.add_cascade(label = 'Salir', command=ventana.destroy)


#-----------IMAGEN DE BIENVENIDA
foto = tk.PhotoImage(file="imagen2.png")
fondo=tk.Label(ventana, image=foto)
fondo.pack()

#----------------CALENDARIO
def mostrar_calendario(ventana):
    ventana = tk.Tk()
    cal=Calendar(ventana)
    cal.pack()

ventana.mainloop()
