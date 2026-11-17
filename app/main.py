from fastapi import FastAPI
from app.routers import gun_route

app = FastAPI(
    title ="Clasificador de armas WZ",
    description="Modelo de IA ",
    version="1.3.0"
)

app.include_router(gun_route.router)

@app.get("/")
async def root():
    return {"message":"todo bien ve a la documentacion del proyecto para probar"}

