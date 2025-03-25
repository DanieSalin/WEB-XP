from django.urls import path
from . import views

urlpatterns = [
    # URLs cho Ticket
    path('', views.ticket_list, name='ticket_list'),
    path('<int:pk>/', views.ticket_detail, name='ticket_detail'),
    path('new/', views.ticket_new, name='ticket_new'),
    path('new/<int:movie_id>/', views.ticket_new, name='ticket_new_for_movie'),
    path('<int:pk>/edit/', views.ticket_edit, name='ticket_edit'),
    path('<int:pk>/delete/', views.ticket_delete, name='ticket_delete'),
    
    # URLs cho TicketHolder
    path('holders/', views.ticket_holder_list, name='ticket_holder_list'),
    path('holders/<int:pk>/', views.ticket_holder_detail, name='ticket_holder_detail'),
    path('holders/new/', views.ticket_holder_new, name='ticket_holder_new'),
    path('holders/new/<int:ticket_id>/', views.ticket_holder_new, name='ticket_holder_new_for_ticket'),
    path('holders/<int:pk>/edit/', views.ticket_holder_edit, name='ticket_holder_edit'),
    path('holders/<int:pk>/delete/', views.ticket_holder_delete, name='ticket_holder_delete'),
] 