from django.urls import path
from blog import views

app_name = 'blog'


urlpatterns = [
    path('cbv-view', views.IndexView.as_view(), name='cbv-view'),
    path('post/', views.PostList.as_view(), name='post-list'),
    path('go-to-maktabkhoone/<int:pk>', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhoone')
]