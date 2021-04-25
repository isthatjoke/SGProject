from datetime import datetime

import pytz
from django.conf import settings

from django.core.management import BaseCommand
from authapp.models import HubUser


class Command(BaseCommand):

    def handle(self, *args, **options):
        now = datetime.now(pytz.timezone(settings.TIME_ZONE))
        users = HubUser.objects.filter(banned=HubUser.BANNED_FOR_TIME).filter(banned_to__gte=now)
        if users:
            for user in users:
                user.banned = HubUser.BANNED_FALSE
                user.banned_to = None
                user.save()


