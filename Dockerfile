FROM python:3
WORKDIR /app
ADD requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt 
ADD main.py models.py ./
CMD ["python", "./main.py"]