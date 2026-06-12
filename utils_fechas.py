# ./RegistroLaboral/utils_fechas.py

from datetime import datetime, timedelta
from constantes import DIAS


def fecha_con_dia(fecha):

    fecha_dt = datetime.strptime(
        fecha,
        "%Y-%m-%d"
    )

    return (
        f"{DIAS[fecha_dt.weekday()]} "
        f"{fecha_dt.strftime('%d/%m/%Y')}"
    )


def numero_lunes_del_anio(fecha_dt):

    contador = 0

    dia = datetime(
        fecha_dt.year,
        1,
        1
    )

    while dia <= fecha_dt:

        if dia.weekday() == 0:
            contador += 1

        dia += timedelta(days=1)

    return contador


from datetime import datetime

def fecha_larga(fecha_db):

    dias = [
        "Lunes",
        "Martes",
        "Miércoles",
        "Jueves",
        "Viernes",
        "Sábado",
        "Domingo"
    ]

    meses = [
        "",
        "Enero",
        "Febrero",
        "Marzo",
        "Abril",
        "Mayo",
        "Junio",
        "Julio",
        "Agosto",
        "Septiembre",
        "Octubre",
        "Noviembre",
        "Diciembre"
    ]

    try:
        fecha = datetime.strptime(
            fecha_db,
            "%Y-%m-%d"
        )
    except ValueError:
        fecha = datetime.strptime(
            fecha_db,
            "%d-%m-%Y"
        )

    return (
        f"{dias[fecha.weekday()]} "
        f"{fecha.day:02d} de "
        f"{meses[fecha.month]} de "
        f"{fecha.year}"
    )
