FROM python:3.9-bullseye

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg git

COPY . /app
WORKDIR /app

RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

CMD ["python3", "-m", "zira"]
