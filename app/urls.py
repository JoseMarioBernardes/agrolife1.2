"""
URL configuration for proj_agrolife project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path
from boi import views
from account import views as v2

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', v2.login_view, name='login'),
    path('logout/', v2.logout_view, name='logout'),
    path('', views.home, name='base'),
    path('incluirboi/', views.incluirboi, name='incluirboi'),
    path('consultarboi/', views.consultarboi, name='consultarboi'),
    path('editarboi/<str:brinco>/', views.editarboi, name='editarboi'),
    path('consultarcurral/', views.consultar_curral, name='consultarcurral'),
    path('editarcurral/<int:id_curral>/', views.editar_curral, name='editarcurral'),
    path('excluircurrais/', views.excluir_currais, name='excluircurrais'),
    path('criarcurral/', views.criar_curral, name='criarcurral'),
]
