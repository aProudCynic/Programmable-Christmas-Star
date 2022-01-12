from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

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
def loop_light_programme(light_programme_name: str):
    light_programme = light_controller.get_light_programme_by(light_programme_name)
    light_controller.start_loop(light_programme)


@app.post("/stop")
def stop_light_programme():
    light_controller.stop()


@app.get("/light_programmes")
def get_light_programmes():
    return light_controller.get_light_programmes()
