from fastapi import FastAPI
from controller.star_controller import StarController
import controller.light_programmes as light_programmes
from inspect import getmembers, isfunction

app = FastAPI()

star_controller = StarController()

@app.post("/loop/{light_programme_name}")
def loop_snippet(light_programme_name: str):
    snippet = getattr(light_programmes, light_programme_name)
    star_controller.start_loop(snippet)

@app.post("/stop")
def stop():
    star_controller.stop()

@app.get("/light_programmes")
def get_snippets():
    function_tuples = getmembers(light_programmes, isfunction)
    return [function_tuple[0] for function_tuple in function_tuples]
