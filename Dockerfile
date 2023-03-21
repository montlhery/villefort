FROM python:2.7-alpine
WORKDIR /opt/villefort
COPY requirements.txt villefort.py .
RUN pip install --requirement requirements.txt
ENTRYPOINT ["python", "villefort.py"]
