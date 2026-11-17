from pydantic import BaseModel, Field, ConfigDict
from typing import Literal

#CONFIGURACIÓN BASE(DRY)
class BaseGunFeatures(BaseModel):
    """
    Clase base para heredar configuraciones de seguridad a todos los modelos.
    - extra="forbid": Rechaza cualquier campo que no esté definido aquí.
    - str_strip_whitespace: Elimina espacios en blanco al inicio y al final.
    """
    model_config=ConfigDict(
        extra="forbid",
        str_strip_whitespace=True
    )


class GunFeatures(BaseGunFeatures):
    model_config = ConfigDict(allow_inf_nan=False)

    ttk_0_10m_ms: float = Field(..., ge=0, le=5000, description="Time to Kill a 10m (ms)")
    cadencia_rpm: float = Field(..., gt=0, le=1500, description="Cadencia de disparo (RPM)")
    velocidad_bala_ms: float = Field(..., gt=0, le=2000, description="Velocidad de la bala (m/s)")
    ads_ms: float = Field(..., gt=0, le=1000, description="Tiempo de apuntado (ms)")
    recarga_ms: float = Field(..., gt=0, le=10000, description="Tiempo de recarga (ms)")
    alcance_efectivo_m: float = Field(..., gt=0, le=200, description="Alcance efectivo (metros)")
    retroceso_vertical: float = Field(...,ge=0.0, le=200,  description="Control de retroceso vertical")


class GunPrediction(BaseModel):
    clase_predicha: Literal["Ametralladora Ligera",
            "Escopeta",
            "Francotirador",
            "Pistola",
            "Rifle de asalto", 
            "Rifle de Tirador",
            "Subfusil"]