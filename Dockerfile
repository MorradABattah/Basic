FROM python:3.9-slim-buster
WORKDIR /app
ADD . /app
RUN pip install --no-cache-dir flask
EXPOSE 80
CMD ["python", "app.py"]
