FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install --no-cache-dir flask==3.0.0
EXPOSE 5000
CMD ["python", "app.py"]