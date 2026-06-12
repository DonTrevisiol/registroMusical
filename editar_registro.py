# ./RegistroLaboral/editar_registro.py

import tkinter as tk
from tkinter import messagebox

from datetime import datetime

import database

from tabla_utils import (
    obtener_datos_fila
)

from utils import (
    parsear_tiempo,
    formatear_tiempo_total,
    formatear_tiempo_promedio,
    fecha_db_a_pantalla,
    fecha_pantalla_a_db
)

from utils_fechas import (
    fecha_con_dia,
    numero_lunes_del_anio
)

def editar_registro_seleccionado(tabla):

    seleccion = tabla.selection()

    if not seleccion:
        return

    registro_id = seleccion[0]

    if (
        str(registro_id).startswith("virtual_")
    or
        str(registro_id).startswith("vacaciones_")
    ):

        messagebox.showinfo(
            "Registro protegido",
            "Las faltas virtuales y las cacaciones no pueden editarse ni eliminarse"
            )

    registro = database.obtener_registro_por_id(
        registro_id
    )

    if not registro:
        return

    (
        _id,
        fecha,
        canciones,
        tiempo_seg,
        dinero,
        detalles,
        tipo_registro
    ) = registro

    ventana = tk.Toplevel()
    ventana.title("Editar registro")

    tk.Label(
        ventana,
        text="Fecha (DD-MM-AAAA)"
    ).pack()

    entry_fecha = tk.Entry(ventana)
    entry_fecha.pack()

    entry_fecha.insert(
        0,
        fecha_db_a_pantalla(fecha)
    )

    tk.Label(
        ventana,
        text="Canciones"
    ).pack()

    entry_canciones = tk.Entry(ventana)
    entry_canciones.pack()

    entry_canciones.insert(
        0,
        str(canciones)
    )

    tk.Label(
        ventana,
        text="Tiempo total"
    ).pack()

    entry_tiempo = tk.Entry(ventana)
    entry_tiempo.pack()

    entry_tiempo.insert(
        0,
        formatear_tiempo_total(
            tiempo_seg
        )
    )

    tk.Label(
        ventana,
        text="Dinero total"
    ).pack()

    entry_dinero = tk.Entry(ventana)
    entry_dinero.pack()

    entry_dinero.insert(
        0,
        str(dinero)
    )

    tk.Label(
        ventana,
        text="Detalles"
    ).pack()

    entry_detalles = tk.Entry(
        ventana,
        width=50
    )

    entry_detalles.pack()

    entry_detalles.insert(
        0,
        detalles
    )

    falta_justificada = tk.BooleanVar(
        value=(tipo_registro == "justificada")
    )

    def actualizar_campos_falta():
        if falta_justificada.get():
            entry_canciones.config(state="disabled")
            entry_tiempo.config(state="disabled")
            entry_dinero.config(state="disabled")
        else:
            entry_canciones.config(state="normal")
            entry_tiempo.config(state="normal")
            entry_dinero.config(state="normal")

    tk.Checkbutton(
        ventana,
        text="Falta justificada",
        variable=falta_justificada,
        command=actualizar_campos_falta
    ).pack()

    actualizar_campos_falta()

    def guardar_cambios():

        try:

            fecha_nueva = (
                fecha_pantalla_a_db(
                    entry_fecha.get()
                )
            )

            if fecha_nueva is None:

                messagebox.showerror(
                    "Error",
                    "Formato inválido. Usar DD-MM-AAAA"
                )

                return

            if database.existe_fecha(
                fecha_nueva,
                excluir_id=registro_id
            ):

                messagebox.showerror(
                    "Fecha duplicada",
                    f"Ya existe un registro para "
                    f"{entry_fecha.get()}.\n\n"
                    f"Elija otra fecha o elimine "
                    f"primero el registro existente."
                )

                return

            canciones_texto = (
                entry_canciones.get().strip()
            )

            canciones_nuevas = (
                int(canciones_texto)
                if canciones_texto
                else 0
            )

            tiempo_texto = (
                entry_tiempo.get().strip()
            )

            if tiempo_texto:

                tiempo_nuevo = parsear_tiempo(
                    tiempo_texto
                )

            else:

                tiempo_nuevo = 0

            if tiempo_nuevo is None:

                messagebox.showerror(
                    "Error",
                    "Formato de tiempo inválido"
                )

                return

            dinero_texto = (
                entry_dinero.get().strip()
            )

            dinero_nuevo = (
                float(dinero_texto)
                if dinero_texto
                else 0
            )

            detalles_nuevos = (
                entry_detalles.get()
            )

            tipo_registro_nuevo = (
                "justificada"
                if falta_justificada.get()
            else "trabajado"
            )

            database.actualizar_registro(
                registro_id,
                fecha_nueva,
                canciones_nuevas,
                tiempo_nuevo,
                dinero_nuevo,
                detalles_nuevos,
                tipo_registro_nuevo
            )

            # ===========================
            # REFRESCAR FILA EN TABLA
            # ===========================

            registro_actualizado = (
                registro_id,
                fecha_nueva,
                canciones_nuevas,
                tiempo_nuevo,
                dinero_nuevo,
                detalles_nuevos,
                tipo_registro_nuevo
            )

            color, valores = (
                obtener_datos_fila(
                    registro_actualizado
                )
            )

            tabla.item(
                str(registro_id),
                values=valores,
                tags=(color,)
            )

            tabla.winfo_toplevel().lift()
            tabla.winfo_toplevel().focus_force()

            messagebox.showinfo(
                "Registro actualizado",
                "Los cambios fueron guardados."
            )

            tabla.winfo_toplevel().lift()
            tabla.winfo_toplevel().focus_force()

            ventana.destroy()

            tabla.winfo_toplevel().lift()
            tabla.winfo_toplevel().focus_force()

        except Exception as e:

            messagebox.showerror(
                "Error",
                str(e)
            )

    tk.Button(
        ventana,
        text="Guardar cambios",
        command=guardar_cambios
    ).pack(pady=10)
