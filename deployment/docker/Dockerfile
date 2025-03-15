FROM python:3.9
WORKDIR /app

COPY requirements.txt .
COPY deployment/app.py .
COPY src ./src
COPY models ./models
COPY data ./data

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="/app/src"

# Streamlit Port
EXPOSE 8501
CMD ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
