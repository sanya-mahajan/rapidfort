from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
from .forms import DocumentUploadForm
from .models import UploadedDocument
from .utils import convert_docx_to_pdf
import os
from django.conf import settings
from django.http import HttpResponseBadRequest

def upload_document(request):
    if request.method == "POST":
        form = DocumentUploadForm(request.POST, request.FILES)
        if form.is_valid():
            doc = form.save()
            
            # Convert .docx to PDF
            input_path = doc.uploaded_file.path
            output_path = os.path.join(settings.MEDIA_ROOT, f"{doc.name}.pdf")
            convert_docx_to_pdf(input_path, output_path)
            return redirect("view_document", pk=doc.pk)
    else:
        form = DocumentUploadForm()
    return render(request, "upload.html", {"form": form})

def view_document(request, pk):
    doc = UploadedDocument.objects.get(pk=pk)
    pdf_path = os.path.join(settings.MEDIA_ROOT, f"{doc.name}.pdf")
    metadata = {
        "Name": doc.name,
        "Uploaded At": doc.uploaded_at,
        "PDF Path": pdf_path,
    }
    return render(request, "view.html", {"metadata": metadata, "doc": doc})

def download_pdf(request, pk):
    doc = UploadedDocument.objects.get(pk=pk)
    pdf_path = os.path.join(settings.MEDIA_ROOT, f"{doc.name}.pdf")
    response = FileResponse(open(pdf_path, "rb"), as_attachment=True, filename=f"{doc.name}.pdf")
    return response
