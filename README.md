## Description
This is a Django-based web application that allows users to:

- Upload a .docx file.
- View the file metadata.
- Convert the uploaded file into a PDF format.
- Download the converted PDF.
## Features
- Secure Upload: The application restricts uploads to .docx files only.
- PDF Password Protection: Users can password-protect the generated PDF.
- Microservice Architecture: The app is designed to use a microservice for handling file conversion.
- Containerization: Dockerized for easy deployment and scalability.
- Kubernetes-Ready: Includes manifest files for deploying the application to Kubernetes.
- Hosted Endpoint: The app is hosted online for easy testing.

## Technologies Used
Backend: Django, Python
Frontend: HTML5, CSS3, Bootstrap
Database: PostgreSQL
PDF Processing: python-docx for handling .docx files, reportlab for PDF generation, and PyPDF2 for password-protected PDFs.
Containerization: Docker
Orchestration: Kubernetes
Cloud Hosting: AWS or any cloud provider
CI/CD: GitHub Actions for automated build pipelines.

## Installation
### Prerequisites
Python 3.9+
Docker and Docker Compose
Kubernetes CLI (kubectl) and Minikube or a Kubernetes cluster

### Steps
Clone the Repository

```
git clone https://github.com/your-repo/docx-to-pdf
cd docx-to-pdf
```

Set Up Virtual Environment
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Run Migrations

```
python manage.py makemigrations
python manage.py migrate

```
Start the Server

```
python manage.py runserver
```
