FROM python:3.11-slim
WORKDIR /app
COPY app.py .
#Ajout mongoDB
RUN pip install --no-cache-dir flask==3.0.0 pymongo==4.8.0 
CMD ["python", "app.py"]
