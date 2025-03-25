from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm
from .models import CustomUser
from django.db.models import Count, Sum
from movies.models import Movie
from tickets.models import Ticket, TicketHolder
from django.db.models.functions import TruncMonth

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Đăng ký tài khoản thành công!")
            return redirect('movie_list')
        else:
            print(form.errors)
    else:
        form = CustomUserCreationForm()
    return render(request, 'users/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Xin chào, {username}! Bạn đã đăng nhập thành công.")
                return redirect('movie_list')
            else:
                messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
        else:
            messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng.")
    else:
        form = CustomAuthenticationForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.info(request, "Bạn đã đăng xuất thành công.")
    return redirect('movie_list')

@login_required
def profile_view(request):
    return render(request, 'users/profile.html')

def staff_check(user):
    return user.is_staff

@login_required
@user_passes_test(staff_check)
def admin_dashboard(request):
    # Thống kê tổng quan
    total_movies = Movie.objects.count()
    total_tickets = Ticket.objects.count()
    total_ticket_holders = TicketHolder.objects.count()
    total_users = CustomUser.objects.count()
    
    # Phim phổ biến nhất (có nhiều vé nhất)
    popular_movies = Movie.objects.annotate(
        ticket_count=Count('ticket')
    ).order_by('-ticket_count')[:5]
    
    # Thống kê người dùng đã đặt vé
    users_with_tickets = CustomUser.objects.annotate(
        ticket_count=Count('ticketholder')
    ).order_by('-ticket_count')[:5]
    
    # Vé theo thể loại phim
    genre_stats = Movie.objects.values('genre').annotate(
        count=Count('ticket')
    ).order_by('-count')[:5]
    
    # Thống kê theo tháng - cách viết tương thích với SQLite
    tickets_by_month = TicketHolder.objects.annotate(
        month=TruncMonth('created_at')
    ).values('month').annotate(count=Count('id')).order_by('month')
    
    # Thống kê theo loại ghế (Thường/VIP)
    seat_type_stats = Ticket.objects.values('seat_type__name').annotate(
        count=Count('id')
    ).order_by('-count')
    
    # Thống kê doanh thu theo loại ghế
    seat_type_revenue = Ticket.objects.values('seat_type__name').annotate(
        total_revenue=Sum('price')
    ).order_by('-total_revenue')
    
    # Thống kê theo loại vé (Người lớn/Trẻ em)
    ticket_type_stats = Ticket.objects.values('type').annotate(
        count=Count('id')
    ).order_by('-count')
    
    context = {
        'total_movies': total_movies,
        'total_tickets': total_tickets,
        'total_ticket_holders': total_ticket_holders,
        'total_users': total_users,
        'popular_movies': popular_movies,
        'users_with_tickets': users_with_tickets,
        'genre_stats': genre_stats,
        'tickets_by_month': tickets_by_month,
        'seat_type_stats': seat_type_stats,
        'seat_type_revenue': seat_type_revenue,
        'ticket_type_stats': ticket_type_stats,
    }
    
    return render(request, 'users/admin_dashboard.html', context)
