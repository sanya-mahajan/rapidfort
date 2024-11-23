FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["gunicorn", "doc_to_pdf.wsgi:application", "--bind", "0.0.0.0:8000"]\
