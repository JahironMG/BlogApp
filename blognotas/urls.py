# Dumento url de blognotas

from django.urls import path
from . import views
app_name = 'blognotas'

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<int:id>/', views.post_detail, name='post_detail'),

]
