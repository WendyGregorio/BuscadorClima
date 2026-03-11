import os
import requests
import webbrowser
from threading import Timer
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configuración de la API OpenWeatherMap
# La API key se obtiene de una variable de entorno como se solicitó
API_KEY = os.environ.get("OPENWEATHER_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def open_browser():
    """Abre el navegador automáticamente al iniciar el servidor."""
    webbrowser.open_new("http://127.0.0.1:5000/")

@app.route("/")
def index():
    """Muestra la página principal con el formulario de búsqueda."""
    return render_template("index.html")

@app.route("/resultado", methods=["POST"])
def resultado():
    """Consume la API de OpenWeatherMap y muestra los resultados."""
    ciudad = request.form.get("ciudad")
    
    if not ciudad:
        return redirect(url_for("index"))

    # Parámetros para la API: ciudad, unidades métricas y lenguaje español
    params = {
        "q": ciudad,
        "appid": API_KEY,
        "units": "metric",
        "lang": "es"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        
        # Verificar el código de estado HTTP antes de procesar
        if response.status_code == 200:
            data = response.json()
            
            # Mapeo de datos solicitados
            clima = {
                "ciudad": data["name"],
                "pais": data["sys"]["country"].lower(),
                "temp": data["main"]["temp"],
                "sensacion": data["main"]["feels_like"],
                "min": data["main"]["temp_min"],
                "max": data["main"]["temp_max"],
                "humedad": data["main"]["humidity"],
                "presion": data["main"]["pressure"],
                "viento": round(data["wind"]["speed"] * 3.6, 2),  # m/s a km/h
                "visibilidad": data.get("visibility", 0) / 1000,   # m a km
                "nubes": data["clouds"]["all"],
                "icono": data["weather"][0]["icon"],
                "icono_base": data["weather"][0]["icon"][:2], # Código base (01, 02, etc.)
                "descripcion": data["weather"][0]["description"],
                "clima_principal": data["weather"][0]["main"].lower()
            }
            
            return render_template("resultado.html", clima=clima)
        else:
            # Si la ciudad no existe o hay error de API
            return render_template("error.html", mensaje="No pudimos encontrar la ciudad solicitada.")
            
    except Exception as e:
        print(f"Error consultando la API: {e}")
        return render_template("error.html", mensaje="Ocurrió un error inesperado al consultar el clima.")

if __name__ == "__main__":
    if not API_KEY:
        print("ADVERTENCIA: La variable de entorno OPENWEATHER_KEY no está definida.")
    
    # Programar la apertura del navegador 1 segundo después de iniciar
    Timer(1, open_browser).start()
    
    # El servidor Flask debe ejecutarse en el puerto 5000
    app.run(host="127.0.0.1", port=5000, debug=True)
