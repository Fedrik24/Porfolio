from django.urls import path
from . import views

app_name = "AryaFedrik"

urlpatterns = [
    path('About/', views.AboutView.as_view(), name='about'),
    path('', views.indexView.as_view(), name='index'),
    path('Work/', views.WorkView.as_view(), name='work'),
    path('Contact/', views.ContactView.as_view(), name='contact')
]
