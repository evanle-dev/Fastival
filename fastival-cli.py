import subprocess
import sys

import inquirer

RUN_SERVER = 'run server'
DO_SEEDER = 'do seeder'
DO_MIGRATION = 'do migration'

choices = [
    RUN_SERVER,
    DO_SEEDER,
    DO_MIGRATION
]

questions = [
    inquirer.List(
        name='task',
        message="What do you want to do?",
        choices=choices,
    ),
]
answers = inquirer.prompt(questions)

if answers['task'] == RUN_SERVER:
    try:
        subprocess.call(['sh', './scripts/runserver.sh'])
    except KeyboardInterrupt:
        sys.exit(0)
