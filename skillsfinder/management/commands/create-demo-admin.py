from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.db import transaction

User = get_user_model()


class Command(BaseCommand):
    help = """
    Creates demo admin user
    """

    def add_arguments(self, parser):
        parser.add_argument('-u', '--username', default='admin', required=False)
        parser.add_argument('-p', '--password', default='admin', required=False)

    @transaction.atomic()
    def handle(self, *args, username, password, **options):
        User.objects.create_user(username=username, password=password, is_staff=True, is_superuser=True)
