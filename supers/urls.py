from django.urls import path
from . import views

urlpatterns = [     
    path('', views.create_supers),
    path('<int:pk>/', views.specific_super),
]