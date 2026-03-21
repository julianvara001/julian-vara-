import tkinter as tk
from tkinter import messagebox

# datos
sabores_disponibles = ["Chocolate", "Vainilla", "Frutilla", "Dulce de leche", "Limon", "Pistacho", "Oreo"]
precio_1 = 700
precio_2 = 1200
precio_3 = 1600

# para mostrar las bochas

def actualizar_pantalla():

    cant = int(var_cantidad.get())

    frame_bocha2.pack_forget()
    frame_bocha3.pack_forget()
    
    if cant == 2:
        frame_bocha2.pack(side="left", padx=10)
    elif cant == 3:
        frame_bocha2.pack(side="left", padx=10)
        frame_bocha3.pack(side="left", padx=10)

def realizar_pedido():
    cant = int(var_cantidad.get())
    total = 0
    resumen_sabores = ""

    # sumamos los sabores dependiendo las bochas elegidas
    if cant == 1:
        total = precio_1
        resumen_sabores = "\n- " + var_sabor1.get()
    elif cant == 2:
        total = precio_2
        resumen_sabores = "\n- " + var_sabor1.get() + "\n- " + var_sabor2.get()
    elif cant == 3:
        total = precio_3
        resumen_sabores = "\n- " + var_sabor1.get() + "\n- " + var_sabor2.get() + "\n- " + var_sabor3.get()

    # mostramos el ticket
    messagebox.showinfo("Ticket", "Pedido:" + resumen_sabores + "\n\nTotal: $" + str(total))

# interfaz
ventana = tk.Tk()
ventana.title("Heladería Dulce Frío (Básico)")
ventana.geometry("600x500")
ventana.config(bg="#E0F2F7")

# titulo
tk.Label(ventana, text="🍦 HELADOS DULCE FRÍO 🍦", font=("Arial", 18, "bold"), bg="#E0F2F7").pack(pady=15)

# pregunta cuantas bochas quiere
tk.Label(ventana, text="¿Cuántas bochas?", font=("Arial", 11), bg="#E0F2F7").pack()
var_cantidad = tk.StringVar(value="1")

# se elijen las bochas
tk.Radiobutton(ventana, text="1 Bocha", variable=var_cantidad, value="1", command=actualizar_pantalla, bg="#E0F2F7").pack()
tk.Radiobutton(ventana, text="2 Bochas", variable=var_cantidad, value="2", command=actualizar_pantalla, bg="#E0F2F7").pack()
tk.Radiobutton(ventana, text="3 Bochas", variable=var_cantidad, value="3", command=actualizar_pantalla, bg="#E0F2F7").pack()

# contenedor de los sabores
frame_contenedor_sabores = tk.Frame(ventana, bg="#E0F2F7")
frame_contenedor_sabores.pack(pady=20)

# guarda el sabor de cada bocha
var_sabor1 = tk.StringVar(value=sabores_disponibles[0])
var_sabor2 = tk.StringVar(value=sabores_disponibles[0])
var_sabor3 = tk.StringVar(value=sabores_disponibles[0])

# bocha 1
frame_bocha1 = tk.LabelFrame(frame_contenedor_sabores, text="Bocha 1", bg="#E0F2F7")
frame_bocha1.pack(side="left", padx=10)
for s in sabores_disponibles:
    tk.Radiobutton(frame_bocha1, text=s, variable=var_sabor1, value=s, bg="#E0F2F7").pack(anchor="w")

# bocha 2
frame_bocha2 = tk.LabelFrame(frame_contenedor_sabores, text="Bocha 2", bg="#E0F2F7")
for s in sabores_disponibles:
    tk.Radiobutton(frame_bocha2, text=s, variable=var_sabor2, value=s, bg="#E0F2F7").pack(anchor="w")

# bocha 3
frame_bocha3 = tk.LabelFrame(frame_contenedor_sabores, text="Bocha 3", bg="#E0F2F7")
for s in sabores_disponibles:
    tk.Radiobutton(frame_bocha3, text=s, variable=var_sabor3, value=s, bg="#E0F2F7").pack(anchor="w")

# boton para confirmar
btn_confirmar = tk.Button(ventana, text="CONFIRMAR PEDIDO", command=realizar_pedido, bg="#1E90FF", fg="white", font=("Arial", 12, "bold"))
btn_confirmar.pack(side="bottom", pady=30)

actualizar_pantalla()

ventana.mainloop()