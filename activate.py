import webbrowser
import time

import streamlit as st
def ejecutar_sitio_web(url, intervalo):
    """
    Abre un sitio web en el navegador predeterminado cada cierto tiempo.

    Args:
        url (str): La URL del sitio web que se desea abrir.
        intervalo (int): Intervalo en segundos entre cada apertura del sitio.
    """
    try:
        st.header("Bot test")
        st.write(f"Iniciando apertura del, sitio web: {url} cada {intervalo} segundos.")
        print(f"Iniciando apertura del, sitio web: {url} cada {intervalo} segundos. Presiona Ctrl+C para detener.")
        while True:
            webbrowser.open(url)
            time.sleep(intervalo)
            
    except KeyboardInterrupt:
        print("\nEjecución detenida por el usuario.")

# Configura la URL del sitio web y el intervalo de tiempo
url_sitio = "https://allquwebservices.onrender.com"
intervalo_segundos = 90  # Cambia esto al intervalo deseado en segundos

ejecutar_sitio_web(url_sitio, intervalo_segundos)
