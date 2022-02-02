from django.urls import path
from core import views


urlpatterns = [
    path("", views.index, name='index'),
    path("nosotros_de", views.nosotros_de, name ='nosotros_de'),
    path("entrar", views.entrar, name ='entrar'),
    path('carrito', views.carrito, name='carrito'),
    path("contactos", views.contacto, name='contacto'),
    path("registro", views.registrarse, name='registro'),
    path("salir", views.salir, name = 'salir'),
    path("galeria_dos", views.galeria_dos, name = 'galeria_dos'),
    path(r'vista_producto/(?P<product_id>\d+)/$', views.vista_producto, name='vista_producto')
    #path('vista_producto', views.vista_producto, name='vista_producto'),

]

