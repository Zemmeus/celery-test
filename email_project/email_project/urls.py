from django.contrib import admin
from django.urls import path
from email_app.views import send_email_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', send_email_view, name='send_email'),
]