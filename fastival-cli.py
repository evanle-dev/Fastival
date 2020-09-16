import subprocess

import inquirer

choices = [
    'run',
    'migrate',
    'seed'
]

questions = [
    inquirer.List('task',
                  message="What do you want to do?",
                  choices=choices,
                  ),
]
answers = inquirer.prompt(questions)

if answers['task'] == 'run':
    try:
        subprocess.call(['sh', './scripts/runserver.sh'])
    except KeyboardInterrupt:
        print('Interrupted')
