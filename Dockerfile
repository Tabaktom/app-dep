FROM python:3.10

WORKDIR /app

COPY streamlit-app/requirements.txt .
RUN pip install -r requirements.txt
RUN python -m textblob.download_corpora

COPY . .

EXPOSE 5000
CMD ["python", "main.py"]
