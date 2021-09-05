FROM python:3.9
RUN apt-get update -y
RUN apt update && apt install -y libsm6 libxext6 libgl1-mesa-dev
RUN apt-get -y install tesseract-ocr
RUN pip install poetry

COPY . /app
WORKDIR /app
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev
CMD ["./start.sh"]
