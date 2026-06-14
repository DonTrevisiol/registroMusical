# ./RegistroLaboral/app.py

import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import views
import database
from vacaciones import abrir_vacaciones
from utils import (
    parsear_tiempo,
    formatear_tiempo_total,
    formatear_tiempo_promedio
    )

# ===============================
# FUNCION DE FECHA (DD-MM-AAAA → AAAA-MM-DD)
# ===============================

def convertir_fecha(fecha_texto):
    try:
        fecha = datetime.strptime(fecha_texto, "%d-%m-%Y")
        return fecha.strftime("%Y-%m-%d")
    except:
        return None

def actualizar_campos_falta():

    if falta_justificada.get():

        entry_canciones.delete(0, tk.END)
        entry_tiempo.delete(0, tk.END)
        entry_dinero.delete(0, tk.END)

        entry_canciones.config(state="disabled")
        entry_tiempo.config(state="disabled")
        entry_dinero.config(state="disabled")

    else:

        entry_canciones.config(state="normal")
        entry_tiempo.config(state="normal")
        entry_dinero.config(state="normal")

# ===============================
# GUARDAR REGISTRO
# ===============================

def guardar():
    try:

        detalles = entry_detalles.get()

        tipo_registro = (
            "justificada"
            if falta_justificada.get()
            else "trabajado"
        )

        if tipo_registro == "justificada":

            canciones = 0
            tiempo_seg = 0
            dinero = 0

        else:

            canciones = int(
                entry_canciones.get()
            )

            tiempo_str = (
                entry_tiempo.get()
            )

            dinero = float(
                entry_dinero.get()
            )

            tiempo_seg = parsear_tiempo(
                tiempo_str
            )

            if tiempo_seg is None:

                messagebox.showerror(
                    "Error",
                    "Formato de tiempo inválido"
                )

                return
        fecha_input = entry_fecha.get()

        # Manejo de fecha
        if fecha_input.strip() == "":
            fecha = datetime.now().strftime("%Y-%m-%d")
        else:
            fecha_convertida = convertir_fecha(fecha_input)
            if fecha_convertida is None:
                messagebox.showerror("Error", "Formato inválido. Usar DD-MM-AAAA")
                return
            fecha = fecha_convertida

        # Guardar en DB
        database.insertar_registro(
            fecha,
            canciones,
            tiempo_seg,
            dinero,
            detalles,
            tipo_registro
            )

        # Cálculos

        if canciones > 0:

            tiempo_promedio = tiempo_seg / canciones
            dinero_promedio = dinero / canciones

            tiempo_promedio_texto = (
                formatear_tiempo_promedio(tiempo_promedio)
                if tiempo_seg > 0
                else "No disponible"
            )

            dinero_promedio_texto = f"${dinero_promedio:.2f}"

        else:

            tiempo_promedio_texto = "No disponible"
            dinero_promedio_texto = "No disponible"

        resultado.set(
            f"Guardado ✔\n"
            f"Fecha: {fecha}\n"
            f"Tiempo promedio: {tiempo_promedio_texto}\n"
            f"Dinero promedio: {dinero_promedio_texto}"
        )

        limpiar()

    except Exception as e:
        messagebox.showerror("Error", str(e))


def limpiar():
    entry_fecha.delete(0, tk.END)
    entry_canciones.delete(0, tk.END)
    entry_tiempo.delete(0, tk.END)
    entry_dinero.delete(0, tk.END)
    entry_detalles.delete(0, tk.END)

    falta_justificada.set(False)

    entry_canciones.config(state="normal")
    entry_tiempo.config(state="normal")
    entry_dinero.config(state="normal")

# ===============================
# INTERFAZ
# ===============================

root = tk.Tk()
icono = tk.PhotoImage(file="icono.png")
root.iconphoto(True, icono)
root.title("Registro Laboral")
root.attributes("-zoomed", True)

logo_original = tk.PhotoImage(
    file="logo.png"
)

logo = logo_original.subsample(4, 4)

root.logo = logo

tk.Label(
    root,
    image=logo
).pack(
    pady=10
)

tk.Label(root, text="Fecha (DD-MM-AAAA)").pack()
entry_fecha = tk.Entry(root)
entry_fecha.pack()

tk.Label(root, text="Canciones").pack()
entry_canciones = tk.Entry(root)
entry_canciones.pack()

tk.Label(root, text="Tiempo total (1h23'45\":67)").pack()
entry_tiempo = tk.Entry(root)
entry_tiempo.pack()

tk.Label(root, text="Dinero total").pack()
entry_dinero = tk.Entry(root)
entry_dinero.pack()

tk.Label(root, text="Detalles").pack()
entry_detalles = tk.Entry(root)
entry_detalles.pack()

falta_justificada = tk.BooleanVar(
    value=False
)

tk.Checkbutton(
    root,
    text="Falta justificada",
    variable=falta_justificada,
    command=actualizar_campos_falta
).pack()


database.crear_tablas()

tk.Button(
    root,
    text="Ver Registro",
    command=views.abrir_ver_registros
    ).pack()

tk.Button(
    root,
    text="Guardar registro",
    command=guardar
    ).pack()

tk.Button(
    root,
    text="Vacaciones",
    command=lambda:
        abrir_vacaciones(None)
    ).pack()

resultado = tk.StringVar()
tk.Label(root, textvariable=resultado).pack()

root.mainloop()
