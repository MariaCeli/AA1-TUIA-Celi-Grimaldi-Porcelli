# Predicción de lluvia en Australia - MLOps con Docker

Este módulo permite ejecutar inferencias sobre nuevos datos usando el modelo entrenado de regresión logística, empaquetado en un contenedor Docker.

---

## Estructura del repositorio

AA1-TUIA-Apellido1-Apellido2-Apellido3/
├── TP-clasificacion-AA1.ipynb
├── weatherAUS.csv
├── docker/
│ ├── inference.py
│ ├── pipeline.pkl
│ ├── requirements.txt
│ ├── Dockerfile
│ └── readme.md
├── files/
│ ├── input.csv
│ └── output.csv

## Requisitos

- Docker instalado y funcionando
- Crear carpeta `files/` con un archivo `input.csv` que tenga las columnas esperadas por el modelo

---

## Instrucciones de uso

### 1. Construir la imagen Docker

Desde la raíz del proyecto:

```bash
docker build -t lluvia-predictor ./docker´´´´

2. Ejecutar el contenedor

docker run --rm -v $(pwd)/files:/files lluvia-predictor

winpty docker run --rm -v "/$(pwd | sed 's|/|\\|g' | sed 's|\\c|C:|')/files:/files" lluvia-predictor

Entrada esperada (input.csv)

El archivo files/input.csv debe contener las siguientes columnas:

MinTemp, MaxTemp, Evaporation, Sunshine, WindGustSpeed, WindSpeed9am, WindSpeed3pm,
Humidity9am, Humidity3pm, Pressure9am, Pressure3pm, Cloud9am, Cloud3pm, Temp9am, Temp3pm,
Estacion_invierno, Estacion_otoño, Estacion_primavera, Estacion_verano,
Direccion_viento_C, Direccion_viento_E, Direccion_viento_N, Direccion_viento_O, Direccion_viento_S,
Tipo_lluvia_Fuerte, Tipo_lluvia_Leve, Tipo_lluvia_Moderada, Tipo_lluvia_Ninguna,
Region_Este, Region_Norte, Region_Oeste, Region_Sur,
RainToday_No, RainToday_Yes,
WindDir9am_C, WindDir9am_E, WindDir9am_N, WindDir9am_O, WindDir9am_S,
WindDir3pm_C, WindDir3pm_E, WindDir3pm_N, WindDir3pm_O, WindDir3pm_S

Salida esperada (output.csv)

El contenedor genera un archivo files/output.csv con la predicción del modelo:

RainTomorrow_pred
No
Yes
No
...

Notas finales
El modelo fue entrenado con regresión logística y preprocesamiento (StandardScaler)

Debido al desbalance del dataset y el umbral predeterminado (0.5), es posible que las predicciones tiendan a "No"

A futuro se puede ajustar el umbral de decisión o aplicar técnicas de rebalanceo

Estado del modelo
Modelo: LogisticRegression entrenado con validación cruzada

Entrenado sobre variables numéricas y categóricas dummificadas

Serializado como pipeline.pkl y empaquetado en contenedor Docker