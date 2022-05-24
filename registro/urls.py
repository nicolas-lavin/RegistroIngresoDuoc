from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('',views.home,name="home"),
    path('listar_registros/', views.registros, name="listar_registros"),
    path('ingresar_registros/', views.CreateRegistros, name="ingresar_registros"),
    path('mantenedor_personas/', views.MantenedorPersonas, name="mantenedor_personas"),

    path('crear_persona/', views.createPersona, name="crear_persona"),
    path('actualizar_persona/<str:pk>/', views.updatePersona, name="actualizar_persona"),
    path('borrar_persona/<str:pk>/', views.deletePersona, name="borrar_persona"),
]