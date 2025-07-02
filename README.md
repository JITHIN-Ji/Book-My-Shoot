📸 Book My Shoot – Django Photography Booking Web App

This is a Django-based web application designed to manage a photography service platform. Admins can manage services, users, bookings, and video uploads. Users can register, book services, make payments, and view uploaded work.

---

## 🔧 Features

### 👤 User Module:
- Register & login
- Browse categories and services
- Book events (date & venue)
- Make payments (advance/full)
- View uploaded video/photos
- Submit feedback

### 🛠 Admin Module:
- Admin login
- Manage users, categories & services
- View, approve, or delete bookings
- Track and mark payment status
- Upload videos/photos after events
- View feedback from users

---

## 📁 Folder Structure

bookshoot/ # Main Django project folder
├── book/ # Django app with views, models, and templates
├── templates/ # HTML templates
├── static/ # CSS, JS, videos, images
├── manage.py # Django project runner
└── db.sqlite3 # SQLite database

yaml
Copy
Edit

---

## 🚀 How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/JITHIN-ji/Book-My-Shoot.git
   cd Book-My-Shoot
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run migrations:

bash
Copy
Edit
python manage.py makemigrations
python manage.py migrate
Start the server:

bash
Copy
Edit
python manage.py runserver
Open in browser:
http://127.0.0.1:8000/
