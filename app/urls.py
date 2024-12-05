"""
URL configuration for app project.

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
    path('', views.home, name='base'),
    path('admin/', admin.site.urls),
    path('login/', v2.login_view, name='login'),
    path('logout/', v2.logout_view, name='logout'),
    path('criarcurral/', views.criar_curral_view, name='criarcurral'),
    path('incluirboi/', views.incluir_boi_view, name='incluirboi'),
    path('criarlote/', views.criar_lote_view, name='criarlote'),
    path('criarmedicamento/', views.criar_medicamento_view, name='criarmedicamento'),
    path('listacurral/', views.lista_curral_view, name='listacurral'),
    path('listaboi/', views.lista_boi_view, name='listaboi'),
    path('listamedicamento/', views.lista_medicamento_view, name='listamedicamento'),
    path('listalote/', views.lista_lote_view, name='listalote'),
    path('curral/<int:pk>/', views.CurralDetailView.as_view(), name='detalhecurral'),
    path('curral/<int:pk>/update/', views.CurralUpdateView.as_view(), name='atualizacurral'),
    path('curral/<int:pk>/delete/', views.CurralDeleteView.as_view(), name='deletacurral'),
    ]