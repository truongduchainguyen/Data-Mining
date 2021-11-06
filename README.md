# Data-Mining

Recreate Shazam

## Features:
- Find the similiar songs in the database to the input song (audio fingerprint)


## Crawling guide
- Ex: https://chiasenhac.vn/mp3/vietnam.html?tab=vua-download&page=20
- Input: 
  - vietnam
  - vua-download/bai-hat-moi
Giải thích:
- Gạch đầu dòng đầu tiên là nước nào ví dụ ở trên là vietnam, có thể us-uk, nhạc hoa, etc (Tham khảo thêm trên web), lúc này link được crawl sẽ là  https://chiasenhac.vn/mp3/us-uk.html
- Gạch đầu dòng thứ hai là tab nào, sẽ gồm có hai tab là bai-hat-moi và vua-download. Ex: https://chiasenhac.vn/mp3/us-uk.html?tab=bai-hat-moi

>> Có thể mở rộng để crawl dược cả 2 tab album bên cạnh.

## Lưu ý:
- Với mỗi tab vua-download và bao-hat-moi sẽ chỉ crawl được trang thuộc [1; 19]. Trang 19+ không crawl được, đừng để bị số lượng trang lừa ¯\_(ツ)_/¯
- Phần chưa hoàn thành là lấy link và download bỏ vào location ./data


## Running demo

cd Data-Mining/musichsearch
python manage.py runserver
