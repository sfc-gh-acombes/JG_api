FROM python:3.8
COPY ./requirements.txt /requirements.txt
COPY ./app app
RUN pip install -r requirements.txt

COPY ./.secrets/SERV_API_key.p8 /SERV_API_key.p8

WORKDIR app
CMD ngrok-asgi uvicorn app:app --host 0.0.0.0 --port $PORT --log-level debug
