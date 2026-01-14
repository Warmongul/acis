from django.contrib import admin
from django.urls import path

urlpatterns = [
    path("acis_form_editor/", include("acis_form_editor.urls")),
    path("admin/", admin.site.urls),
]