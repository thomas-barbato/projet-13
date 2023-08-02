from django.core.management.utils import get_random_secret_key

with open(".env", "w") as f:
    f.write(f"DJANGO_SECRET_KEY={get_random_secret_key()}\n")
    f.write(
        "SENTRY_DSN=https://8818e1035f7441f4bb83c122d9388456@o4505601723269120.ingest.sentry.io"
        "/4505624010227712"
    )
    f.close()

print(".env creation done")
