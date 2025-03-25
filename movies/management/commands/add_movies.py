import os
import urllib.request
from urllib.parse import unquote
import ssl
from django.core.management.base import BaseCommand
from movies.models import Movie

class Command(BaseCommand):
    help = 'Thêm dữ liệu phim'

    def handle(self, *args, **kwargs):
        # Xóa tất cả phim hiện có
        Movie.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Đã xóa tất cả phim hiện có'))

        # Tạo thư mục media/movies nếu chưa có
        os.makedirs('media/movies', exist_ok=True)

        # Bỏ qua xác thực SSL để tải ảnh
        ssl._create_default_https_context = ssl._create_unverified_context

        # Danh sách phim từ dữ liệu đã cung cấp
        MOVIES_DATA = [
            {
                'title': 'Trừ Tà Ký: Khởi Nguyên Hắc Ám',
                'genre': 'Kinh dị, Hoạt hình',
                'duration': 85,
                'director': 'Đạo diễn Trừ Tà Ký',
                'producer': 'Studio phim kinh dị',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f03%2f13%2f400x633%2D170853%2D130325%2D40.jpg',
                'description': 'Một bộ phim kinh dị kết hợp hoạt hình về câu chuyện trừ tà.'
            },
            {
                'title': 'Nàng Bạch Tuyết',
                'genre': 'Phiêu lưu, Âm Nhạc',
                'duration': 108,
                'director': 'Đạo diễn Bạch Tuyết',
                'producer': 'Disney',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f02%2f19%2f1%2D162736%2D190225%2D24.jpg',
                'description': 'Phiên bản mới của câu chuyện cổ tích Nàng Bạch Tuyết với âm nhạc đặc sắc.'
            },
            {
                'title': 'Quỷ Nhập Tràng',
                'genre': 'Kinh dị',
                'duration': 122,
                'director': 'Đạo diễn Quỷ Nhập Tràng',
                'producer': 'Studio phim kinh dị',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f02%2f18%2fscreenshot%2D2025%2D02%2D18%2D152722%2D152809%2D180225%2D53.png',
                'description': 'Câu chuyện kinh dị về những thực thể siêu nhiên xâm nhập vào thế giới con người.'
            },
            {
                'title': 'Sát Thủ Vô Cùng Cực Hài',
                'genre': 'Hài hước, Hành động',
                'duration': 107,
                'director': 'Đạo diễn hành động',
                'producer': 'Studio phim hài',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f03%2f01%2f400x633%2D6%2D170323%2D010325%2D66.jpg',
                'description': 'Câu chuyện về một sát thủ hài hước với nhiều tình huống dở khóc dở cười.'
            },
            {
                'title': 'Nhà Gia Tiên',
                'genre': 'Gia đình, Hài hước',
                'duration': 117,
                'director': 'Đạo diễn gia đình',
                'producer': 'Studio phim gia đình',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f02%2f06%2fngt%2Dpayoff%2Dposter%2D400x633%2D154653%2D060225%2D20.jpg',
                'description': 'Câu chuyện hài hước và cảm động về một gia đình đặc biệt.'
            },
            {
                'title': 'Cô Gái Năm Ấy Chúng Ta Cùng Theo Đuổi',
                'genre': 'Tâm lý, Tình cảm',
                'duration': 102,
                'director': 'Đạo diễn phim tình cảm',
                'producer': 'Studio phim tình cảm',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f03%2f14%2fscreenshot%2D2025%2D03%2D14%2D143025%2D143121%2D140325%2D92.png',
                'description': 'Chuyện tình lãng mạn và đầy cảm xúc về những năm tháng tuổi trẻ.'
            },
            {
                'title': 'Lạc Trôi',
                'genre': 'Hoạt hình',
                'duration': 89,
                'director': 'Đạo diễn hoạt hình',
                'producer': 'Studio hoạt hình',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f02%2f17%2fmv5botm5odblotatyjcwzi00yzkzlwizodetmtm2mtzlndfmmwu2xkeyxkfqcgc%2Dv1%2Dfmjpg%2Dux1000%2D151445%2D170225%2D93.jpg',
                'description': 'Phim hoạt hình về chuyến phiêu lưu kỳ thú.'
            },
            {
                'title': 'Love Lies: Yêu Vì Tiền - Điên Vì Tình',
                'genre': 'Tình cảm, Hài hước',
                'duration': 114,
                'director': 'Đạo diễn Love Lies',
                'producer': 'Studio phim tình cảm',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f02%2f17%2fscreenshot%2D2025%2D02%2D17%2D161948%2D162028%2D170225%2D78.png',
                'description': 'Câu chuyện hài hước và cảm động về sự lựa chọn giữa tình yêu và tiền bạc.'
            },
            {
                'title': 'Mickey 17',
                'genre': 'Khoa học, viễn tưởng',
                'duration': 137,
                'director': 'Đạo diễn viễn tưởng',
                'producer': 'Studio phim viễn tưởng',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f02%2f17%2fscreenshot%2D2025%2D02%2D17%2D152707%2D152739%2D170225%2D62.png',
                'description': 'Phim viễn tưởng về tương lai của nhân loại và công nghệ.'
            },
            {
                'title': 'Nghề Siêu Khó Nói',
                'genre': 'Hài hước, Tình cảm',
                'duration': 102,
                'director': 'Đạo diễn hài',
                'producer': 'Studio phim hài',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f03%2f14%2fff%2Dmain%2Dposter%2D400x633px%2D151317%2D140325%2D48.jpg',
                'description': 'Câu chuyện hài hước về một người làm nghề đặc biệt không thể nói với ai.'
            },
            {
                'title': 'Nghi Lễ Trục Quỷ',
                'genre': 'Kinh dị',
                'duration': 96,
                'director': 'Đạo diễn kinh dị',
                'producer': 'Studio phim kinh dị',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f03%2f05%2fscreenshot%2D2025%2D03%2D05%2D142116%2D142207%2D050325%2D78.png',
                'description': 'Câu chuyện kinh dị về nghi lễ trục quỷ đầy kinh hoàng.'
            },
            {
                'title': 'Nhà Ga Ma Chó',
                'genre': 'Kinh dị, Bí ẩn',
                'duration': 89,
                'director': 'Đạo diễn kinh dị',
                'producer': 'Studio phim kinh dị',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2024%2f11%2f12%2fscreenshot%2D2024%2D11%2D12%2D150446%2D150547%2D121124%2D17.png',
                'description': 'Phim kinh dị về nhà ga bí ẩn với những câu chuyện ma quái.'
            },
            {
                'title': 'The Monkey: Tiếng Vọng Kinh Hoàng',
                'genre': 'Kinh dị',
                'duration': 98,
                'director': 'Đạo diễn The Monkey',
                'producer': 'Studio phim kinh dị',
                'image_url': 'https://files.betacorp.vn/media%2fimages%2f2025%2f01%2f14%2fscreenshot%2D2025%2D01%2D14%2D160523%2D160557%2D140125%2D34.png',
                'description': 'Câu chuyện kinh dị về tiếng vọng bí ẩn từ rừng sâu.'
            }
        ]

        # Thêm phim vào database
        for movie_data in MOVIES_DATA:
            try:
                # Tạo tên file ảnh
                image_url = movie_data['image_url']
                image_name = f"{movie_data['title'].replace(' ', '_').replace(':', '_')}.jpg"
                image_path = f"movies/{image_name}"
                local_path = f"media/{image_path}"
                
                # Tải ảnh về 
                urllib.request.urlretrieve(image_url, local_path)
                
                # Tạo phim mới
                movie = Movie(
                    title=movie_data['title'],
                    director=movie_data['director'],
                    producer=movie_data['producer'],
                    duration=movie_data['duration'],
                    genre=movie_data['genre'],
                    description=movie_data['description'],
                    image=image_path
                )
                movie.save()
                self.stdout.write(self.style.SUCCESS(f"Đã thêm phim: {movie_data['title']}"))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f"Lỗi khi thêm phim {movie_data['title']}: {str(e)}"))

        self.stdout.write(self.style.SUCCESS('Hoàn tất việc thêm phim!')) 