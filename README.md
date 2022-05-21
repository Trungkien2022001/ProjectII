# ProjectII
Đầu tiên mình sẽ tạo ra một list các url của mỗi loại. Tạo bằng file Crawl.py
Khi có list URL rồi thì chạy bên CrawlData, mỗi URL sẽ tạo được 1 file .txt
Dữ liệu này sẽ dùng để training model

# crawler voi scrapy
- cài đặt sẵn scrapy trong máy
- chạy các lệnh sau trong cmd tại thư mục của project:
    scrapy crawl basic -s CLOSESPIDER_ITEMCOUNT=100 -o test.csv (chạy test với 100 items)
- thay số lượng tuỳ chỉnh theo ý muốn hoặc để chạy vô tận
