# ỨNG DỤNG WEB ĐẶT VÉ XEM PHIM

## Giới thiệu
Ứng dụng Web Đặt vé xem phim được phát triển bằng framework Django theo mô hình MVC (trong Django thực tế là MTV - Model-Template-View). Ứng dụng cho phép người dùng đặt vé xem phim, quản lý thông tin phim, vé và người giữ vé.

## Mô tả hệ thống

### Các thực thể chính
1. **Phim (Movie)**
   - Tiêu đề (title)
   - Nhà sản xuất (producer)
   - Thời lượng (duration)
   - Đạo diễn (director)
   - Thể loại (genre)

2. **Vé (Ticket)**
   - Giá vé (price)
   - Loại vé (người lớn/trẻ em - adult/child)
   - Giờ chiếu (showtime)
   - Phim (movie - liên kết tới thực thể Phim)

3. **Người giữ vé (TicketHolder)**
   - Tên (name)
   - Loại người (người lớn/trẻ em - adult/child)
   - Tuổi (age)
   - Vé (ticket - liên kết tới thực thể Vé)

### Mối quan hệ
- Một phim có thể có nhiều vé, nhưng một vé chỉ liên kết đến một phim duy nhất (quan hệ 1-n)
- Một người giữ vé chỉ giữ một vé, và một vé chỉ thuộc về một người giữ vé (quan hệ 1-1)

## Sơ đồ chức năng

### Quản lý Phim
- Thêm phim mới
- Chỉnh sửa thông tin phim
- Xóa phim
- Xem danh sách phim
- Tìm kiếm phim theo tiêu đề, thể loại, đạo diễn

### Quản lý Vé
- Tạo vé mới cho phim
- Chỉnh sửa thông tin vé
- Xóa vé
- Xem danh sách vé
- Tìm kiếm vé theo giờ chiếu, phim, giá...

### Quản lý Người giữ vé
- Thêm thông tin người giữ vé
- Chỉnh sửa thông tin người giữ vé
- Xóa thông tin người giữ vé
- Xem danh sách người giữ vé
- Tìm kiếm người giữ vé theo tên, tuổi...

### Thống kê
- Thống kê số lượng vé bán ra theo phim
- Thống kê doanh thu theo phim
- Thống kê theo thời gian (ngày, tuần, tháng)
- Thống kê theo loại vé (người lớn/trẻ em)

## Biểu đồ Use Case

### Actors
1. **Khách hàng**
   - Xem danh sách phim
   - Tìm kiếm phim
   - Đặt vé xem phim
   - Xem thông tin vé đã đặt

2. **Admin**
   - Quản lý phim (CRUD)
   - Quản lý vé (CRUD)
   - Quản lý người giữ vé (CRUD)
   - Xem thống kê
   - Quản lý tài khoản người dùng

### Use Cases chính
- Đăng nhập/Đăng ký
- Quản lý phim
- Quản lý vé
- Quản lý người giữ vé
- Đặt vé
- Tìm kiếm
- Thống kê
- Thanh toán

## Biểu đồ Lớp

### Movie
- Attributes:
  - id: int
  - title: string
  - producer: string
  - duration: int (phút)
  - director: string
  - genre: string
- Methods:
  - create()
  - update()
  - delete()
  - get_tickets()

### Ticket
- Attributes:
  - id: int
  - price: decimal
  - type: enum (ADULT, CHILD)
  - showtime: datetime
  - movie_id: int (Foreign Key)
- Methods:
  - create()
  - update()
  - delete()
  - get_movie()

### TicketHolder
- Attributes:
  - id: int
  - name: string
  - type: enum (ADULT, CHILD)
  - age: int
  - ticket_id: int (Foreign Key)
- Methods:
  - create()
  - update()
  - delete()
  - get_ticket()

## Biểu đồ dữ liệu (ERD)

### Bảng Movie
- id (PK)
- title
- producer
- duration
- director
- genre
- created_at
- updated_at

### Bảng Ticket
- id (PK)
- price
- type
- showtime
- movie_id (FK)
- created_at
- updated_at

### Bảng TicketHolder
- id (PK)
- name
- type
- age
- ticket_id (FK)
- created_at
- updated_at

## Giao diện ứng dụng

### Trang chủ
- Banner quảng cáo phim mới
- Danh sách phim đang chiếu
- Tìm kiếm phim
- Đăng nhập/Đăng ký

### Trang chi tiết phim
- Thông tin phim (tiêu đề, nhà sản xuất, thời lượng, đạo diễn, thể loại)
- Danh sách giờ chiếu
- Nút đặt vé

### Trang đặt vé
- Chọn ghế
- Chọn loại vé (người lớn/trẻ em)
- Nhập thông tin người giữ vé
- Thanh toán

### Trang Admin
- Quản lý phim
- Quản lý vé
- Quản lý người giữ vé
- Thống kê

## Test Cases

### Test Case cho chức năng Quản lý Phim
1. **TC-01**: Thêm phim mới
   - Input: Tất cả thông tin hợp lệ
   - Expected Result: Thêm phim thành công

2. **TC-02**: Thêm phim với dữ liệu thiếu
   - Input: Thiếu tiêu đề phim
   - Expected Result: Hiện thông báo lỗi

3. **TC-03**: Cập nhật thông tin phim
   - Input: Cập nhật thời lượng phim
   - Expected Result: Cập nhật thành công

4. **TC-04**: Xóa phim
   - Input: Xóa phim không có vé
   - Expected Result: Xóa thành công

5. **TC-05**: Xóa phim có vé
   - Input: Xóa phim đã có vé
   - Expected Result: Hiện thông báo xác nhận về việc xóa cả vé

### Test Case cho chức năng Quản lý Vé
1. **TC-06**: Tạo vé mới
   - Input: Tất cả thông tin hợp lệ
   - Expected Result: Tạo vé thành công

2. **TC-07**: Tạo vé với giá âm
   - Input: Giá vé là số âm
   - Expected Result: Hiện thông báo lỗi

3. **TC-08**: Cập nhật thông tin vé
   - Input: Cập nhật giờ chiếu
   - Expected Result: Cập nhật thành công

4. **TC-09**: Xóa vé
   - Input: Xóa vé chưa có người giữ
   - Expected Result: Xóa thành công

5. **TC-10**: Xóa vé đã có người giữ
   - Input: Xóa vé đã có người giữ
   - Expected Result: Hiện thông báo xác nhận

### Test Case cho chức năng Đặt vé
1. **TC-11**: Đặt vé thành công
   - Input: Đầy đủ thông tin người giữ vé và vé hợp lệ
   - Expected Result: Đặt vé thành công

2. **TC-12**: Đặt vé với thông tin người giữ vé không hợp lệ
   - Input: Tuổi người giữ vé là số âm
   - Expected Result: Hiện thông báo lỗi

## Cấu trúc MVC trong Django

Django sử dụng mô hình MTV (Model-Template-View) tương đương với MVC:

### Model (M)
- Định nghĩa cấu trúc dữ liệu
- Chứa các phương thức để tương tác với cơ sở dữ liệu
- File: `models.py` trong mỗi ứng dụng Django

```python
# Ví dụ mẫu cho models.py
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)
    producer = models.CharField(max_length=200)
    duration = models.IntegerField()
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

class Ticket(models.Model):
    TICKET_TYPES = [
        ('ADULT', 'Người lớn'),
        ('CHILD', 'Trẻ em'),
    ]
    price = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.CharField(max_length=5, choices=TICKET_TYPES)
    showtime = models.DateTimeField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.movie.title} - {self.showtime}"

class TicketHolder(models.Model):
    HOLDER_TYPES = [
        ('ADULT', 'Người lớn'),
        ('CHILD', 'Trẻ em'),
    ]
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=5, choices=HOLDER_TYPES)
    age = models.IntegerField()
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
```

### Template (T) - tương đương View trong MVC
- Xử lý việc hiển thị dữ liệu
- Chứa HTML, CSS và JavaScript
- File: `*.html` trong thư mục templates

### View (V) - tương đương Controller trong MVC
- Xử lý logic nghiệp vụ
- Tương tác với Model và Template
- File: `views.py` trong mỗi ứng dụng Django

```python
# Ví dụ mẫu cho views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Movie, Ticket, TicketHolder
from .forms import MovieForm, TicketForm, TicketHolderForm

def movie_list(request):
    movies = Movie.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_detail(request, pk):
    movie = get_object_or_404(Movie, pk=pk)
    return render(request, 'movies/movie_detail.html', {'movie': movie})

def movie_new(request):
    if request.method == "POST":
        form = MovieForm(request.POST)
        if form.is_valid():
            movie = form.save()
            return redirect('movie_detail', pk=movie.pk)
    else:
        form = MovieForm()
    return render(request, 'movies/movie_edit.html', {'form': form})
```

## Cấu trúc thư mục dự án

```
cinema_ticket_booking/
├── manage.py
├── cinema_ticket_booking/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── movies/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── tickets/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── users/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── migrations/
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── static/
│   ├── css/
│   ├── js/
│   └── images/
└── templates/
    ├── base.html
    ├── movies/
    ├── tickets/
    └── users/
```

## Cài đặt và chạy dự án

### Yêu cầu hệ thống
- Python 3.8+
- Django 4.0+
- Database (SQLite, PostgreSQL,...)

### Các bước cài đặt
1. Clone repository
```
git clone <repository-url>
cd cinema_ticket_booking
```

2. Tạo và kích hoạt môi trường ảo
```
python -m venv venv
source venv/bin/activate  # Trên Windows: venv\Scripts\activate
```

3. Cài đặt các thư viện cần thiết
```
pip install -r requirements.txt
```

4. Tạo cơ sở dữ liệu
```
python manage.py migrate
```

5. Tạo tài khoản quản trị
```
python manage.py createsuperuser
```

6. Chạy server
```
python manage.py runserver
```

7. Truy cập ứng dụng
- Web: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## Tổng kết
Ứng dụng Web Đặt vé xem phim được phát triển với Django sử dụng mô hình MTV (Model-Template-View). Ứng dụng cung cấp đầy đủ các chức năng CRUD cho Phim, Vé và Người giữ vé, cùng với chức năng đặt vé, tìm kiếm và thống kê. Giao diện người dùng được thiết kế đơn giản, thân thiện giúp người dùng dễ dàng tìm kiếm và đặt vé xem phim. 