#!/usr/bin/env python
import os
import sys

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourist_places_explorer.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError("Couldn't import Django") from exc
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

# ✅ TEMPORARY CODE: auto-create or reset admin account
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourist_places_explorer.settings')
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

username = "admin"
password = "nafisa1705"
email = "admin@example.com"

try:
    user, created = User.objects.get_or_create(username=username, defaults={"email": email})
    user.set_password(password)
    user.is_superuser = True
    user.is_staff = True
    user.save()
    if created:
        print("✅ Superuser 'admin' created successfully.")
    else:
        print("✅ Superuser 'admin' password reset successfully.")
except Exception as e:
    print("⚠️ Error while creating superuser:", e)
