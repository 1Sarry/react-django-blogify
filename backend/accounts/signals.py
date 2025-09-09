from django.contrib.auth.models import User
from django.db.models.signals import post_migrate
from django.dispatch import receiver

@receiver(post_migrate)
def create_admin_user(sender, **kwargs):
    if sender.name == "auth":  # only after auth app is migrated
        if not User.objects.filter(username="admin").exists():
            User.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="SuperSecret123!"
            )
