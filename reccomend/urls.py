from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('python/', views.Python, name='python'),
    path('javascript/', views.JavaScript, name='javascript'),
    path('django/', views.Django, name='django'),
    path('react/', views.React, name='react'),
    path('vue/', views.Vue, name='vue'),
    path('bootstrap/', views.Bootstrap, name='bootstrap'),
    path('angular/', views.Angular, name='angular'),
    path('django-rest/', views.DjangoRest, name='django-rest'),
    path('tensorflow/', views.TensorFlow, name='tensorflow'),
]
