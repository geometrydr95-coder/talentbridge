# talentbridge
 A Django platform that helps students showcase their sports and tech talents to get scholarships
# 🌟 TalentBridge

> Connecting student talent to scholarship opportunities.

TalentBridge is a web platform built with Django that helps students 
showcase their sports and tech talents to scouts and scholarship 
organizations. Students can upload videos, images, and descriptions 
of their talents, while scouts and organizations can browse and 
discover talented individuals.

---

## 🚀 Features

- 🎯 Student talent profiles with video and image uploads
- 🔍 Browse and search talents by category (Sport / Tech)
- 🏆 Scholarship listings with application system
- 👤 Role-based users (Student, Scout, Organization, Admin)
- 📊 Personal dashboard for students
- 🔐 Secure authentication system
- 📱 Fully responsive dark theme UI

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Django 4.2 |
| Database | MySQL (XAMPP) |
| Frontend | Bootstrap 5 |
| Icons | Bootstrap Icons |
| Fonts | Google Fonts (Poppins) |
| Server | Django Dev Server / Apache |

---

## 📁 Project Structure
```
talentbridge/
├── Talentbridge/          ← Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── talents/               ← Main app
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── admin.py
├── templates/             ← HTML templates
│   ├── base.html
│   └── talents/
│       ├── home.html
│       ├── register.html
│       ├── login.html
│       ├── dashboard.html
│       ├── talent_list.html
│       ├── talent_detail.html
│       ├── add_talent.html
│       ├── scholarship_list.html
│       └── scholarship_detail.html
├── media/                 ← Uploaded files
└── manage.py
```

---

## ⚙️ Installation & Setup

### Prerequisites
- Python 3.8+
- XAMPP (MySQL)
- pip

### 1. Clone the repository
```bash
git clone https://github.com/YOURUSERNAME/talentbridge.git
cd talentbridge
```

### 2. Install dependencies
```bash
pip install django==4.2 mysqlclient pillow
```

### 3. Create the database
Open phpMyAdmin at `http://localhost/phpmyadmin/` and run:
```sql
CREATE DATABASE talentbridge_db;
```

### 4. Configure database
Open `Talentbridge/settings.py` and update:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'talentbridge_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 5. Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create superuser
```bash
python manage.py createsuperuser
```

### 7. Run the server
```bash
python manage.py runserver
```

### 8. Visit the app
```
http://127.0.0.1:8000/
```

---

## 👥 User Roles

| Role | Permissions |
|------|------------|
| Student | Create profile, upload talents, apply for scholarships |
| Scout | Browse and discover talents |
| Organization | Post scholarships, view applicants |
| Admin | Full platform management |

---

## 📸 Pages

- **Home** — Landing page with featured talents
- **Register/Login** — Authentication system
- **Dashboard** — Personal student dashboard
- **Talents** — Browse all talents with search and filter
- **Talent Detail** — Full talent profile with media
- **Add Talent** — Upload talent with video/image
- **Scholarships** — Browse available scholarships
- **Scholarship Detail** — Full scholarship info with apply button

---

## 🎨 Color Theme

| Element | Color |
|---------|-------|
| Background | `#0f1117` |
| Card Background | `#1a1d27` |
| Primary Accent | `#7c6aff` |
| Sport Badge | `#ff6a3d` |
| Tech Badge | `#3daaff` |
| Text | `#e0e0e0` |

---

## 🔮 Future Improvements

- [ ] Email verification on registration
- [ ] Direct messaging between students and scouts
- [ ] Scholarship application tracking
- [ ] Student leaderboard
- [ ] Mobile app (React Native)
- [ ] AI-powered talent matching

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue 
first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author
Built with ❤️ by **Omullo**  
GitHub: [@YOURUSERNAME](https://github.com/geometrydr95-coder)

Built with ❤️ by **Blackman**  
GitHub: [@YOURUSERNAME](https://github.com/YOURUSERNAME)
