from django.urls import path
from . import views

urlpatterns = [
    path("", views.Accueil, name="Accueil"),
    path("lire/<int:id>", views.lire, name ="lire"),
    

    ]