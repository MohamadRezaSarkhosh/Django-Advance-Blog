from django.urls import path
from blog import views



urlpatterns = [
    path('cbv-view', views.IndexView.as_view(), name='cbv-view'),
]