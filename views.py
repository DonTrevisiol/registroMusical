# ./RegistroLaboral/views.py

import tkinter as tk
import database
from tabla_mes import (mostrar_meses)
from resumen_anual import (mostrar_resumen_anual)
from vacaciones import (abrir_vacaciones)


def abrir_ver_registros():

    ventana = tk.Toplevel()
    ventana.title("Ver registros")

    tk.Label(
        ventana,
        text="Seleccione un año"
    ).pack(pady=10)

    anios = database.obtener_anios()

    for anio in anios:

        frame = tk.Frame(
            ventana
        )

        frame.pack(
            pady=2
        )

        tk.Button(
            frame,
            text=anio,
            width=20,
            command=lambda a=anio:
            mostrar_meses(a)
        ).pack(
            side="left"
        )

        tk.Button(
            frame,
            text="Resumen",
            command=lambda a=anio:
            mostrar_resumen_anual(a)
        ).pack(
            side="left",
            padx=5
        )
