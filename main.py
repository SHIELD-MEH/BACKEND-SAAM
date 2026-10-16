from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Bienvenidos al Backend de SAAM"}