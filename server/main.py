from fastapi import (
    FastAPI,
    Request,
)
from fastapi.middleware.cors import CORSMiddleware

from json.decoder import JSONDecodeError

from controller.blinkt.blinkt_controller import BlinktController

app = FastAPI()

origins = [
    "*",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

light_controller = BlinktController()


@app.post("/loop/{light_programme_name}")
async def loop_light_programme(light_programme_name: str, request: Request):
    light_programme = light_controller.get_light_programme_by(light_programme_name)
    try:
        parameters = await request.json()
    except JSONDecodeError as json_error:
        parameters = None
    light_controller.start_loop(light_programme, parameters)


@app.post("/stop")
def stop_light_programme():
    light_controller.stop_loop()


@app.get("/light_programmes")
def get_light_programmes():
    return light_controller.get_light_programmes()
