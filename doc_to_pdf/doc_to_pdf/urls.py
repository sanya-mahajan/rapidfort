from django.contrib import admin
from django.urls import path
from converter import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.upload_document, name="upload_document"),
    path("document/<int:pk>/", views.view_document, name="view_document"),
    path("document/<int:pk>/download/", views.download_pdf, name="download_pdf"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
