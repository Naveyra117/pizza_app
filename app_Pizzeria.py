import tkinter as tk

def mostrar_seleccion():
    tamaño = var_tamaño.get()
    extras = []
    if extra_queso.get():
        extras.append("Queso extra")
    if extra_pepperoni.get():
        extras.append("Pepperoni")
    if extra_champiñones.get():
        extras.append("Champiñones")
    texto = f"Tamaño: {tamaño}\nExtras: {', ' .join(extras) if extras else 'Ninguno'}"
    lb1_resultado.config(text=texto)
# Ventana principal
ventana = tk.Tk()
ventana.title("Pedido de Pizza")
ventana.geometry("300x300")
# Radiobuttons (solo una opción entre varias)
tk.Label(ventana, text="Elige el tamaño: ").pack(anchor="w")
var_tamaño = tk.StringVar(value="Pequeña") # valor selec por defecto
tk.Radiobutton(ventana, text="Pequeña", variable=var_tamaño, value="Pequeña").pack(anchor="w")
tk.Radiobutton(ventana, text="Mediana", variable=var_tamaño, value="Mediana").pack(anchor="w")
tk.Radiobutton(ventana, text="Grande", variable=var_tamaño, value="Grande").pack(anchor="w")
# Checkbuttons (selecciona múltiples opciones)
tk.Label(ventana, text="\nElige ingredientes extra:").pack(anchor="w")
extra_queso = tk.BooleanVar()
extra_pepperoni = tk.BooleanVar()
extra_champiñones = tk.BooleanVar()
tk.Checkbutton(ventana, text="Queso extra", variable=extra_queso).pack(anchor="w")
tk.Checkbutton(ventana, text="Pepperoni", variable=extra_pepperoni).pack(anchor="w")
tk.Checkbutton(ventana, text="Champiñones", variable=extra_champiñones).pack(anchor="w")
# Botón para mostrar selección
tk.Button(ventana, text="Confirmar pedido", command=mostrar_seleccion).pack(pady=10)
# Etiqueta para mostar el resultado
lb1_resultado = tk.Label(ventana, text="")
lb1_resultado.pack()

ventana.mainloop()




