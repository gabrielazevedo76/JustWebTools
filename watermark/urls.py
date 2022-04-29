from django.urls import path

from . import views

app_name = 'watermark'

urlpatterns = [
    path('', views.uploadForm, name='upload-form'),
    path('<int:pk>', views.handleForm, name='handle-form'),
    path('^<int:pk>^width=<int:width>&height=<int:height>/download', views.download, name='download')
]