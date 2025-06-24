import joblib
import pandas as pd
import logging
from sys import stdout
import warnings

warnings.simplefilter('ignore')

# Logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
formatter = logging.Formatter("%(asctime)s %(levelname)s %(message)s")
ch = logging.StreamHandler(stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)

# Cargar modelo
pipeline = joblib.load('pipeline.pkl')
logger.info("Modelo cargado.")

# Cargar input
df_input = pd.read_csv('/files/input.csv')
df_input = df_input.select_dtypes(include=['number'])  # usar solo numéricas
logger.info("Input cargado.")

# Predecir
pred = pipeline.predict(df_input)
logger.info("Predicción realizada.")

# Guardar output
pd.DataFrame(pred, columns=["RainTomorrow_pred"]).to_csv('/files/output.csv', index=False)
logger.info("Resultado guardado.")

print("Predicciones completadas")
