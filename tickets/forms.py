from django import forms
from .models import Ticket, TicketHolder

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['price', 'type', 'showtime', 'movie']
        widgets = {
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'showtime': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'movie': forms.Select(attrs={'class': 'form-control'}),
        }

class TicketHolderForm(forms.ModelForm):
    class Meta:
        model = TicketHolder
        fields = ['name', 'type', 'age', 'ticket']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control'}),
            'ticket': forms.Select(attrs={'class': 'form-control'}),
        } 