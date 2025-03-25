from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from datetime import datetime
from .models import Ticket, TicketHolder, SeatType
from .forms import TicketForm, TicketHolderForm
from movies.models import Movie

def ticket_list(request):
    tickets = Ticket.objects.all().order_by('showtime')
    
    # Xử lý tìm kiếm
    movie_id = request.GET.get('movie', '')
    ticket_type = request.GET.get('ticket_type', '')
    seat_type = request.GET.get('seat_type', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')
    date = request.GET.get('date', '')
    
    # Lọc theo phim
    if movie_id:
        tickets = tickets.filter(movie_id=movie_id)
    
    # Lọc theo loại vé
    if ticket_type:
        tickets = tickets.filter(type=ticket_type)
    
    # Lọc theo loại ghế
    if seat_type:
        tickets = tickets.filter(seat_type_id=seat_type)
    
    # Lọc theo khoảng giá
    if min_price:
        try:
            min_price = float(min_price)
            tickets = tickets.filter(price__gte=min_price)
        except ValueError:
            pass

    if max_price:
        try:
            max_price = float(max_price)
            tickets = tickets.filter(price__lte=max_price)
        except ValueError:
            pass
    
    # Lọc theo ngày chiếu
    if date:
        try:
            date_obj = datetime.strptime(date, '%Y-%m-%d')
            tickets = tickets.filter(showtime__date=date_obj.date())
        except ValueError:
            pass
    
    # Lấy dữ liệu cho các dropdown
    movies = Movie.objects.all()
    seat_types = SeatType.objects.all()
    
    context = {
        'tickets': tickets,
        'movies': movies,
        'seat_types': seat_types,
        'ticket_types': Ticket.TICKET_TYPES,
        'selected_movie': movie_id,
        'selected_ticket_type': ticket_type,
        'selected_seat_type': seat_type,
        'min_price': min_price,
        'max_price': max_price,
        'date': date,
    }
    
    return render(request, 'tickets/ticket_list.html', context)

def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    return render(request, 'tickets/ticket_detail.html', {'ticket': ticket})

@login_required
def ticket_new(request, movie_id=None):
    initial = {}
    if movie_id:
        movie = get_object_or_404(Movie, pk=movie_id)
        initial['movie'] = movie
    
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, "Vé đã được tạo thành công!")
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm(initial=initial)
    return render(request, 'tickets/ticket_edit.html', {'form': form})

@login_required
def ticket_edit(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            ticket = form.save()
            messages.success(request, "Thông tin vé đã được cập nhật!")
            return redirect('ticket_detail', pk=ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'tickets/ticket_edit.html', {'form': form})

@login_required
def ticket_delete(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    if request.method == "POST":
        ticket.delete()
        messages.success(request, "Vé đã được xóa thành công!")
        return redirect('ticket_list')
    return render(request, 'tickets/ticket_confirm_delete.html', {'ticket': ticket})

def ticket_holder_list(request):
    ticket_holders = TicketHolder.objects.all()
    return render(request, 'tickets/ticket_holder_list.html', {'ticket_holders': ticket_holders})

def ticket_holder_detail(request, pk):
    ticket_holder = get_object_or_404(TicketHolder, pk=pk)
    return render(request, 'tickets/ticket_holder_detail.html', {'ticket_holder': ticket_holder})

@login_required
def ticket_holder_new(request, ticket_id=None):
    initial = {}
    if ticket_id:
        ticket = get_object_or_404(Ticket, pk=ticket_id)
        initial['ticket'] = ticket
    
    if request.method == "POST":
        form = TicketHolderForm(request.POST)
        if form.is_valid():
            ticket_holder = form.save(commit=False)
            ticket_holder.user = request.user  # Tự động gán người dùng hiện tại
            ticket_holder.save()
            messages.success(request, "Thông tin người giữ vé đã được tạo thành công!")
            return redirect('ticket_holder_detail', pk=ticket_holder.pk)
    else:
        form = TicketHolderForm(initial=initial)
    return render(request, 'tickets/ticket_holder_edit.html', {'form': form})

@login_required
def ticket_holder_edit(request, pk):
    ticket_holder = get_object_or_404(TicketHolder, pk=pk)
    if request.method == "POST":
        form = TicketHolderForm(request.POST, instance=ticket_holder)
        if form.is_valid():
            ticket_holder = form.save()
            messages.success(request, "Thông tin người giữ vé đã được cập nhật!")
            return redirect('ticket_holder_detail', pk=ticket_holder.pk)
    else:
        form = TicketHolderForm(instance=ticket_holder)
    return render(request, 'tickets/ticket_holder_edit.html', {'form': form})

@login_required
def ticket_holder_delete(request, pk):
    ticket_holder = get_object_or_404(TicketHolder, pk=pk)
    if request.method == "POST":
        ticket_holder.delete()
        messages.success(request, "Thông tin người giữ vé đã được xóa thành công!")
        return redirect('ticket_holder_list')
    return render(request, 'tickets/ticket_holder_confirm_delete.html', {'ticket_holder': ticket_holder})
