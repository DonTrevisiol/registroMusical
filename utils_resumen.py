# ./RegistroLaboral/utils_resumen.py

from utils import (
    fecha_db_a_pantalla
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
        f"{fecha_db_a_pantalla(fecha)}"
        f" | {canciones} canciones"
        f" | ${dinero:.2f}"
    )
