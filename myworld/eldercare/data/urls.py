from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('data/', views.data, name='data'),
    path('dataimport/', views.dataimport, name='dataimport'),
    path('dataexport/', views.dataexport, name='dataexport'),
    path('dataentry/', views.dataentry, name='dataentry'),
    path('process_file/', views.process_file, name='process_file'),
]