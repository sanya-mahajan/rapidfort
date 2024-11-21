from django import forms
from .models import UploadedDocument

class DocumentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedDocument
        fields = ["name", "uploaded_file"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['uploaded_file'].widget.attrs.update({'accept': '.docx'})