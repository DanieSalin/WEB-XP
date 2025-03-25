from django.core.management.base import BaseCommand
from tickets.models import SeatType

class Command(BaseCommand):
    help = 'Thêm các loại ghế vào cơ sở dữ liệu'

    def handle(self, *args, **options):
        # Xóa tất cả các loại ghế hiện có
        SeatType.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Đã xóa tất cả loại ghế hiện có.'))

        # Tạo loại ghế thường
        normal_seat = SeatType.objects.create(
            name='Thường',
            description='Ghế tiêu chuẩn, phù hợp cho đa số người xem.',
            price_multiplier=1.0
        )
        self.stdout.write(self.style.SUCCESS(f'Đã thêm loại ghế: {normal_seat.name}'))

        # Tạo loại ghế VIP
        vip_seat = SeatType.objects.create(
            name='VIP',
            description='Ghế cao cấp, rộng rãi và thoải mái hơn, vị trí đẹp trong rạp.',
            price_multiplier=1.5
        )
        self.stdout.write(self.style.SUCCESS(f'Đã thêm loại ghế: {vip_seat.name}'))

        # Tổng kết
        self.stdout.write(self.style.SUCCESS('Hoàn tất việc thêm loại ghế!')) 