import os
import glob
import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.responses import RedirectResponse
from cnn_process import read_image, predicts
from esp_process import predictx

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")


@app.get("/docs", include_in_schema=False)
async def docs():
    return RedirectResponse(url="/docs")


@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("home.html", context)


@app.get("/contact", response_class=HTMLResponse)
async def test_page(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("contact.html", context)


@app.get("/knn", response_class=HTMLResponse)
async def test_page(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("knn.html", context)


# @app.get("/esp", response_class=HTMLResponse)
# async def test_page(request: Request):
#     context = {
#         "request": request,
#     }
#     return templates.TemplateResponse("esp.html", context)


@app.get("/cnn", response_class=HTMLResponse)
async def cnn_page(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("cnn.html", context)


@app.post('/cnn')
async def predict_cnn(request: Request, file: UploadFile = File(...)):
    extension = file.filename.split(".")[-1] in ("jpg", "jpeg", "png")
    if not extension:
        return "Image must be jpg or png format!"
    image = read_image(await file.read())
    prediction = predicts(image)
    context = {
        "request": request,
        "image": image,
        "predictions": prediction,

    }
    return templates.TemplateResponse("cnn.html", context)


@app.post('/esp')
async def image_esp(request: Request):
    list_of_files = glob.glob('static/uploads/*')
    latest_file = max(list_of_files, key=os.path.getctime)
    prediction = predictx(latest_file)
    context = {
        "request": request,
        "latest_image": latest_file,
        "predictions": prediction
    }
    return templates.TemplateResponse("esp.html", context)


@app.get("/esp", response_class=HTMLResponse)
async def test_page(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("esp.html", context)


if __name__ == "__main__":
    uvicorn.run(app, debug=True)
