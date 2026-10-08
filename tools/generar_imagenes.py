"""Genera las imágenes del README con estética de terminal de fósforo ámbar.

Crea el bloque About Me y la tabla de competencias (pip list). Ambas comparten
el mismo postproceso CRT: brillo, halo, scanlines, viñeta y grano con semilla fija.

Uso: python tools/generar_imagenes.py
Requiere Pillow, NumPy y la fuente Cascadia Mono (incluida en Windows 11).
"""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

RAIZ = Path(__file__).resolve().parent.parent
RUTA_FUENTE = Path("C:/Windows/Fonts/CascadiaMono.ttf")
SEMILLA = 42

# Escala 2x para que se vea nítida en pantallas de alta densidad
ANCHO = 1896
ALTO_BARRA = 52
MARGEN = 56

# Paleta: ámbar del perfil, crema para los valores y un verde de fósforo para el estado
NEGRO = (6, 5, 3)
AMBAR = (255, 176, 0)
AMBAR_TENUE = (122, 86, 14)
# Las barras de competencias son bloques contiguos: con el brillo encima, el ámbar puro
# se satura a amarillo, así que necesitan un tono más bajo
AMBAR_BARRA = (150, 92, 0)
AMBAR_APAGADO = (58, 42, 8)
CREMA = (243, 234, 211)
GRIS = (150, 140, 120)
VERDE = (110, 240, 150)
BARRA = (226, 220, 206)
BORDE = (70, 66, 58)

USUARIO = "sysop@gabriel.caruso"

FILAS_PERFIL = [
    ("NAME", "Ramiro \"Gabriel\" Caruso", CREMA),
    ("CLASS", "Junior Data Scientist · Data Analyst", CREMA),
    ("STATUS", "Available for hire", VERDE),
    ("NODE", "Oviedo, Asturias (ES) · remote-friendly", CREMA),
    ("EXP", "9y customer service → self-taught → DS & AI Bootcamp", CREMA),
    ("CORE MODULES", "Python · Pandas · SQL · scikit-learn · Databricks", CREMA),
    ("LEARNING", "Azure Databricks", CREMA),
    ("BACKGROUND PROC", "Writer · 2D artist · Twitch Content Creator", CREMA),
    ("CURRENT BUILD", "Telco churn · Databricks + MLflow", AMBAR),
]

# Paquete, nivel sobre 8 y etiqueta
FILAS_COMPETENCIAS = [
    ("python", 7, "solid"),
    ("pandas · numpy", 7, "solid"),
    ("scikit-learn", 7, "solid"),
    ("sql", 7, "solid"),
    ("git · github", 6, "daily driver"),
    ("azure", 5, "in use"),
    ("databricks", 3, "learning"),
]


def cargar_fuente(tamano, peso):
    """Carga Cascadia Mono con el peso indicado (fuente variable)."""
    fuente = ImageFont.truetype(str(RUTA_FUENTE), tamano)
    try:
        fuente.set_variation_by_axes([peso])
    except OSError:
        pass
    return fuente


def dibujar_prompt(dibujo, x, y, comando, fuente):
    """Dibuja el prompt con el usuario en ámbar y el comando en crema. Devuelve la x final."""
    dibujo.text((x, y), USUARIO, font=fuente, fill=AMBAR, anchor="lm")
    x_resto = x + dibujo.textlength(USUARIO, font=fuente)
    texto_resto = ":~$ " + comando
    dibujo.text((x_resto, y), texto_resto, font=fuente, fill=CREMA, anchor="lm")
    return x_resto + dibujo.textlength(texto_resto, font=fuente)


def dibujar_cursor(dibujo, x, y):
    """Dibuja un cursor de bloque centrado verticalmente en y."""
    dibujo.rectangle([x, y - 20, x + 18, y + 20], fill=AMBAR)


def dibujar_barra(dibujo, titulo, fuente):
    """Dibuja la barra de título de la ventana, igual que la del header."""
    dibujo.rectangle([0, 0, ANCHO, ALTO_BARRA], fill=BARRA)
    dibujo.text((18, ALTO_BARRA // 2), titulo, font=fuente, fill=NEGRO, anchor="lm")
    dibujo.text((ANCHO // 2, ALTO_BARRA // 2), "<O>", font=fuente, fill=NEGRO, anchor="mm")
    dibujo.text((ANCHO - 18, ALTO_BARRA // 2), "—□X", font=fuente, fill=NEGRO, anchor="rm")


def aplicar_crt(capa, titulo_ventana):
    """Convierte la capa de texto sobre negro en una pantalla CRT con barra de título."""
    ancho, alto = capa.size
    texto = np.asarray(capa, dtype=np.float32)

    # Brillo de fósforo: dos desenfoques sumados al texto original
    brillo_cercano = np.asarray(capa.filter(ImageFilter.GaussianBlur(6)), dtype=np.float32)
    brillo_lejano = np.asarray(capa.filter(ImageFilter.GaussianBlur(22)), dtype=np.float32)

    # Fondo: negro cálido con un halo ámbar suave arriba a la izquierda
    filas_y, columnas_x = np.mgrid[0:alto, 0:ancho].astype(np.float32)
    distancia_halo = np.sqrt(((columnas_x - ancho * 0.25) / ancho) ** 2 + ((filas_y - alto * 0.3) / alto) ** 2)
    halo = np.clip(1.0 - distancia_halo * 1.6, 0.0, 1.0) ** 2
    tinte_halo = [34.0, 22.0, 4.0]
    fondo = np.zeros((alto, ancho, 3), dtype=np.float32)
    for canal in range(3):
        fondo[:, :, canal] = NEGRO[canal] + halo * tinte_halo[canal]

    imagen = fondo + texto + brillo_cercano * 0.8 + brillo_lejano * 0.5

    # Scanlines: una línea más oscura cada 4 píxeles
    mascara_scan = np.ones((alto, 1, 1), dtype=np.float32)
    mascara_scan[::4] = 0.82
    imagen = imagen * mascara_scan

    # Viñeta para curvar visualmente la pantalla
    distancia_centro = np.sqrt(((columnas_x - ancho / 2) / (ancho / 2)) ** 2 + ((filas_y - alto / 2) / (alto / 2)) ** 2)
    vineta = np.clip(1.0 - 0.28 * distancia_centro ** 2, 0.0, 1.0)
    imagen = imagen * vineta[:, :, None]

    # Grano monocromo con semilla fija para que el resultado sea reproducible
    generador = np.random.default_rng(SEMILLA)
    grano = generador.normal(0.0, 12.0, size=(alto, ancho, 1)).astype(np.float32)
    imagen = imagen + grano

    imagen = np.clip(imagen, 0, 255).astype(np.uint8)
    resultado = Image.fromarray(imagen, mode="RGB")

    # La barra de título se dibuja al final para que quede limpia, como en el header
    dibujo = ImageDraw.Draw(resultado)
    dibujar_barra(dibujo, titulo_ventana, cargar_fuente(30, 600))
    dibujo.rectangle([0, 0, ancho - 1, alto - 1], outline=BORDE, width=2)
    return resultado


def guardar(imagen, nombre):
    """Guarda en JPEG: con el grano, un PNG pesaría varios MB."""
    imagen.save(RAIZ / nombre, quality=90, optimize=True, progressive=True, subsampling=0)


def dibujar_tabla(dibujo, y_tabla, alto_tabla, x_columna, cabeceras, fuente):
    """Dibuja el marco de una tabla de dos columnas con su cabecera. Devuelve la y de la primera fila."""
    alto_cabecera = 78
    x_tabla = MARGEN
    x_fin = ANCHO - MARGEN
    y_fin = y_tabla + alto_tabla
    dibujo.rectangle([x_tabla, y_tabla, x_fin, y_fin], outline=AMBAR_TENUE, width=2)
    dibujo.line([x_columna, y_tabla, x_columna, y_fin], fill=AMBAR_TENUE, width=2)
    y_separador = y_tabla + alto_cabecera
    dibujo.line([x_tabla, y_separador, x_fin, y_separador], fill=AMBAR_TENUE, width=2)

    y_centro = y_tabla + alto_cabecera // 2
    dibujo.text((x_tabla + 32, y_centro), cabeceras[0], font=fuente, fill=GRIS, anchor="lm")
    dibujo.text((x_columna + 32, y_centro), cabeceras[1], font=fuente, fill=GRIS, anchor="lm")
    return y_separador + 12


def generar_about_me():
    """Tabla de perfil: nombre, rol, estado, ubicación y proyecto actual."""
    fuente_texto = cargar_fuente(36, 350)
    fuente_prompt = cargar_fuente(34, 500)

    alto_fila = 70
    y_prompt = ALTO_BARRA + 56
    y_tabla = y_prompt + 64
    alto_tabla = 78 + alto_fila * len(FILAS_PERFIL) + 24
    alto = y_tabla + alto_tabla + 112
    x_columna = MARGEN + 470

    capa = Image.new("RGB", (ANCHO, alto), (0, 0, 0))
    dibujo = ImageDraw.Draw(capa)
    dibujar_prompt(dibujo, MARGEN, y_prompt, "cat profile.md", fuente_prompt)
    y_inicio = dibujar_tabla(dibujo, y_tabla, alto_tabla, x_columna, ("PROPERTY", "VALUE"), fuente_texto)

    y_fila = y_inicio + alto_fila // 2
    for clave, valor, color in FILAS_PERFIL:
        dibujo.text((MARGEN + 32, y_fila), clave, font=fuente_texto, fill=AMBAR, anchor="lm")
        x_valor = x_columna + 32
        if clave == "STATUS":
            radio = 9
            x_punto = x_valor + radio
            dibujo.ellipse([x_punto - radio, y_fila - radio, x_punto + radio, y_fila + radio], fill=VERDE)
            x_valor = x_punto + radio + 18
        dibujo.text((x_valor, y_fila), valor, font=fuente_texto, fill=color, anchor="lm")
        if clave == "STATUS":
            dibujar_cursor(dibujo, x_valor + dibujo.textlength(valor + " ", font=fuente_texto), y_fila)
        y_fila = y_fila + alto_fila

    y_pie = y_tabla + alto_tabla + 56
    x_pie = dibujar_prompt(dibujo, MARGEN, y_pie, "", fuente_prompt)
    dibujar_cursor(dibujo, x_pie, y_pie)

    guardar(aplicar_crt(capa, "PROFILE.md"), "about_me.jpg")


def generar_competencias():
    """Tabla de competencias con barras de 8 segmentos, como la salida de pip list."""
    fuente_texto = cargar_fuente(36, 350)
    fuente_prompt = cargar_fuente(34, 500)

    alto_fila = 70
    y_prompt = ALTO_BARRA + 56
    y_tabla = y_prompt + 64
    alto_tabla = 78 + alto_fila * len(FILAS_COMPETENCIAS) + 24
    alto = y_tabla + alto_tabla + 112
    x_columna = MARGEN + 470

    capa = Image.new("RGB", (ANCHO, alto), (0, 0, 0))
    dibujo = ImageDraw.Draw(capa)
    dibujar_prompt(dibujo, MARGEN, y_prompt, "pip list --core", fuente_prompt)
    y_inicio = dibujar_tabla(dibujo, y_tabla, alto_tabla, x_columna, ("PACKAGE", "PROFICIENCY"), fuente_texto)

    ancho_segmento = 44
    hueco = 8
    alto_segmento = 34
    y_fila = y_inicio + alto_fila // 2
    for paquete, nivel, etiqueta in FILAS_COMPETENCIAS:
        dibujo.text((MARGEN + 32, y_fila), paquete, font=fuente_texto, fill=AMBAR, anchor="lm")
        x_segmento = x_columna + 32
        for indice in range(8):
            if indice < nivel:
                color = AMBAR_BARRA
            else:
                color = AMBAR_APAGADO
            dibujo.rectangle(
                [x_segmento, y_fila - alto_segmento // 2, x_segmento + ancho_segmento, y_fila + alto_segmento // 2],
                fill=color,
            )
            x_segmento = x_segmento + ancho_segmento + hueco
        color_etiqueta = CREMA
        if etiqueta == "learning":
            color_etiqueta = VERDE
        dibujo.text((x_segmento + 32, y_fila), etiqueta, font=fuente_texto, fill=color_etiqueta, anchor="lm")
        y_fila = y_fila + alto_fila

    y_pie = y_tabla + alto_tabla + 56
    x_pie = dibujar_prompt(dibujo, MARGEN, y_pie, "", fuente_prompt)
    dibujar_cursor(dibujo, x_pie, y_pie)

    guardar(aplicar_crt(capa, "TERMINAL"), "skills.jpg")


def main():
    generar_about_me()
    generar_competencias()


if __name__ == "__main__":
    main()
