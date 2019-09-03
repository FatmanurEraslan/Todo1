import os
import sys
import todo

from argparse import ArgumentParser

FILE_NAME = sys.argv[0].split("/")[-1]
STORAGE = {
    'active_path': '{}/.todo-list-active'.format(os.environ.get('HOME')),
    'completed_path': '{} /.todo-list-completed'.format(os.environ.get('HOME')),
}
HELPS = {
    'command': '{} add | list | complete | completed'.format(FILE_NAME),
    'add': "{} add 'My new task' 'Other task' 'more' or single item".format(FILE_NAME),
    'complete': "{} complete 1".format(FILE_NAME),
    'params': 'can be a task (string) or index (int)',
}


def main(argv=None):
    if argv is None:
        argv = sys.argv

    command_choices = ['list', 'add', 'complete', 'completed']

    parser = ArgumentParser(prog=FILE_NAME)
    parser.add_argument('command',
                        choices=command_choices,
                        type=str, nargs='?',
                        help=HELPS['command'])
    parser.add_argument('params',
                        type=str,
                        nargs='*',
                        help=HELPS['params'])
    parser.add_argument('-v',
                        '--version',
                        action='version',
                        version=todo.VERSION)

    args = parser.parse_args()
    if args.command is None:
        parser.print_help()

    def read_list(storage=STORAGE['active_path']):
        try:
            with open(storage, 'r') as f:
                lines = f.readlines()
            return [line.strip() for line in lines]
        except FileNotFoundError:
            return []

    def update_file(data, storage=STORAGE['active_path']):
        if len(data) == 0:
            with open(storage, 'w') as f:
                pass
            return

            mode = 'w'
            if not os.path.exists(storage):
                mode = 'a'

            with open(Storage, mode) as f:
                for line in data:
                    f.write(line + '\n')

    if args.command == 'add':
        if not args.params:
            print('please enter your task.\n\t{}'.format(HELPS['add']))
            return

        todo.Todo.items = read_list()
        messages = []
        for task in args.params:
            status, message = todo.Todo.add(task)
            messages.append(message)
            if status:
                update_file(todo.Todo.items)
        if len(messages) > 0:
            for message in messages:
                print(message)
            todo.Todo.list
    if args.command == 'list':
        print('Current Tasks:')
        todo.Todo.items = read_list()
        todo.Todo.list

    if args.command == 'completed':
        todo.Todo.completed = read_list((STORAGE['completed_path']))
        todo.Todo.completed_list()

    if args.command == 'complete':
        if not args.params:
            print('Please enter index. \n\t{}'.format(HELPS['complete']))
            return
        todo.Todo.items = read_list()
        todo.Todo.completed = read_list(STORAGE['completed_path'])

    return 0


if __name__ == "__main__":
    sys.exit(main())
