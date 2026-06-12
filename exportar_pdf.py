# ./RegistroLaboral/exportar_pdf.py

import os

from constantes import MESES

from tkinter import messagebox

from tabla_utils import obtener_datos_fila

from reportlab.platypus import (
    SimpleDocTemplate,
    Table,
    TableStyle,
    Paragraph,
    Spacer,
    Image
)

from reportlab.lib import colors

from reportlab.lib.styles import (
    getSampleStyleSheet
)

from reportlab.lib.pagesizes import (
    landscape,
    letter
)


def exportar_resumen_anual_pdf(
    anio,
    texto
):

    carpeta_anio = (
        f"PDFs/{anio}"
    )

    os.makedirs(
        carpeta_anio,
        exist_ok=True
    )

    nombre_archivo = (
        f"{carpeta_anio}/anual.pdf"
    )

    documento = SimpleDocTemplate(
        nombre_archivo,
        pagesize=landscape(letter),
        leftMargin=60,
        rightMargin=60,
        topMargin=15,
        bottomMargin=15
    )

    estilos = (
        getSampleStyleSheet()
    )

    contenido = []

    # ==========================
    # LOGO
    # ==========================

    if os.path.exists("logo.png"):

        contenido.append(
            Image(
                "logo.png",
                width=60,
                height=60
            )
        )

    contenido.append(
        Paragraph(
            f"<b>RESUMEN ANUAL {anio}</b>",
            estilos["Title"]
        )
    )

    contenido.append(
        Spacer(1, 10)
    )

    lineas = [
        linea.strip()
        for linea in texto.split("\n")
        if linea.strip()
    ]

    mitad = (
        len(lineas) + 1
    ) // 2

    izquierda = lineas[:mitad]
    derecha = lineas[mitad:]

    while len(derecha) < len(izquierda):
        derecha.append("")

    filas = []

    for izq, der in zip(
        izquierda,
        derecha
    ):

        filas.append([
            Paragraph(
                izq,
                estilos["BodyText"]
            ),
            Paragraph(
                der,
                estilos["BodyText"]
            )
        ])

    tabla = Table(
        filas,
        colWidths=[330, 330]
    )

    tabla.setStyle(
        TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING", (60,60), (-1,-1), 5),
            ("RIGHTPADDING", (0,0), (-1,-1), 5),
            ("TOPPADDING", (0,0), (-1,-1), 2),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ])
    )

    contenido.append(
        tabla
    )

    documento.build(
        contenido
    )

    return nombre_archivo


def exportar_resumen_mensual_pdf(
    registros,
    texto
):

    if not registros:
        return None

    fecha = registros[0][1]

    anio = fecha[:4]
    mes = fecha[5:7]

    carpeta_anio = (
        f"PDFs/{anio}"
    )

    os.makedirs(
        carpeta_anio,
        exist_ok=True
    )

    nombre_mes = (
        MESES[mes]
        .lower()
    )

    nombre_archivo = (
        f"{carpeta_anio}/{nombre_mes}.pdf"
    )

    documento = SimpleDocTemplate(
        nombre_archivo,
        pagesize=landscape(letter),
        leftMargin=40,
        rightMargin=40,
        topMargin=15,
        bottomMargin=15
    )

    estilos = (
        getSampleStyleSheet()
    )

    contenido = []

    if os.path.exists(
        "logo.png"
    ):

        contenido.append(
            Image(
                "logo.png",
                width=60,
                height=60
            )
        )

    contenido.append(
        Paragraph(
            f"<b>RESUMEN {MESES[mes].upper()} {anio}</b>",
            estilos["Title"]
        )
    )

    contenido.append(
        Spacer(1, 10)
    )

    lineas = [
        linea.strip()
        for linea in texto.split("\n")
        if linea.strip()
    ]

    mitad = (
        len(lineas) + 1
    ) // 2

    izquierda = lineas[:mitad]
    derecha = lineas[mitad:]

    while len(derecha) < len(izquierda):
        derecha.append("")

    filas = []

    for izq, der in zip(
        izquierda,
        derecha
    ):

        filas.append([
            Paragraph(
                izq,
                estilos["BodyText"]
            ),
            Paragraph(
                der,
                estilos["BodyText"]
            )
        ])

    tabla = Table(
        filas,
        colWidths=[330, 330]
    )

    tabla.setStyle(
        TableStyle([
            ("VALIGN", (0,0), (-1,-1), "TOP"),
            ("LEFTPADDING", (0,0), (-1,-1), 5),
            ("RIGHTPADDING", (0,0), (-1,-1), 5),
            ("TOPPADDING", (0,0), (-1,-1), 2),
            ("BOTTOMPADDING", (0,0), (-1,-1), 2),
        ])
    )

    contenido.append(
        tabla
    )

    documento.build(
        contenido
    )

    return nombre_archivo

def exportar_tabla_mensual_pdf(
    anio,
    mes,
    registros
):

    carpeta_anio = f"PDFs/{anio}"

    os.makedirs(
        carpeta_anio,
        exist_ok=True
    )

    nombre_mes = (
        MESES[mes]
        .lower()
    )

    archivo = (
        f"{carpeta_anio}/tabla_{nombre_mes}.pdf"
    )

    documento = SimpleDocTemplate(
        archivo,
        pagesize=landscape(letter),
        leftMargin=20,
        rightMargin=20,
        topMargin=15,
        bottomMargin=15
    )

    estilos = getSampleStyleSheet()

    contenido = []

    if os.path.exists("logo.png"):

        contenido.append(
            Image(
                "logo.png",
                width=60,
                height=60
            )
        )

    contenido.append(
        Paragraph(
            f"<b>TABLA {MESES[mes].upper()} {anio}</b>",
            estilos["Title"]
        )
    )

    contenido.append(
        Spacer(1, 10)
    )

    datos = [[
        "#",
        "Fecha",
        "Canciones",
        "Tiempo",
        "Tiempo prom.",
        "Puntaje",
        "Puntaje prom.",
        "Detalles"
    ]]

    estilos_tabla = [

        ("GRID",
        (0,0),
        (-1,-1),
        0.5,
        colors.black),

        ("BACKGROUND",
        (0,0),
        (-1,0),
        colors.HexColor("#1F4E78")),

        ("TEXTCOLOR",
        (0,0),
        (-1,0),
        colors.white),

        ("FONTNAME",
        (0,0),
        (-1,0),
        "Helvetica-Bold"),

        ("ALIGN",
        (0,0),
        (-2,-1),
        "CENTER"),

        ("VALIGN",
        (0,0),
        (-1,-1),
        "MIDDLE"),
    ]

    def resumir_detalle(
        texto,
        limite=50
    ):

        if len(texto) <= limite:
            return texto

        return texto[:limite] + "..."

    for registro in registros:

        color, valores = (
            obtener_datos_fila(
                registro
            )
        )

        fila = list(valores)

        fila[7] = resumir_detalle(
            str(fila[7])
        )

        datos.append(fila)

        numero_fila = len(datos) - 1

        colores_pdf = {

            "rojo": colors.red,
            "azul": colors.blue,
            "verde": colors.green,
            "morado": colors.purple,
            "gris": colors.gray

        }

        if color in colores_pdf:

            estilos_tabla.append(
                (
                    "TEXTCOLOR",
                    (0, numero_fila),
                    (-1, numero_fila),
                    colores_pdf[color]
                )

            )

    tabla = Table(
        datos,
        colWidths=[
            35,
            80,
            50,
            70,
            70,
            60,
            60,
            250
        ]
    )

    tabla.setStyle(
        TableStyle(estilos_tabla)
    )

    contenido.append(
        tabla
    )

    documento.build(
        contenido
    )

    messagebox.showinfo(
        "PDF exportado",
        f"Tabla guardada en:\n\n{archivo}"
    )

    return archivo
