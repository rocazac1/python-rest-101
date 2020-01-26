FROM python:3.8.1
WORKDIR /app
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
ADD main.py models.py ./
CMD ["python", "./main.py"]
