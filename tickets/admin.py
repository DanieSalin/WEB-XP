from django.contrib import admin
from .models import Ticket, TicketHolder

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('movie', 'showtime', 'price', 'type')
    list_filter = ('type', 'showtime')
    search_fields = ('movie__title',)

@admin.register(TicketHolder)
class TicketHolderAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'type', 'ticket')
    list_filter = ('type', 'age')
    search_fields = ('name', 'ticket__movie__title')
