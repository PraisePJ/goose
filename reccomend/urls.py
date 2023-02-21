from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home),
    path('python/', views.Python, name='python'),
    path('javascript/', views.JavaScript, name='javascript'),
    path('django/', views.Django, name='django')
]
