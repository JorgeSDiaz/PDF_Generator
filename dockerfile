FROM ubuntu:20.04

RUN apt-get update && apt-get install -y python3 python3-pip wget

RUN wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6-1/wkhtmltox_0.12.6-1.focal_and64.deb
RUN apt install -y ./wkhtmltox_0.12.6-1.focal_and64.deb

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
