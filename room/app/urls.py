from django.urls import path
from . import views
from django.views.i18n import JavaScriptCatalog

urlpatterns = [
    path('', views.home, name="home"),
    
]