# ./RegistroLaboral/resumenes/mtp.py




# ===============================
# M.T.P.
# MEJOR TIEMPO PROMEDIO
# ===============================

def obtener_mtp(registros):

    mejor = None
    mejor_promedio = None

    for registro in registros:

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
            continue

        if tiempo_seg <= 0:
            continue

        promedio = tiempo_seg / canciones

        if mejor is None:

            mejor = registro
            mejor_promedio = promedio
            continue

        if promedio < mejor_promedio:

            mejor = registro
            mejor_promedio = promedio

    return mejor
