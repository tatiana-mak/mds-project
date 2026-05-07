from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 

app = FastAPI()

app.add_middleware (
        CORSMiddleware,
        allow_origins = ["*"],
        allow_methods = ["*"],
)

class RollParams(BaseModel):
    temperature: float
    speed: float


@app.get("/standards")
def get_standards():
    return {
        "temperature_min": 950,
        "temperature_max": 1100,
        "speed_min": 5,
        "speed_max": 15

    }

@app.post("/check")
def check_quality(par: RollParams):
    if par.temperature >= 950 and par.temperature <= 1100:
        temp_ok = True
    else:
        temp_ok = False
    if par.speed >= 5 and par.speed <= 15:
        speed_ok = True
    else:
        speed_ok = False
    if temp_ok == True and speed_ok == True:
        quality = "Годен"
    else:
        quality = "Брак"
    return{
        "quality": quality,
        "temp_ok": temp_ok,
        "speed_ok": speed_ok
    }
    

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host = "0.0.0.0", port = 8080)