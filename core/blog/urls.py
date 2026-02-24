from django.urls import path
from blog import views

app_name = 'blog'


urlpatterns = [
    # path('cbv-view', views.IndexView.as_view(), name='cbv-view'),
    # path('go-to-maktabkhoone/<int:pk>', views.RedirectToMaktab.as_view(), name='redirect-to-maktabkhoone'),
    # path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/<int:pk>', views.PostDetailView.as_view(), name='post-detail'),
    # path('post/create/', views.PostCreateView.as_view(), name='post-create'),
    # path('post/<int:pk>/edit/', views.PostEditView.as_view(), name='post-edit'),
    # path('post/<int:pk>/delete/', views.PostDeleteView.as_view(), name='post-delete'),
    path('post/', views.api_post_list_view, name='post-list'),
]