from fastapi import FastAPI
from controller.star_controller import StarController
from service.explode import explode

app = FastAPI()

star_controller = StarController()

@app.get("/explode/")
def initiate_explode():
    star_controller.start_loop(explode)

@app.get("/stop/")
def stop():
    star_controller.stop()
