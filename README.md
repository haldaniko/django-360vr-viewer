# 🌿 CalmSphere – MVP Landing Page

## 🎯 Purpose
- Provide immersive 360° video experiences for relaxation, meditation, and breathing exercises.  
- Deliver guided meditation instructions alongside spherical videos for a calming VR and browser experience.

## Installation

#### Manual
``` bash
git clone https://github.com/haldaniko/django-360vr-viewer.git
cd django-360vr-viewer

# on macOS
python3 -m venv venv
source venv/bin/activate

# on Windows
python -m venv venv
venv\Scripts\activate

pip install -r requirements.txt

# Copy .env.sample to .env and fill in required environment variables
cp .env.sample .env

python manage.py migrate
python manage.py runserver

Create admin user
python manage.py createsuperuser
```

#### Docker
``` bash
Not implemented yet
```

The web app will be available at `http://127.0.0.1:8000/`  
The admin dashboard at `http://127.0.0.1:8000/admin`