
import tkinter as tk
from tkinter import ttk, messagebox, filedialog

import serial
import threading
import sqlite3
import csv

from datetime import datetime

from collections import deque

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# =========================================================
# CONFIGURACIÓN
# =========================================================

PUERTO = "COM5"
BAUDRATE = 115200

UMBRAL_PREALARMA = 2.0
UMBRAL_ALARMA = 4.0

MAX_MUESTRAS = 150

BASE_DATOS = "alarma_sismica.db"


# =========================================================
# VARIABLES
# =========================================================

conexion = None

ejecutando = False

alarma = False

contador_alarmas = 0

datos_x = deque(
    maxlen=MAX_MUESTRAS
)

datos_y = deque(
    maxlen=MAX_MUESTRAS
)

datos_z = deque(
    maxlen=MAX_MUESTRAS
)

datos_vibracion = deque(
    maxlen=MAX_MUESTRAS
)

tiempos = deque(
    maxlen=MAX_MUESTRAS
)


# =========================================================
# BASE DE DATOS
# =========================================================

def crear_base_datos():

    conexion_db = sqlite3.connect(
        BASE_DATOS
    )

    cursor = conexion_db.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mediciones (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            fecha TEXT,

            hora TEXT,

            ax REAL,

            ay REAL,

            az REAL,

            vibracion REAL,

            estado TEXT

        )
    """)

    conexion_db.commit()

    conexion_db.close()


def guardar_medicion(
    ax,
    ay,
    az,
    vibracion,
    estado
):

    conexion_db = sqlite3.connect(
        BASE_DATOS
    )

    cursor = conexion_db.cursor()

    fecha = datetime.now().strftime(
        "%Y-%m-%d"
    )

    hora = datetime.now().strftime(
        "%H:%M:%S.%f"
    )

    cursor.execute(
        """
        INSERT INTO mediciones
        (
            fecha,
            hora,
            ax,
            ay,
            az,
            vibracion,
            estado
        )

        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,

        (
            fecha,
            hora,
            ax,
            ay,
            az,
            vibracion,
            estado
        )
    )

    conexion_db.commit()

    conexion_db.close()


# =========================================================
# DETERMINAR ESTADO
# =========================================================

def determinar_estado(vibracion):

    if vibracion >= UMBRAL_ALARMA:

        return "ALARMA"

    elif vibracion >= UMBRAL_PREALARMA:

        return "PREALARMA"

    else:

        return "NORMAL"


# =========================================================
# CONECTAR ESP32
# =========================================================

def conectar():

    global conexion
    global ejecutando

    try:

        conexion = serial.Serial(
            PUERTO,
            BAUDRATE,
            timeout=1
        )

        ejecutando = True

        etiqueta_conexion.config(
            text="● ESP32 CONECTADO"
        )

        etiqueta_conexion.config(
            foreground="green"
        )

        boton_conectar.config(
            state="disabled"
        )

        hilo = threading.Thread(
            target=leer_esp32,
            daemon=True
        )

        hilo.start()

        registrar_evento(
            "ESP32 conectado"
        )

    except Exception as error:

        messagebox.showerror(
            "Error de conexión",
            f"No se pudo conectar:\n\n{error}"
        )


# =========================================================
# LEER ESP32
# =========================================================

def leer_esp32():

    global alarma
    global contador_alarmas

    while ejecutando:

        try:

            linea = (
                conexion
                .readline()
                .decode(
                    "utf-8",
                    errors="ignore"
                )
                .strip()
            )

            if not linea:

                continue

            # -----------------------------
            # RESET
            # -----------------------------

            if linea == "RESET":

                alarma = False

                ventana.after(
                    0,
                    actualizar_estado
                )

                registrar_evento(
                    "Alarma reiniciada"
                )

                continue

            # -----------------------------
            # Ignorar mensajes
            # -----------------------------

            if "," not in linea:

                continue

            partes = linea.split(",")

            if len(partes) != 4:

                continue

            try:

                ax = float(partes[0])
                ay = float(partes[1])
                az = float(partes[2])
                vibracion = float(partes[3])

            except ValueError:

                continue

            # -----------------------------
            # Estado
            # -----------------------------

            estado = determinar_estado(
                vibracion
            )

            # -----------------------------
            # Detectar alarma
            # -----------------------------

            if estado == "ALARMA":

                if not alarma:

                    alarma = True

                    contador_alarmas += 1

                    ventana.after(
                        0,
                        lambda: registrar_evento(
                            "🚨 ALARMA SÍSMICA"
                        )
                    )

            # -----------------------------
            # Guardar memoria
            # -----------------------------

            datos_x.append(ax)
            datos_y.append(ay)
            datos_z.append(az)

            datos_vibracion.append(
                vibracion
            )

            tiempos.append(
                len(tiempos)
            )

            # -----------------------------
            # Base de datos
            # -----------------------------

            guardar_medicion(
                ax,
                ay,
                az,
                vibracion,
                estado
            )

            # -----------------------------
            # Interfaz
            # -----------------------------

            ventana.after(
                0,
                actualizar_interfaz
            )

        except Exception:

            pass


# =========================================================
# ACTUALIZAR INTERFAZ
# =========================================================

def actualizar_interfaz():

    if not datos_vibracion:

        return

    ax = datos_x[-1]
    ay = datos_y[-1]
    az = datos_z[-1]

    vibracion = (
        datos_vibracion[-1]
    )

    valor_ax.config(
        text=f"{ax:.3f} m/s²"
    )

    valor_ay.config(
        text=f"{ay:.3f} m/s²"
    )

    valor_az.config(
        text=f"{az:.3f} m/s²"
    )

    valor_vibracion.config(
        text=f"{vibracion:.3f} m/s²"
    )

    actualizar_estado()

    actualizar_grafica()


# =========================================================
# ESTADO VISUAL
# =========================================================

def actualizar_estado():

    if alarma:

        etiqueta_estado.config(
            text="🚨 ALARMA SÍSMICA"
        )

        etiqueta_estado.config(
            foreground="red"
        )

        return

    if not datos_vibracion:

        return

    vibracion = (
        datos_vibracion[-1]
    )

    if vibracion >= UMBRAL_PREALARMA:

        etiqueta_estado.config(
            text="⚠️ PREALARMA"
        )

        etiqueta_estado.config(
            foreground="orange"
        )

    else:

        etiqueta_estado.config(
            text="● NORMAL"
        )

        etiqueta_estado.config(
            foreground="green"
        )


# =========================================================
# GRÁFICA
# =========================================================

def actualizar_grafica():

    grafica.clear()

    eje = grafica.add_subplot(111)

    if datos_vibracion:

        eje.plot(
            list(datos_vibracion),
            label="Vibración"
        )

        eje.axhline(
            UMBRAL_PREALARMA,
            linestyle="--",
            label="Prealarma"
        )

        eje.axhline(
            UMBRAL_ALARMA,
            linestyle="--",
            label="Alarma"
        )

    eje.set_title(
        "Vibración en tiempo real"
    )

    eje.set_xlabel(
        "Muestras"
    )

    eje.set_ylabel(
        "m/s²"
    )

    eje.grid()

    eje.legend()

    canvas.draw()


# =========================================================
# REGISTRAR EVENTO
# =========================================================

def registrar_evento(texto):

    hora = datetime.now().strftime(
        "%H:%M:%S"
    )

    lista_eventos.insert(
        0,
        f"[{hora}] {texto}"
    )


# =========================================================
# REINICIAR
# =========================================================

def reiniciar_alarma():

    global alarma

    alarma = False

    if conexion:

        try:

            conexion.write(
                b"RESET\n"
            )

        except:

            pass

    actualizar_estado()

    registrar_evento(
        "Alarma reiniciada manualmente"
    )


# =========================================================
# EXPORTAR CSV
# =========================================================

def exportar_csv():

    archivo = filedialog.asksaveasfilename(
        defaultextension=".csv",
        filetypes=[
            ("Archivo CSV", "*.csv")
        ]
    )

    if not archivo:

        return

    conexion_db = sqlite3.connect(
        BASE_DATOS
    )

    cursor = conexion_db.cursor()

    cursor.execute(
        """
        SELECT
            fecha,
            hora,
            ax,
            ay,
            az,
            vibracion,
            estado

        FROM mediciones
        """
    )

    registros = cursor.fetchall()

    conexion_db.close()

    with open(
        archivo,
        "w",
        newline="",
        encoding="utf-8"
    ) as archivo_csv:

        escritor = csv.writer(
            archivo_csv
        )

        escritor.writerow([
            "Fecha",
            "Hora",
            "X",
            "Y",
            "Z",
            "Vibracion",
            "Estado"
        ])

        escritor.writerows(
            registros
        )

    messagebox.showinfo(
        "Exportación",
        "Datos exportados correctamente."
    )


# =========================================================
# CERRAR
# =========================================================

def cerrar():

    global ejecutando

    ejecutando = False

    if conexion:

        conexion.close()

    ventana.destroy()


# =========================================================
# CREAR BASE
# =========================================================

crear_base_datos()


# =========================================================
# VENTANA
# =========================================================

ventana = tk.Tk()

ventana.title(
    "Sistema Universitario de Monitoreo Sísmico"
)

ventana.geometry(
    "1200x800"
)

ventana.protocol(
    "WM_DELETE_WINDOW",
    cerrar
)


# =========================================================
# TITULO
# =========================================================

tk.Label(
    ventana,
    text="SISTEMA DE MONITOREO SÍSMICO",
    font=("Arial", 24, "bold")
).pack(pady=10)


tk.Label(
    ventana,
    text="ESP32 + MPU6050 + Python + SQLite",
    font=("Arial", 12)
).pack()


# =========================================================
# ESTADO
# =========================================================

etiqueta_estado = tk.Label(
    ventana,
    text="● SISTEMA INICIADO",
    font=("Arial", 18, "bold")
)

etiqueta_estado.pack(
    pady=10
)


etiqueta_conexion = tk.Label(
    ventana,
    text="● ESP32 DESCONECTADO",
    font=("Arial", 10)
)

etiqueta_conexion.pack()


# =========================================================
# DATOS
# =========================================================

marco_datos = tk.Frame(
    ventana
)

marco_datos.pack(
    pady=15
)


def crear_indicador(
    nombre,
    columna
):

    marco = tk.Frame(
        marco_datos,
        relief="groove",
        borderwidth=2,
        padx=25,
        pady=10
    )

    marco.grid(
        row=0,
        column=columna,
        padx=8
    )

    tk.Label(
        marco,
        text=nombre,
        font=("Arial", 10, "bold")
    ).pack()

    valor = tk.Label(
        marco,
        text="0.000",
        font=("Arial", 15)
    )

    valor.pack()

    return valor


valor_ax = crear_indicador(
    "Aceleración X",
    0
)

valor_ay = crear_indicador(
    "Aceleración Y",
    1
)

valor_az = crear_indicador(
    "Aceleración Z",
    2
)

valor_vibracion = crear_indicador(
    "Vibración",
    3
)


# =========================================================
# GRÁFICA
# =========================================================

figura = Figure(
    figsize=(8, 4)
)

grafica = figura.add_subplot(111)

canvas = FigureCanvasTkAgg(
    figura,
    master=ventana
)

canvas.get_tk_widget().pack(
    fill="both",
    expand=True,
    padx=20
)


# =========================================================
# BOTONES
# =========================================================

marco_botones = tk.Frame(
    ventana
)

marco_botones.pack(
    pady=10
)


boton_conectar = tk.Button(
    marco_botones,
    text="CONECTAR ESP32",
    command=conectar,
    font=("Arial", 11, "bold"),
    padx=15
)

boton_conectar.grid(
    row=0,
    column=0,
    padx=5
)


tk.Button(
    marco_botones,
    text="REINICIAR ALARMA",
    command=reiniciar_alarma,
    font=("Arial", 11, "bold"),
    padx=15
).grid(
    row=0,
    column=1,
    padx=5
)


tk.Button(
    marco_botones,
    text="EXPORTAR CSV",
    command=exportar_csv,
    font=("Arial", 11, "bold"),
    padx=15
).grid(
    row=0,
    column=2,
    padx=5
)


# =========================================================
# REGISTRO
# =========================================================

tk.Label(
    ventana,
    text="Registro de eventos",
    font=("Arial", 11, "bold")
).pack()


lista_eventos = tk.Listbox(
    ventana,
    height=5,
    width=120
)

lista_eventos.pack(
    padx=20,
    pady=5
)


# =========================================================
# INICIO
# =========================================================

registrar_evento(
    "Sistema iniciado"
)

ventana.mainloop()

