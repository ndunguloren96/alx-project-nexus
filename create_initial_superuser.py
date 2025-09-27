# create_initial_superuser.py
import os
import django
import sys

# Point to your project's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pollProject.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

superuser_username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin')
superuser_email = os.environ.get('DJANGO_SUPERUSER_EMAIL', 'admin@example.com')
superuser_password = os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'adminpass')

if not User.objects.filter(username=superuser_username).exists():
    try:
        print(f"Creating superuser '{superuser_username}'...")
        User.objects.create_superuser(
            username=superuser_username,
            email=superuser_email,
            password=superuser_password
        )
        print("Superuser created successfully.")
    except Exception as e:
        print(f"Error creating superuser: {e}", file=sys.stderr)
else:
    print(f"Superuser '{superuser_username}' already exists. Skipping creation.")

