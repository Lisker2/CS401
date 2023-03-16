FROM python:3.9-slim-bullseye


COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . /opt

CMD ["sh","-c","python3", "/opt/app.py"]