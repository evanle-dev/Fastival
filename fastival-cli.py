#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import subprocess
import sys

import inquirer

from api import settings

RUN_SERVER = 'run server'
UP_MIGRATION = 'up migration'
UP_SEEDER = 'up seeder'
DOWN_MIGRATION = 'down migration'
DOWN_SEEDER = 'down seeder'
GET_VERSION = 'get version'

choices = [
    RUN_SERVER,
    UP_MIGRATION,
    DOWN_MIGRATION,
    UP_SEEDER,
    DOWN_SEEDER,
    GET_VERSION,
]

questions = [
    inquirer.List(
        name='task',
        message="What do you want to do?",
        choices=choices,
    ),
]

answers = inquirer.prompt(questions)

if answers is None:
    sys.exit(0)

if answers['task'] == RUN_SERVER:
    try:
        subprocess.call(['sh', './scripts/runserver.sh'])
    except KeyboardInterrupt:
        sys.exit(0)

elif answers['task'] == GET_VERSION:
    print('Current version is', settings.version)
