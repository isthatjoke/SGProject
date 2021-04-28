from django.core.management import BaseCommand
from crontab import CronTab
import os


class Command(BaseCommand):

    def handle(self, *args, **options):
        path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
        python = os.path.join(path, 'venv', 'bin', 'python3')
        mng = os.path.join(path, 'manage.py')
        script = 'script_banned_check'
        cron = CronTab(user='root')
        job = cron.new(command=f'{python} {mng} {script}  >>{path}/out.txt 2>&1')
        job.minute.every(1)
        cron.write()
        print('job was added to cron')




