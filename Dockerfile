FROM python:3.8.1
WORKDIR /app
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD src/main.py src/models.py ./
CMD ["python", "./main.py"]
