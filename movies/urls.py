from django.urls import path
from . import views

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:pk>/', views.movie_detail, name='movie_detail'),
    path('new/', views.movie_new, name='movie_new'),
    path('<int:pk>/edit/', views.movie_edit, name='movie_edit'),
    path('<int:pk>/delete/', views.movie_delete, name='movie_delete'),
] 