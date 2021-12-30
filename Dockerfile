FROM python:2.7-alpine
WORKDIR /opt/montlhery
COPY requirements.txt .
COPY montlhery.py montlhery
RUN pip install --requirement requirements.txt
ENTRYPOINT ["python", "montlhery"]
