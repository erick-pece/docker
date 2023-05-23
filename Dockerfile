FROM python:3.8-slim-buster
WORKDIR /container_task
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000
ENV FLASK_APP="app.py"

COPY . .
CMD ["flask", "run","--host=0.0.0.0"]