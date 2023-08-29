from django.urls import path
from galeria.views import index, imagem, sobre

urlpatterns = [
    path('', index, name='index'),
    path('imagem/', imagem, name='imagem'),
    path('sobre/', sobre, name='sobre'),
]