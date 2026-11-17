from fastapi import APIRouter
from app.models.gun_model import GunFeatures, GunPrediction
from app.services.ml_service import ml_service

router = APIRouter(prefix="/api/v1/armas", tags=["clasificacion de armas"])

@router.post("/clasificar", response_model=GunPrediction)
def clasificar_arma(features: GunFeatures):
    """
        Recibe las estadisticas de una arma y predice a que clase pertenece
    """
    clase_calculada = ml_service.predict_weapon(features)
    return GunPrediction(clase_predicha=clase_calculada)
