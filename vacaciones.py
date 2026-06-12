# ./RegistroLaboral/vacaciones.py

import tkinter as tk
from tkinter import messagebox
from utils_fechas import fecha_larga
from utils import fecha_pantalla_a_db

import database

def abrir_vacaciones(anio=None):

    ventana = tk.Toplevel()

    ventana.title(
        "Vacaciones"
    )

    tk.Label(
        ventana,
        text=f"Vacaciones",
        font=("Arial", 14, "bold")
    ).pack(
        pady=10
    )

    tk.Label(
        ventana,
        text="Fecha inicio (DD-MM-AAAA)"
    ).pack()

    entry_inicio = tk.Entry(
        ventana
    )

    entry_inicio.pack()

    tk.Label(
        ventana,
        text="Fecha fin (DD-MM-AAAA)"
    ).pack()

    entry_fin = tk.Entry(
        ventana
    )

    entry_fin.pack()

    tk.Label(
        ventana,
        text="Observaciones"
    ).pack()

    entry_obs = tk.Entry(
        ventana,
        width=50
    )

    entry_obs.pack()

    def guardar():

        fecha_inicio = fecha_pantalla_a_db(
            entry_inicio.get()
        )

        fecha_fin = fecha_pantalla_a_db(
            entry_fin.get()
        )

        if (
            fecha_inicio is None
            or
            fecha_fin is None
        ):

            messagebox.showerror(
                "Error",
                "Formato inválido. Use DD-MM-AAAA"
            )

            return

        observaciones = (
            entry_obs.get()
        )

        database.guardar_vacaciones(
            fecha_inicio,
            fecha_fin,
            observaciones
        )

        messagebox.showinfo(
            "Vacaciones",
            "Vacaciones registradas."
        )

        ventana.destroy()

    tk.Button(
        ventana,
        text="Guardar vacaciones",
        command=guardar
    ).pack(
        pady=10
    )

    tk.Label(
        ventana,
        text="Historial de vacaciones"
    ).pack(
        pady=(20, 5)
    )

    texto_vacaciones = tk.Text(
        ventana,
        width=70,
        height=15
    )

    texto_vacaciones.pack(
        padx=10,
        pady=5
    )

    vacaciones = (
        database.obtener_vacaciones()
    )

    for (
        _id,
        fecha_inicio,
        fecha_fin,
        observaciones
    ) in vacaciones:

        fecha_inicio_texto = (
            fecha_larga(
                fecha_inicio
            )
        )

        fecha_fin_texto = (
            fecha_larga(
                fecha_fin
            )
        )

        texto_vacaciones.insert(
            "end",
            f"Estas vacaciones son desde el día "
            f"{fecha_inicio_texto}\n"
            f"hasta el día \n"
            f"{fecha_fin_texto}\n\n"
            f"{observaciones}\n\n"
            f"---------------------------\n\n"
        )

    texto_vacaciones.config(
        state="disabled"
    )
