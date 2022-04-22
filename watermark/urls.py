from django.urls import path

from . import views

app_name = 'watermark'

urlpatterns = [
    path('', views.uploadForm, name='upload-form'),
    path('<int:pk>', views.download, name='download')
]