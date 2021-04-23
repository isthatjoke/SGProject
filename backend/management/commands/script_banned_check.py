from django.core.management import BaseCommand
from authapp.models import HubUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        users = HubUser.objects.exclude(banned=HubUser.BANNED_FALSE)




