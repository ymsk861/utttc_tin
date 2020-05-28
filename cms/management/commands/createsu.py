from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        if not User.objects.filter(username="utttc").exists():
            User.objects.create_superuser(username="utttc", email="yamasaki-shun219@g.ecc.u-tokyo.ac.jp", password="Akamon_0285")
            self.stdout.write(self.style.SUCCESS('Successfully created new super user'))