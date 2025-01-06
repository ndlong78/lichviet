
```markdown
Tài Liệu Ứng Dụng Lịch Việt

1. Tổng Quan
1.1 Giới thiệu
Lịch Việt là một ứng dụng web được phát triển bằng Python Flask, cho phép người dùng quản lý lịch theo ngày, tuần, tháng và năm. Ứng dụng hỗ trợ cả lịch âm và các sự kiện đặc biệt.

1.2 Tính năng chính
- Xem lịch theo ngày/tuần/tháng/năm
- Quản lý sự kiện và lịch hẹn
- Hiển thị lịch âm
- Quản lý danh mục sự kiện
- API cho tích hợp bên ngoài

2. Cài Đặt và Triển Khai
2.1 Yêu cầu hệ thống
- Python 3.8+
- SQLite/PostgreSQL
- Virtual Environment

2.2 Cài đặt
```bash
# Clone repository
git clone https://github.com/ndlong78/lichviet.git
cd lichviet

# Tạo môi trường ảo
python3 -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Cài đặt dependencies
pip install -r requirements.txt

# Thiết lập môi trường
cp .env.example .env
# Chỉnh sửa file .env theo cấu hình mong muốn

# Khởi tạo database
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
```

3. Cấu Trúc Dự Án
3.1 Cấu trúc thư mục
```plaintext
lichviet/
├── app/                    # Thư mục chính của ứng dụng
│   ├── __init__.py        # Khởi tạo ứng dụng Flask
│   ├── models.py          # Định nghĩa models
│   ├── main/              # Blueprint chính
│   │   ├── __init__.py
│   │   └── routes.py      # Định tuyến
│   ├── templates/         # Templates Jinja2
│   │   ├── base.html
│   │   └── calendar/      # Templates cho calendar
│   └── static/            # Static files
│       ├── css/
│       └── js/
├── migrations/            # Database migrations
├── tests/                # Unit tests
├── config.py            # Cấu hình
├── requirements.txt     # Dependencies
└── run.py              # Entry point
```

3.2 Components chính
- **Models (app/models.py)**
    - **Event Model**
        - id: Integer (Primary Key)
        - title: String
        - description: Text
        - start_time: DateTime
        - end_time: DateTime
        - category_id: ForeignKey
        - created_at: DateTime
        - updated_at: DateTime
    - **Category Model**
        - id: Integer (Primary Key)
        - name: String
        - color: String
        - description: String

4. API Documentation
4.1 RESTful API Endpoints
- **Events API**
    - `GET /api/events`: Lấy danh sách sự kiện
    - `POST /api/events`: Tạo sự kiện mới
    - `GET /api/events/<id>`: Lấy chi tiết sự kiện
    - `PUT /api/events/<id>`: Cập nhật sự kiện
    - `DELETE /api/events/<id>`: Xóa sự kiện
- **Categories API**
    - `GET /api/categories`: Lấy danh sách categories
    - `POST /api/categories`: Tạo category mới

5. Tính Năng Chi Tiết
5.1 Calendar View
- Month View: Hiển thị lịch theo tháng
- Week View: Hiển thị lịch theo tuần
- Day View: Hiển thị lịch theo ngày
- Year View: Hiển thị tổng quan theo năm

5.2 Event Management
- Tạo/Sửa/Xóa sự kiện
- Phân loại sự kiện theo category
- Lặp lại sự kiện (daily, weekly, monthly)
- Nhắc nhở sự kiện

5.3 Lunar Calendar
- Hiển thị ngày âm lịch
- Các ngày lễ, tết theo âm lịch
- Các ngày đặc biệt trong năm

6. Database Schema
```sql
CREATE TABLE events (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title VARCHAR(100) NOT NULL,
    description TEXT,
    start_time DATETIME NOT NULL,
    end_time DATETIME NOT NULL,
    category_id INTEGER,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(50) NOT NULL,
    color VARCHAR(7) DEFAULT '#3498db',
    description VARCHAR(200)
);
```

7. Configuration
7.1 Environment Variables
```plaintext
FLASK_APP=run.py
FLASK_ENV=development
FLASK_DEBUG=1
FLASK_HOST=0.0.0.0
FLASK_PORT=8088
DATABASE_URL=sqlite:///lichviet.db
SECRET_KEY=your-secret-key
TIMEZONE=Asia/Ho_Chi_Minh
```

7.2 Development Configuration
```python
class DevelopmentConfig:
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
```

8. Testing
8.1 Unit Tests
```bash
# Chạy tests
python -m pytest tests/

# Chạy với coverage
pytest --cov=app tests/
```

8.2 Test Cases
- Test các models
- Test các routes
- Test API endpoints
- Test lunar calendar calculations

9. Deployment
9.1 Production Setup
```bash
# Install production dependencies
pip install gunicorn

# Run with gunicorn
gunicorn -w 4 -b 0.0.0.0:8088 run:app
```

9.2 Docker Deployment
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8088", "run:app"]
```

10. Bảo Trì và Cập Nhật
10.1 Database Migrations
```bash
# Tạo migration mới
flask db migrate -m "Description of changes"

# Apply migrations
flask db upgrade

# Rollback
flask db downgrade
```

10.2 Backup
```bash
# Backup database
sqlite3 lichviet.db .dump > backup.sql

# Restore database
sqlite3 lichviet.db < backup.sql
```

11. Contributing
Hướng dẫn đóng góp cho dự án:

- Fork repository
- Tạo branch mới
- Commit changes
- Push to branch
- Tạo Pull Request

12. License
MIT License - Copyright (c) 2025 ndlong78
```
