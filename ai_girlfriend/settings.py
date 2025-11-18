# ai_girlfriend/settings.py
import os
from pathlib import Path
from dotenv import load_dotenv

# ✅ এটি নিশ্চিত করুন যে .env ফাইলটি প্রজেক্ট রুটে আছে
# এটি ফাইল লোড করবে
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

# সিকিউরিটির জন্য .env থেকে SECRET_KEY লোড করুন
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'default-insecure-key-dont-use-in-production') 
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'core',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ai_girlfriend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "core/templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'ai_girlfriend.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

STATIC_URL = '/static/'

# ✅ GEMINI_API_KEY লোড করুন। যদি লোড না হয়, আপনার দেওয়া কী-টি ব্যবহার করুন (অস্থায়ীভাবে)
# 🛑 IMPORTANT: Replace 'YOUR_FALLBACK_API_KEY' with your actual key if the code still fails.
# Since you confirmed the key:
FALLBACK_KEY = 'AIzaSyA2_wtgfp8VHVx7J4GfSqmRwyVeqcMjltg' 
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", FALLBACK_KEY)