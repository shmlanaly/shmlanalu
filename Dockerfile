# استخدام نسخة بايثون حديثة تتوافق مع متطلبات yt-dlp
FROM python:3.10-bullseye

# تحديث النظام وتثبيت الأدوات الضرورية
RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y ffmpeg git python3-pip

# تجهيز مجلد العمل
COPY . /app
WORKDIR /app

# تحديث pip وتثبيت المكتبات
RUN pip3 install --upgrade pip
RUN pip3 install --no-cache-dir -r requirements.txt

# أمر التشغيل
CMD ["python3", "-m", "zira"]
