from django.core.management.base import BaseCommand
from tickets.models import Ticket, SeatType
from movies.models import Movie
from django.utils import timezone
import random
from datetime import timedelta

class Command(BaseCommand):
    help = 'Thêm các vé mẫu vào cơ sở dữ liệu'

    def handle(self, *args, **options):
        # Xóa tất cả vé hiện có
        Ticket.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Đã xóa tất cả vé hiện có.'))

        # Lấy danh sách phim
        movies = list(Movie.objects.all())
        if not movies:
            self.stdout.write(self.style.ERROR('Không có phim nào trong cơ sở dữ liệu.'))
            return

        # Lấy danh sách loại ghế
        seat_types = list(SeatType.objects.all())
        if not seat_types:
            self.stdout.write(self.style.ERROR('Không có loại ghế nào trong cơ sở dữ liệu.'))
            return

        # Danh sách giá vé cơ bản
        base_prices = [80000, 85000, 90000, 100000, 110000]
        
        # Tạo các vé mẫu
        total_tickets = 20
        tickets_created = 0
        
        # Thời gian hiện tại
        now = timezone.now()
        
        for i in range(total_tickets):
            # Chọn ngẫu nhiên phim
            movie = random.choice(movies)
            
            # Chọn ngẫu nhiên loại ghế
            seat_type = random.choice(seat_types)
            
            # Chọn ngẫu nhiên loại vé
            ticket_type = random.choice(['ADULT', 'CHILD'])
            
            # Chọn ngẫu nhiên giá vé cơ bản
            base_price = random.choice(base_prices)
            
            # Tạo showtime trong 7 ngày tới
            days_ahead = random.randint(0, 7)
            hours = random.randint(9, 22)
            minutes = random.choice([0, 30])
            showtime = now + timedelta(days=days_ahead, hours=hours-now.hour, minutes=minutes-now.minute)
            
            # Tạo số ghế
            row = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'])
            seat_number = f"{row}{random.randint(1, 15)}"
            
            # Tạo vé
            ticket = Ticket.objects.create(
                price=base_price,
                type=ticket_type,
                showtime=showtime,
                movie=movie,
                seat_type=seat_type,
                seat_number=seat_number
            )
            
            self.stdout.write(self.style.SUCCESS(
                f'Đã thêm vé: {movie.title} - {showtime.strftime("%d/%m/%Y %H:%M")} - '
                f'Loại ghế: {seat_type.name} - Số ghế: {seat_number}'
            ))
            tickets_created += 1
        
        # Tổng kết
        self.stdout.write(self.style.SUCCESS(f'Đã thêm thành công {tickets_created} vé mẫu!')) 