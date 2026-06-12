# ./RegistroLaboral/database.py

import sqlite3

DB_NAME = "registros.db"


def conectar():
    return sqlite3.connect(DB_NAME)


def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS registros (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha TEXT NOT NULL UNIQUE,
        canciones INTEGER,
        tiempo_total_segundos REAL,
        dinero_total REAL,
        detalles TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS observaciones_anuales (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        anio INTEGER UNIQUE,
        observaciones TEXT,
        objetivos TEXT,
        fecha_cierre TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vacaciones (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fecha_inicio TEXT NOT NULL,
        fecha_fin TEXT NOT NULL,
        observaciones text
    )
    """)

    try:
        cursor.execute("""
            ALTER TABLE registros
            ADD COLUMN tipo_registro TEXT
    """)

    except:
        pass


    cursor.execute("""
        UPDATE registros
        SET tipo_registro = 'trabajado'
        WHERE tipo_registro IS NULL
    """)

    conn.commit()
    conn.close()




def insertar_registro(
    fecha,
    canciones,
    tiempo_total_segundos,
    dinero_total,
    detalles,
    tipo_registro
):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO registros (
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro
    )
    VALUES (?, ?, ?, ?, ?, ?)
    """, (
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro
    ))

    conn.commit()
    conn.close()

def guardar_cierre_anual(
    anio,
    observaciones,
    objetivos,
    fecha_cierre
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO observaciones_anuales (
        anio,
        observaciones,
        objetivos,
        fecha_cierre
    )
    VALUES (?, ?, ?, ?)
    """, (
        anio,
        observaciones,
        objetivos,
        fecha_cierre
    ))

    conn.commit()
    conn.close()

def obtener_cierre_anual(anio):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        observaciones,
        objetivos,
        fecha_cierre
    FROM observaciones_anuales
    WHERE anio = ?
    """, (anio,))

    dato = cursor.fetchone()

    conn.close()

    return dato

def fecha_es_vacaciones(fecha):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT COUNT(*)
    FROM vacaciones
    WHERE ? BETWEEN fecha_inicio
    AND fecha_fin
    """, (
        fecha,
    ))

    cantidad = cursor.fetchone()[0]

    conn.close()

    return cantidad > 0

def obtener_registros():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro
    FROM registros
    ORDER BY fecha
    """)

    datos = cursor.fetchall()

    conn.close()

    return datos

# ==============================
# CONSULTAS PARA NAVEGACIÓN
# ==============================

def obtener_anios():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT DISTINCT SUBSTR(fecha,1,4)
    FROM registros
    ORDER BY SUBSTR(fecha,1,4) DESC
    """)

    datos = [fila[0] for fila in cursor.fetchall()]

    conn.close()

    return datos


def obtener_meses(anio):

    from datetime import datetime

    anio = int(anio)

    hoy = datetime.now()

    if anio < hoy.year:

        return [
            "01","02","03","04",
            "05","06","07","08",
            "09","10","11","12"
        ]

    elif anio == hoy.year:

        return [
            str(m).zfill(2)
            for m in range(
                1,
                hoy.month + 1
            )
        ]

    return []

def obtener_registros_mes(anio, mes):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro
    FROM registros
    WHERE SUBSTR(fecha,1,4)=?
      AND SUBSTR(fecha,6,2)=?
    ORDER BY fecha
    """, (
        str(anio),
        str(mes).zfill(2)
    ))

    datos = cursor.fetchall()

    conn.close()

    return datos

# ==============================
# ELIMINAR REGISTRO
# ==============================

def eliminar_registro(registro_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        DELETE FROM registros
        WHERE id = ?
        """,
        (registro_id,)
    )

    conn.commit()
    conn.close()

# ==============================
# OBTENER REGISTRO POR ID
# ==============================

def obtener_registro_por_id(registro_id):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro
    FROM registros
    WHERE id = ?
    """, (registro_id,))

    dato = cursor.fetchone()

    conn.close()

    return dato


# ==============================
# EXISTE FECHA
# ==============================

def existe_fecha(fecha, excluir_id=None):

    conn = conectar()
    cursor = conn.cursor()

    if excluir_id is None:

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM registros
            WHERE fecha = ?
            """,
            (fecha,)
        )

    else:

        cursor.execute(
            """
            SELECT COUNT(*)
            FROM registros
            WHERE fecha = ?
            AND id != ?
            """,
            (fecha, excluir_id)
        )

    cantidad = cursor.fetchone()[0]

    conn.close()

    return cantidad > 0


# ==============================
# ACTUALIZAR REGISTRO
# ==============================

def actualizar_registro(
    registro_id,
    fecha,
    canciones,
    tiempo_total_segundos,
    dinero_total,
    detalles,
    tipo_registro
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    UPDATE registros
    SET
        fecha = ?,
        canciones = ?,
        tiempo_total_segundos = ?,
        dinero_total = ?,
        detalles = ?,
        tipo_registro = ?
    WHERE id = ?
    """, (
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro,
        registro_id
    ))

    conn.commit()
    conn.close()

# ==============================
# PRIMER REGISTRO
# ==============================

def obtener_fecha_primer_registro():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT MIN(fecha)
    FROM registros
    """)

    resultado = cursor.fetchone()

    conn.close()

    if resultado and resultado[0]:
        return resultado[0]

    return None


# ==============================
# REGISTROS DE UN AÑO
# ==============================

def obtener_registros_anio(anio):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        fecha,
        canciones,
        tiempo_total_segundos,
        dinero_total,
        detalles,
        tipo_registro
    FROM registros
    WHERE SUBSTR(fecha,1,4)=?
    ORDER BY fecha
    """, (
        str(anio),
    ))

    datos = cursor.fetchall()

    conn.close()

    return datos


def guardar_cierre_anual(
    anio,
    observaciones,
    objetivos,
    fecha_cierre
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT OR REPLACE INTO observaciones_anuales (
        anio,
        observaciones,
        objetivos,
        fecha_cierre
    )
    VALUES (?, ?, ?, ?)
    """, (
        anio,
        observaciones,
        objetivos,
        fecha_cierre
    ))

    conn.commit()
    conn.close()


def obtener_cierre_anual(anio):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        observaciones,
        objetivos,
        fecha_cierre
    FROM observaciones_anuales
    WHERE anio = ?
    """, (
        anio,
    ))

    dato = cursor.fetchone()

    conn.close()

    return dato

def anio_esta_cerrado(anio):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM observaciones_anuales
        WHERE anio = ?
    """, (
        anio,
    ))

    cantidad = cursor.fetchone()[0]

    conn.close()

    return cantidad > 0


    # ==============================
    # VACACIONES
    # ==============================

def guardar_vacaciones(
    fecha_inicio,
    fecha_fin,
    observaciones
):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO vacaciones (
        fecha_inicio,
        fecha_fin,
        observaciones
    )
    VALUES (?, ?, ?)
    """, (
        fecha_inicio,
        fecha_fin,
        observaciones
    ))

    conn.commit()
    conn.close()


def obtener_vacaciones():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT
        id,
        fecha_inicio,
        fecha_fin,
        observaciones
    FROM vacaciones
    ORDER BY fecha_inicio
    """)

    datos = cursor.fetchall()

    conn.close()

    return datos
