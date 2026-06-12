# ./RegistroLaboral/tabla_mes.py

import tkinter as tk
from tkinter import ttk
from exportar_pdf import (
    exportar_tabla_mensual_pdf
)
from datetime import (
    datetime,
    timedelta
)
import database
from constantes import (
    MESES
)
from exportar_xlsx import (
    exportar_tabla_mensual_xlsx
)
from registros_virtuales import (
    generar_registros_mes
)
from resumen_mensual import (
    mostrar_resumen_mensual
)
from editar_registro import (
    editar_registro_seleccionado
)
from eliminar_registro import (
    eliminar_registro_seleccionado
)
from tabla_utils import (
    obtener_datos_fila
)

def mostrar_meses(anio):

    ventana_meses = tk.Toplevel()
    ventana_meses.title(f"Año {anio}")

    tk.Label(
        ventana_meses,
        text=f"Meses registrados en {anio}"
    ).pack(pady=10)

    meses = database.obtener_meses(anio)

    for mes in meses:

        nombre_mes = MESES.get(mes, mes)

        tk.Button(
            ventana_meses,
            text=nombre_mes,
            width=20,
            command=lambda a=anio, m=mes: mostrar_registros_mes(a, m)
        ).pack(pady=2)


def mostrar_registros_mes(anio, mes):

    registros = generar_registros_mes(anio, mes)

    ventana = tk.Toplevel()
    ventana.title(f"Registros - {mes}/{anio}")

    ventana.attributes("-zoomed", True)

    nombre_mes = MESES.get(
        str(mes).zfill(2),
        str(mes)
    )

    tk.Label(
        ventana,
        text=f"{nombre_mes} {anio}",
        font=("Arial", 16, "bold")
    ).pack(pady=5)

    frame_botones = tk.Frame(
        ventana
    )

    frame_botones.pack(
        pady=5
    )

    tk.Button(
        frame_botones,
        text="Resumen mensual",
        command=lambda:
        mostrar_resumen_mensual(
            generar_registros_mes(
                anio,
                mes
            )
        )
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        frame_botones,
        text="Exportar XLSX",
        command=lambda:
        exportar_tabla_mensual_xlsx(
            str(anio),
            str(mes).zfill(2),
            registros
        )
    ).pack(
        side="left",
        padx=5
    )

    tk.Button(
        frame_botones,
        text="Exportar PDF",
        command=lambda:
        exportar_tabla_mensual_pdf(
            str(anio),
            str(mes).zfill(2),
            registros
        )
    ).pack(
        side="left",
        padx=5
    )

    columnas = (
        "semana",
        "fecha",
        "canciones",
        "tiempo_total",
        "tiempo_promedio",
        "dinero_total",
        "dinero_promedio",
        "detalles"
    )

    frame_tabla = tk.Frame(
        ventana
    )

    frame_tabla.pack(
        fill="both",
        expand=True,
        padx=5,
        pady=5
    )

    tabla = ttk.Treeview(
        frame_tabla,
        columns=columnas,
        show="headings",
        height=25
    )

    # ===========================
    # COLORES DE FILAS
    # ===========================

    tabla.tag_configure(
        "rojo",
        foreground="red"
    )

    tabla.tag_configure(
        "azul",
        foreground="blue"
    )

    tabla.tag_configure(
        "verde",
        foreground="green"
    )

    tabla.tag_configure(
        "morado",
        foreground="purple"
    )

    tabla.tag_configure(
        "gris",
        foreground="gray"
    )

    def mostrar_menu(event):

        fila = tabla.identify_row(event.y)

        if not fila:
            return

        tabla.selection_set(fila)

        menu_contextual.post(
            event.x_root,
            event.y_root
        )

    tabla.bind(
        "<Button-3>",
        mostrar_menu
    )

    tabla.heading("semana", text="#")
    tabla.heading("fecha", text="Fecha")
    tabla.heading("canciones", text="Canciones")
    tabla.heading("tiempo_total", text="Tiempo total")
    tabla.heading("tiempo_promedio", text="Tiempo promedio")
    tabla.heading("dinero_total", text="Dinero total")
    tabla.heading("dinero_promedio", text="Dinero promedio")
    tabla.heading("detalles", text="Detalles")

    tabla.column("semana", width=28)
    tabla.column("fecha", width=120)
    tabla.column("canciones", width=80)
    tabla.column("tiempo_total", width=120)
    tabla.column("tiempo_promedio", width=120)
    tabla.column("dinero_total", width=100)
    tabla.column("dinero_promedio", width=120)
    tabla.column("detalles", width=450)


    scrollbar = ttk.Scrollbar(
        frame_tabla,
        orient="vertical",
        command=tabla.yview
    )

    tabla.configure(
        yscrollcommand=scrollbar.set
    )

    tabla.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    # ===========================
    # PANEL DE DETALLES
    # ===========================

    frame_detalles = tk.Frame(
        ventana
    )

    frame_detalles.pack(
        fill="x",
        padx=1,
        pady=1
    )

    tk.Label(
        frame_detalles,
        text="Detalles completos:"
    ).pack(anchor="w")

    texto_detalles = tk.Text(
        frame_detalles,
        height=7,
        wrap="word",
        state="disabled"
    )

    texto_detalles.pack(
        fill="x"
    )


    # ===========================
    # MENÚ CONTEXTUAL
    # ===========================

    menu_contextual = tk.Menu(
        ventana,
        tearoff=0
    )

    menu_contextual.add_command(
        label="Editar",
        command=lambda:

    editar_registro_seleccionado(tabla)
    )

    menu_contextual.add_separator()

    menu_contextual.add_command(
        label="Eliminar",
        command=lambda:
        eliminar_registro_seleccionado(tabla)
    )

    # ===========================
    # MOSTRAR DETALLES
    # ===========================

    def mostrar_detalles(event):

        seleccion = tabla.selection()

        if not seleccion:
            return

        valores = tabla.item(
            seleccion[0],
            "values"
        )

        detalle = valores[7]

        texto_detalles.config(
            state="normal"
        )

        texto_detalles.delete(
            "1.0",
            tk.END
        )

        texto_detalles.insert(
            tk.END,
            detalle
        )

        texto_detalles.config(
            state="disabled"
        )

    tabla.bind(
        "<<TreeviewSelect>>",
        mostrar_detalles
    )
    for registro in registros:

        color, valores = (
            obtener_datos_fila(
                registro
            )
        )

        tabla.insert(
            "",
            "end",
            iid=str(registro[0]),
            tags=(color,),
            values=valores
        )
