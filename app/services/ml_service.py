import mlflow
import pandas as pd
from fastapi import HTTPException
from app.models.gun_model import GunFeatures

#configuracion del mlflow usando ,a IP deL por el que corre el servicio Mlflow
MLFLOW_TRACRING_URI = "http://172.20.0.3:5000"

RUN_ID = "e109ccfd52c4440681e9f4f4453a1bad"
MODEL_URI = f"runs:/{RUN_ID}/modelo_clasificacion_armas"

class MLService:
    def __init__(self):
        mlflow.set_tracking_uri(MLFLOW_TRACRING_URI)

        try: 
            self.modelo = mlflow.pyfunc.load_model(MODEL_URI)
            print("modelo cargado exitosamente")
        except Exception as e:
            print(f"Error al cargar el modelo: {e}")
            self.modelo = None

    def predict_weapon(self, features: GunFeatures) -> str:
        if self.modelo is None:
            raise HTTPException(status_code=503, detail="El modelo de ML no es ta disponible por el momento")
        try:
            datos_dict= features.model_dump()
            input_df = pd.DataFrame([datos_dict])

            prediccion = self.modelo.predict(input_df)

            clase_numero= str(prediccion[0])

            mapa_clases = {
                "0": "Ametralladora Ligera",
                "1": "Escopeta",
                "2": "Francotirador",
                "3": "Pistola",
                "4": "Rifle de asalto", # Ojo aquí, en tu CSV tiene mayúscula, pero Pydantic lo pide con minúscula
                "5": "Rifle de Tirador",
                "6": "Subfusil"
            }
            clase_resultante = mapa_clases.get(clase_numero, "Deconocido")

            return clase_resultante
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error interno durante la prediccion: {str(e)}")


ml_service = MLService()