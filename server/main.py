from fastapi import FastAPI
from controller.star_controller import StarController
from fastapi.middleware.cors import CORSMiddleware

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

light_controller = StarController()


@app.post("/loop/{light_programme_name}")
def loop_snippet(light_programme_name: str):
    snippet = getattr(light_programmes, light_programme_name)
    light_controller.start_loop(snippet)


@app.post("/stop")
def stop():
    light_controller.stop()


@app.get("/light_programmes")
def get_snippets():
    return light_controller.get_light_programmes()
