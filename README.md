# Buscador de Clima con Flask

## Descripción

Aplicación web desarrollada con **Python y Flask** que permite consultar el clima actual de cualquier ciudad utilizando la **API de OpenWeatherMap**.
La aplicación muestra información meteorológica relevante como temperatura, sensación térmica, humedad, viento, presión atmosférica, visibilidad y nubosidad, además del ícono del clima y la bandera del país.

---

## Requisitos

Antes de ejecutar el proyecto se necesita:

* Python 3.8 o superior
* pip
* Conexión a internet
* Una API Key de OpenWeatherMap

---

## Instalación

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/clima-flask.git
```

2. Entrar a la carpeta del proyecto:

```bash
cd clima-flask
```

3. Instalar las dependencias necesarias:

```bash
pip install flask requests
```

---

## Configuración

La aplicación utiliza una **API Key de OpenWeatherMap** que debe guardarse en una variable de entorno.

### En Windows

```bash
set OPENWEATHER_KEY=tu_api_key
```

### En Linux / Mac

```bash
export OPENWEATHER_KEY=tu_api_key
```

---

## Ejecución

Para iniciar la aplicación ejecuta:

```bash
python clima.py
```

Después abre tu navegador en:

```
http://localhost:5000
```

---

## Uso

1. Escribe el nombre de una ciudad en el campo de búsqueda.
2. Presiona el botón **Buscar**.
3. La aplicación mostrará el clima actual de la ciudad seleccionada.

---

## Tecnologías utilizadas

* Python
* Flask
* Requests
* HTML
* CSS
* API OpenWeatherMap

---

## Autor

Proyecto académico desarrollado como práctica de **consumo de APIs REST con Flask**.
