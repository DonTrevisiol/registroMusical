# ./RegistroLaboral/utils_resumen.py

from utils import (
    formatear_tiempo_promedio
)
from utils_fechas import (
    fecha_larga
)

def resumir_registro(registro):

    if registro is None:
        return "N/A"

    (
        registro_id,
        fecha,
        canciones,
        tiempo_seg,
        dinero,
        detalles,
        tipo_registro
    ) = registro

    return (
        f"{fecha_larga(fecha)}\n"
        f"{canciones} canciones\n"
        f"${dinero:.2f}"
    )

def resumir_mtp(registro):

    if registro is None:
        return "N/A"

    (
        registro_id,
        fecha,
        canciones,
        tiempo_seg,
        dinero,
        detalles,
        tipo_registro
    ) = registro

    if canciones <= 0:
        return "N/A"

    promedio = tiempo_seg / canciones

    return (
        f"{fecha_larga(fecha)}\n"
        f"{formatear_tiempo_promedio(promedio)}"
    )

def resumir_mpp(registro):

    if registro is None:
        return "N/A"

    (
        registro_id,
        fecha,
        canciones,
        tiempo_seg,
        dinero,
        detalles,
        tipo_registro
    ) = registro

    if canciones <= 0:
        return "N/A"

    promedio = dinero / canciones

    return (
        f"{fecha_larga(fecha)}\n"
        f"${promedio:.2f}"
    )
