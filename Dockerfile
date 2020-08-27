FROM python:3.8-alpine
RUN apk add build-base
ADD requirements.txt .
RUN pip install -r requirements.txt
RUN mkdir -p app
WORKDIR /app
ADD bot /app
RUN ls
CMD ["python", "/app/main.py"]