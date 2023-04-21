from django.core.management.base import BaseCommand
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import timedelta

class Command(BaseCommand):
        def handle(self, *args, **options):
        # Delete expired sessions
            expired_sessions = Session.objects.filter(expire_date__lte=timezone.now())
            expired_sessions.delete()
            # Delete inactive users
            retention_period = timedelta(minutes=10)
            inactive_users = User.objects.filter(last_login__lt=timezone.now() - retention_period)
            inactive_users.delete()
            self.stdout.write('Cleanup complete')