"""Banco URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from proyectos.views.login import UserLoginAPIView
from proyectos.views.signup import UserSignUpAPIView

from proyectos.views.usuario_proyectos import *
from proyectos.views.proyecto_entregas import *
from proyectos.views.proyecto_participantes import *

from proyectos.views.lista_grupos import *
from proyectos.views.Instructor_proyectos import  *
from proyectos.views.agregar_integrantes import *
from proyectos.views.integrantes import IntegrantesViewSet


from proyectos.views.calificar_proyecto import CalificaProyectoViewSet
from proyectos.views.usuario_ficha import *
from proyectos.views.calificacion_dell_proyecto import ListaDeProyectosViewSet

from proyectos.views.buscar_proyectos import ProyectoList


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('proyectos.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/login/', UserLoginAPIView.as_view(), name='login'),
    path('api/signup/', UserSignUpAPIView.as_view(), name='signup'),
    # Proyecto
    path('buscar_proyectos/', ProyectoList.as_view()),
    path('api/usuario-proyectos/<int:user_id>/', UsuarioProyectoViewSet.as_view({'get':'get_usuario_proyectos'}), name='lista_de_proyectos_de_un_usuario'),#terminado
    path('api/proyecto-participantes/<int:proyecto_id>/', ProyectoParticpantesViewSet.as_view({'get':'get_participantes'}), name='participantes_del_proyecto'),#terminado
    path('api/proyecto-entregas/<int:id_proyecto>/', ProyectoEntregaViewSet.as_view({'get': 'get_entregas_por_proyecto'}), name='lista_entregas_por_proyecto'),#terminado
    
    
    # instructor
    path('api/calificar-proyecto/<int:proyecto_id>/<str:estado>/', CalificaProyectoViewSet.as_view({'put': 'actualizar_proyecto'}), name='calificar_proyecto'),#terminado
    # grupos
    path('api/agregar-integrantes/<int:id_user>/', AgregarInscritosViewSet.as_view({'get': 'get_inscritos'}), name='agregar_inscritos'),#terminado
    path('api/usuario-grupos/<int:id_user>/', UsuarioGruposViewSet.as_view({'get': 'get_mis_grupos'}), name='lista_de_grupos_de un_usuario'),#terminado
    path('api/integrantes/<int:grupo_id>/', IntegrantesViewSet.as_view({'get': 'get_integrantes'}), name='get_fichas_usuario'),


   
    path('api/proyectos-instructor/<int:ficha_id>/',ProyectosViewSet.as_view({'get':'get_usuario_proyectos'}), name='entregas_por_usuario_proyecto'),
    path('api/usuario-ficha/<int:user_id>/', UsuarioFichaViewSet.as_view({'get':'get_fichas'}), name='lista_fichas_de_un_usuario'),#terminado

    path('proyectos/ficha/<int:ficha_id>/', ListaDeProyectosViewSet.as_view({'get': 'get_usuario_proyectos'}), name='get_usuario_proyectos'),

]

