# ./RegistroLaboral/resumen_anual.py

import tkinter as tk
from datetime import datetime
import database

from tkinter import messagebox

from exportar_pdf import (
    exportar_resumen_anual_pdf
)

from registros_virtuales import (
    generar_registros_mes
)

from utils_fechas import fecha_larga

from cierre_anual import (
    cerrar_anio
)
from estadisticas_anuales.resumen_general import (
    calcular_resumen_anual
)

from estadisticas_anuales.mejor_mes import (
    obtener_mejor_mes
)

from estadisticas_anuales.peor_mes import (
    obtener_peor_mes
)

from estadisticas_anuales.mes_responsable import (
    obtener_mes_responsable
)

from estadisticas_anuales.mes_irresponsable import (
    obtener_mes_irresponsable
)

from estadisticas_anuales.mejor_dia_anual import (
    obtener_mejor_dia_anual
)

from estadisticas_anuales.peor_dia_anual import (
    obtener_peor_dia_anual
)

from estadisticas_anuales.mtp_anual import (
    obtener_mtp_anual
)

from estadisticas_anuales.mpp_anual import (
    obtener_mpp_anual
)

from estadisticas_anuales.mes_constante import (
    obtener_mes_constante
)

from estadisticas_anuales.promedios import (
    obtener_promedios_anuales
)

from utils import (
    formatear_tiempo_total, formatear_tiempo_promedio
)

from utils_texto import (
    nombre_mes
)

from utils_resumen import (
    resumir_registro,
    resumir_mtp,
    resumir_mpp
)


def mostrar_resumen_anual(anio):

    registros = []

    for mes in range(1, 13):

        registros.extend(
            generar_registros_mes(
                anio,
                str(mes).zfill(2)
            )
        )

    datos = calcular_resumen_anual(
        registros
    )

    (
        promedio_diario,
        promedio_cancion,
        promedio_tiempo_cancion
    ) = obtener_promedios_anuales(anio)

    (
        mejor_mes,
        dinero_mejor_mes
    ) = obtener_mejor_mes(anio)

    (
        peor_mes,
        dinero_peor_mes
    ) = obtener_peor_mes(anio)

    (
        mes_responsable,
        dias_mes_responsable
    ) = obtener_mes_responsable(anio)

    (
        mes_irresponsable,
        faltas_mes_irresponsable
    ) = obtener_mes_irresponsable(anio)
    mejor_dia = ( obtener_mejor_dia_anual(anio) )
    peor_dia = ( obtener_peor_dia_anual(anio) )
    mtp = ( obtener_mtp_anual(anio) )
    mpp = ( obtener_mpp_anual(anio) )
    mes_constante = ( obtener_mes_constante(anio) )

    ventana = tk.Toplevel()

    ventana.geometry(
        "900x850"
    )

    ventana.attributes("-zoomed", True)


    ventana.title(
        f"Resumen anual {anio}"
    )

    cerrado = (
        database.anio_esta_cerrado(
            anio
        )
    )

    cierre = (
        database.obtener_cierre_anual(
            anio
        )
    )

    texto_mejor_dia = (
        resumir_registro(mejor_dia)
    )

    texto_peor_dia = (
        resumir_registro(peor_dia)
    )

    texto_mtp = (
        resumir_mtp(mtp)
    )

    texto_mpp = (
        resumir_mpp(mpp)
    )

    if mes_constante:
        (
            numero_mes_constante,
            diferencia_constante,
            _,
            _,
            _
        ) = mes_constante

    else:
        numero_mes_constante = None
        diferencia_constante = 0

    texto = (
        f"═══════════════════════\n"
        f"RESUMEN ANUAL {anio}\n"
        f"═══════════════════════\n"
        f"📀 Canciones: "
        f"{datos['canciones_totales']}\n"

        f"⏱ Tiempo total: "
        f"{formatear_tiempo_total(datos['tiempo_total'])}\n"

        f"💰 Puntaje total: "
        f"${datos['dinero_total']:.2f}\n\n"

        f"📅 Días trabajados: "
        f"{datos['dias_trabajados']}\n"

        f"❌ Faltas totales: "
        f"{datos['faltas_totales']}\n"
        f"❌ Faltas justificadas: "
        f"{datos['faltas_justificadas']}\n"
        f"❌ Faltas injustificadass: "
        f"{datos['faltas_injustificadas']}\n\n"

        f"🏆 Mejor mes: "
        f"{nombre_mes(mejor_mes)}\n"
        f"(${dinero_mejor_mes:.2f})\n"

        f"📉 Peor mes: "
        f"{nombre_mes(peor_mes)}\n"
        f"(${dinero_peor_mes:.2f})\n"

        f"🛡 Mes más responsable: "
        f"{nombre_mes(mes_responsable)}\n"
        f"({dias_mes_responsable} días)\n"

        f"⚠️ Mes más irresponsable: "
        f"{nombre_mes(mes_irresponsable)}\n"
        f"({faltas_mes_irresponsable} faltas)\n"

        f"📏 Mes más constante: "
        f"{nombre_mes(numero_mes_constante)} "
        f"(${diferencia_constante:.2f})\n\n"

        f"🥇 Mejor día del año:\n"
        f"{texto_mejor_dia}\n\n"

        f"🥀 Peor día del año:\n"
        f"{texto_peor_dia}\n\n"

        f"⚡ Mejor tiempo promedio:\n"
        f"{texto_mtp}\n\n"

        f"💵 Mejor puntaje promedio:\n"
        f"{texto_mpp}\n\n"

        f"📊 Promedio diario anual: "
        f"${promedio_diario:.2f}\n"

        f"🎵 Promedio por canción: "
        f"${promedio_cancion:.2f}\n"

        f"⏳ Promedio anual de tiempo por canción: "
        f"{formatear_tiempo_promedio(promedio_tiempo_cancion)}\n"
    )

    if cerrado and cierre:

        observaciones, objetivos, fecha_cierre = cierre

        texto += (
            "\n\n"
            "═══════════════════════\n"
            "CIERRE ANUAL\n"
            "═══════════════════════\n\n"

            "OBSERVACIONES GENERALES\n\n"
            f"{observaciones}\n\n"

            "═══════════════════════\n\n"

            f"OBJETIVOS PARA {int(anio)+1}\n\n"
            f"{objetivos}\n\n"

            "═══════════════════════\n\n"

            f"Fecha de cierre: "
            f"{fecha_larga(fecha_cierre)}\n"
        )

    # ==========================
    # RESUMEN
    # ==========================

    frame_texto = tk.Frame(
        ventana
    )

    frame_texto.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    scrollbar = tk.Scrollbar(
        frame_texto
    )

    scrollbar.pack(
        side="right",
        fill="y"
    )

    texto_resumen = tk.Text(
        frame_texto,
        width=80,
        height=35,
        wrap="word",
        yscrollcommand=scrollbar.set
    )

    texto_resumen.pack(
        side="left",
        fill="both",
        expand=True
    )

    scrollbar.config(
        command=texto_resumen.yview
    )

    texto_resumen.insert(
        "1.0",
        texto
    )

    texto_resumen.tag_configure(
        "centrado",
        justify="center"
    )

    texto_resumen.tag_add(
        "centrado",
        "1.0",
        "end"
    )

    texto_resumen.config(
        state="disabled"
    )

    # ===========================
    # BOTÓN CERRAR AÑO
    # ===========================

    hoy = datetime.now()

    puede_cerrarse = (
        hoy.year > int(anio)
    )

    estado_boton = "normal"

    if cerrado:
        estado_boton = "disabled"

    if not puede_cerrarse:
        estado_boton = "disabled"

    tk.Button(
        ventana,
        text="Cerrar año",
        state=estado_boton,
        command=lambda:
            cerrar_anio(anio)
    ).pack(
        pady=10
    )

    def exportar_pdf():
        archivo = (
            exportar_resumen_anual_pdf(
                anio,
                texto
            )
        )

        messagebox.showinfo(
            "PDF generado",
            f"Se generó correctamente: \n\n{archivo}"
        )

    def exportar_pdf_seguro():

        if not cerrado:

            messagebox.showinfo(
                "Año sin cerrar",
                "Primero debes realizar el cierre anual."
            )

            return

        exportar_pdf()


    tk.Button(
        ventana,
        text="Exportar PDF",
        command=exportar_pdf_seguro
    ).pack(
        pady=5
    )

