import io
import os

import cv2
import numpy as np
import pytesseract
from fastapi import FastAPI, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from starlette.requests import Request
from starlette.responses import Response


TESSERACT_PATH = "/usr/bin/tesseract"
LANGUAGE_MODEL_DIR = os.path.join(os.getcwd(), "data")


def read_img(img):
    pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH
    text = pytesseract.image_to_string(img)
    return text


app = FastAPI()


class Translate(BaseModel):
    text: str


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/ping/")
def ping(request: Request):
    return True


@app.post("/predict/")
def prediction(request: Request, file: bytes = File(...)):
    if request.method == "POST":
        image_stream = io.BytesIO(file)
        image_stream.seek(0)
        file_bytes = np.asarray(bytearray(image_stream.read()), dtype=np.uint8)
        frame = cv2.imdecode(file_bytes, cv2.IMREAD_COLOR)
        label = read_img(frame)
        return label.strip()
    return Response(status_code=400)
