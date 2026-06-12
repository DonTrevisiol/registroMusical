# ./RegistroLaboral/cierre_anual.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import database
def cerrar_anio(anio):
    ventana = tk.Toplevel()
    ventana.title(
        f"Cierre del año {anio}"
    )

    tk.Label(
        ventana,
        text=f"Cierre del año {anio}",
        font=("Arial", 16, "bold")
    ).pack(pady=10)

    tk.Label(
        ventana,
        text="Observaciones generales del año"
    ).pack()

    texto_observaciones = tk.Text(
        ventana,
        width=70,
        height=10
    )

    texto_observaciones.pack(
        padx=10,
        pady=5
    )

    tk.Label(
        ventana,
        text=f"Objetivos para {int(anio)+1}"
    ).pack()

    texto_objetivos = tk.Text(
        ventana,
        width=70,
        height=10
    )

    texto_objetivos.pack(
        padx=10,
        pady=5
    )

    def guardar():

        observaciones = (
            texto_observaciones.get(
                "1.0",
                "end"
            ).strip()
        )

        objetivos = (
            texto_objetivos.get(
                "1.0",
                "end"
            ).strip()
        )

        fecha_cierre = (
            datetime.now().strftime(
                "%Y-%m-%d"
            )
        )

        database.guardar_cierre_anual(
            anio,
            observaciones,
            objetivos,
            fecha_cierre
        )

        messagebox.showinfo(
            "Año cerrado",
            f"El año {anio} fue guardado correctamente."
        )

        ventana.destroy()

    tk.Button(
        ventana,
        text="Guardar cierre anual",
        command=guardar
    ).pack(
        pady=10
    )
