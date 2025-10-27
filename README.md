# 🌍 Tourist Places Explorer

A modern Django web application for exploring and discovering amazing tourist destinations around the world.

## ✨ Features

- 🏞️ **Browse Tourist Places**: Explore beautiful destinations with detailed information
- 🔍 **Advanced Search**: Search by name, city, or category
- 👤 **User Authentication**: Sign up, login, and manage your profile
- 📧 **Contact Form**: Get in touch with the team
- 📱 **Responsive Design**: Beautiful UI that works on all devices
- 🎨 **Modern UI**: Gradient backgrounds, animations, and smooth transitions

## 🚀 Tech Stack

- **Backend**: Django 5.1
- **Frontend**: Bootstrap 5.3, Bootstrap Icons
- **Database**: SQLite (development), PostgreSQL (production)
- **Deployment**: Render-ready with gunicorn and whitenoise

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/tourist-places-explorer.git
   cd tourist-places-explorer
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   venv\Scripts\activate  # Windows
   # or
   source venv/bin/activate  # Linux/Mac
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**
   ```bash
   python manage.py runserver
   ```

7. **Access the application**
   - Home: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## 📁 Project Structure

```
tourist-places-explorer/
├── places/          # Tourist places app
├── users/           # User authentication
├── contact/         # Contact form
├── static/          # CSS, JS, images
├── templates/       # Base templates
├── media/           # User uploads
└── tourist_places_explorer/  # Main settings
```

## 🌐 Deployment

This project is configured for deployment on **Render**:

1. **Create a new Web Service on Render**
2. **Connect your GitHub repository**
3. **Build command**: `chmod +x build.sh && ./build.sh`
4. **Start command**: `gunicorn tourist_places_explorer.wsgi`
5. **Environment variables**:
   - `SECRET_KEY`: Your Django secret key
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: Your domain

## 📝 Configuration Files

- `requirements.txt` - Python dependencies
- `runtime.txt` - Python version
- `Procfile` - Process configuration for Render
- `build.sh` - Build script for deployment
- `.gitignore` - Git ignore rules

## 🎯 Usage

1. **Add Places**: Login as admin and add tourist places through the admin panel
2. **Browse**: Explore places on the homepage
3. **Search**: Use the search bar to find specific places
4. **Filter**: Filter by category or city
5. **View Details**: Click on any place to see detailed information

## 👤 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- Built with Django
- UI powered by Bootstrap
- Icons by Bootstrap Icons

---

Made with ❤️ for exploring the world

