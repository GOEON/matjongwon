from django.core.management.base import BaseCommand
import threading 

timer = None

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            '--stop',
            action ='store_true',
            help = 'Stop the periodic execution of the loadjson command',
        )

    def handle(self, *argc, **options):
        global timer
        if options.get('stop'):
            if timer:
                # Stop the timer if it's running
                timer.cancel()
                timer = None
                self.stdout.write(self.style.SUCCESS('Stopped loadjson command.'))
            else:
                def run_loadjson():
                    global timer
                    # Run the loadjson command every 24 hours
                    timer = threading.Timer(86400, run_loadjson)
                    timer.start()
                    self.stdout.write(self.style.SUCCESS('Running loadjson command...'))
                    call_command('loadjson')
                run_loadjson()
