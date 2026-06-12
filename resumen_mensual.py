# ./RegistroLaboral/resumen_mensual.py
import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import resumenes

from exportar_pdf import (
    exportar_resumen_mensual_pdf
)

from utils import (
    formatear_tiempo_total,
    formatear_tiempo_promedio
)

from utils_fechas import (
    fecha_con_dia,
    numero_lunes_del_anio
)

from resumenes import (
    obtener_mejor_dia,
    obtener_peor_dia,
    obtener_mtp,
    obtener_mpp
)

def mostrar_resumen_mensual(registros):

    datos = resumenes.calcular_resumen_mensual(
        registros
    )

    mejor_dia = resumenes.obtener_mejor_dia(
        registros
    )

    peor_dia = resumenes.obtener_peor_dia(
        registros
    )

    mtp = resumenes.obtener_mtp(
        registros
    )

    mpp = resumenes.obtener_mpp(
        registros
    )

    ventana = tk.Toplevel()

    ventana.title(
        "Resumen mensual"
    )

    if mejor_dia:

        fecha_mejor = fecha_con_dia(
            mejor_dia[1]
        )

        mejor_dia_texto = (
            f"{fecha_mejor} → "
            f"${mejor_dia[4]:.2f}"
        )

    else:

        mejor_dia_texto = (
            "No disponible"
        )


    if peor_dia:

        fecha_peor = fecha_con_dia(
            peor_dia[1]
        )

        peor_dia_texto = (
            f"{fecha_peor} → "
            f"${peor_dia[4]:.2f}"
        )

    else:

        peor_dia_texto = (
            "No disponible"
        )

    if mtp:

        fecha_mtp = fecha_con_dia(
            mtp[1]
        )

        promedio = mtp[3] / mtp[2]

        mtp_texto = (
            f"{fecha_mtp} → "
            f"{formatear_tiempo_promedio(promedio)}"
        )

    else:

        mtp_texto = "No disponible"

    if mpp:

        fecha_mpp = fecha_con_dia(
            mpp[1]
        )

        promedio_mpp = (
            mpp[4] / mpp[2]
        )

        mpp_texto = (
            f"{fecha_mpp} → "
            f"${promedio_mpp:.2f}"
        )

    else:

        mpp_texto = (
            "No disponible"
        )

    texto = (
        f"Canciones totales: "
        f"{datos['canciones_totales']}\n\n"

        f"Tiempo total: "
        f"{formatear_tiempo_total(datos['tiempo_total'])}\n\n"

        f"Dinero total: "
        f"${datos['dinero_total']:.2f}\n\n"

        f"Días trabajados: "
        f"{datos['dias_trabajados']}\n\n"

        f"Faltas totales: "
        f"{datos['faltas_totales']}\n"
        f"Faltas justificadas: "
        f"{datos['faltas_justificadas']}\n"
        f"Faltas injustificadas: "
        f"{datos['faltas_injustificadas']}\n"

        f"\n\nMejor día:\n"
        f"{mejor_dia_texto}"

        f"\n\nPeor día:\n"
        f"{peor_dia_texto}"

        f"\n\nMejor tiempo promedio:\n"
        f"{mtp_texto}"

        f"\n\nMejor puntaje promedio:\n"
        f"{mpp_texto}"
    )

    tk.Label(
        ventana,
        text=texto,
        justify="left"
    ).pack(
        padx=20,
        pady=20
    )

    def exportar_pdf():

        archivo = (
            exportar_resumen_mensual_pdf(
                registros,
                texto
            )
        )

        messagebox.showinfo(
            "PDF generado",
            f"Se generó correctamente:\n\n{archivo}"
        )

    tk.Button(
        ventana,
        text="Exportar PDF",
        command=exportar_pdf
    ).pack(
        pady=10
    )
