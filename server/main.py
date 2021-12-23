from fastapi import FastAPI
from controller.star_controller import StarController
import controller.snippets as snippets

app = FastAPI()

star_controller = StarController()

@app.post("/loop/{snippet_name}")
def loop_snippet(snippet_name: str):
    snippet = getattr(snippets, snippet_name)
    star_controller.start_loop(snippet)

@app.post("/stop")
def stop():
    star_controller.stop()
