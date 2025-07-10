import os
import tkinter as tk
from tkinter import messagebox

# Lista de rutas de los programas que quieres abrir
apps = [
    r"C:\Users\CRISTIAN\AppData\Roaming\.minecraft\TLauncher.exe",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe"
    
]

# Función que se ejecuta al presionar el botón
def abrir_programas():
    for app in apps:
        try:
            os.startfile(app)
        except Exception as e:
            messagebox.showerror("Error", f"Rodes no pudo ejecutar las apps:\n{app}\n\n{e}")

# Crear la ventana
ventana = tk.Tk()
ventana.title("Rodes asistent")
ventana.geometry("300x150")

# Texto
label = tk.Label(ventana, text="Presiona el botón para que Rodes las ejecute", pady=10)
label.pack()

# Botón
boton = tk.Button(ventana, text="Abrir Apps", command=abrir_programas, bg="green", fg="white", height=2, width=15)
boton.place(relx=0.5, rely=0.5, anchor="center")

# Iniciar la app
ventana.mainloop()
