from django.contrib import admin
from django.urls import include, path
from data import views

urlpatterns = [
    path('', include('data.urls')),
    path('admin/', admin.site.urls),
    path('dataimport/',views.upload),
]