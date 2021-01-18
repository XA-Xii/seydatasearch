import views as views
from django.urls import path
from . import views

urlpatterns = [
    path('sey_select/', views.toWelcome),
    path('apitest/', views.apitest),
]
