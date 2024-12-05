from django.urls import path
from . import views
from sites.views import task_list


urlpatterns = [
    path('', views.home_view, name='homepage'),
    path('client/', views.client_view, name='client'),
    path('photos/', views.photo_view, name='photos'),
    path('service/', views.service_view, name='service'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('task', task_list, name='task'),
]