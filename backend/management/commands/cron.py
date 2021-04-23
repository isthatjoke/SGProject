from django.core.management import BaseCommand
from crontab import CronTab
import os


class Command(BaseCommand):
    path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    python = os.path.join(path, 'venv', 'bin', 'python3')
    mng = os.path.join(path, 'manage.py')
    script = os.path.join(path, 'backend', 'management', 'commands', 'script_banned_check.py')

    def handle(self, *args, **options):
        cron = CronTab(user='tzverev')
        job = cron.new(command=f'{self.python} {self.mng} {self.script}')
        job.minute.every(1)
        cron.write()
        print('job was added to cron')




# path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
# print(path)


