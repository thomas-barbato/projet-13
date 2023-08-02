from django.core.management.utils import get_random_secret_key

with open(".env", "w") as f:
    f.write(f"DJANGO_SECRET_KEY={get_random_secret_key()}\n")
    f.write("SENTRY_DSN=\n")
    f.close()

print(".env creation done")
