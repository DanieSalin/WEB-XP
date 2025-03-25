from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Movie
from .forms import MovieForm

def movie_list(request):
    movies = Movie.objects.all()
    
    # Xử lý tìm kiếm
    query = request.GET.get('q', '')
    genre = request.GET.get('genre', '')
    director = request.GET.get('director', '')
    
    if query:
        movies = movies.filter(
            Q(title__icontains=query)
        )
    
    if genre:
        movies = movies.filter(genre__icontains=genre)
    
    if director:
        movies = movies.filter(director__icontains=director)
        
    # Lấy danh sách các thể loại để hiển thị trong dropdown
    all_genres = set()
    for movie in Movie.objects.all():
        for genre in movie.genre.split(','):
            all_genres.add(genre.strip())
    
    # Lấy danh sách đạo diễn để hiển thị trong dropdown
    all_directors = Movie.objects.values_list('director', flat=True).distinct()
    
    context = {
        'movies': movies,
        'query': query,
        'genre': genre,
        'director': director,
        'all_genres': sorted(all_genres),
        'all_directors': all_directors
    }
    
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

@login_required
def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            movie = form.save()
            messages.success(request, "Phim đã được tạo thành công!")
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie_edit.html', {'form': form})

@login_required
def movie_edit(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            movie = form.save()
            messages.success(request, "Thông tin phim đã được cập nhật!")
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm(instance=movie)
    return render(request, 'movies/movie_edit.html', {'form': form})

@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    if request.method == "POST":
        movie.delete()
        messages.success(request, "Phim đã được xóa thành công!")
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
