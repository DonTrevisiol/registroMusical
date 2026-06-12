# ./RegistroLaboral/utils.py

import re
from datetime import datetime


# ===============================
# PARSEAR TIEMPO
# ===============================

def parsear_tiempo(tiempo_str):
    regex = r"(\d+)\s*[hH]\s*(\d+)'\s*(\d+)\":(\d+)"
    match = re.match(regex, tiempo_str)

    if not match:
        return None

    h, m, s, cs = map(int, match.groups())

    return h * 3600 + m * 60 + s + cs / 100


# ===============================
# TIEMPO TOTAL
# Formato:
# 1h23'45":67
# ===============================

def formatear_tiempo_total(segundos):

    h = int(segundos // 3600)

    segundos %= 3600

    m = int(segundos // 60)

    segundos %= 60

    s = int(segundos)

    cs = int(round((segundos - s) * 100))

    return f"{h}h{m:02d}'{s:02d}\":{cs:02d}"


# ===============================
# TIEMPO PROMEDIO
# Formato:
# 04'50":22
# ===============================

def formatear_tiempo_promedio(segundos):

    minutos = int(segundos // 60)

    segundos %= 60

    s = int(segundos)

    cs = int(round((segundos - s) * 100))

    return f"{minutos:02d}'{s:02d}\":{cs:02d}"


# ===============================
# FECHAS
# ===============================

def fecha_db_a_pantalla(fecha_db):

    return datetime.strptime(
        fecha_db,
        "%Y-%m-%d"
    ).strftime("%d-%m-%Y")


def fecha_pantalla_a_db(fecha_texto):

    try:

        return datetime.strptime(
            fecha_texto,
            "%d-%m-%Y"
        ).strftime("%Y-%m-%d")

    except ValueError:

        return None
