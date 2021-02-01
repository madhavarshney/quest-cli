import argparse

from .shell import QuesterShell
from .commands import submit


def setup_argparse():
    parser = argparse.ArgumentParser(description='Quest away')
    subparsers = parser.add_subparsers(dest='command')

    parser_submit = subparsers.add_parser('submit', help='Submit your code for a quest')
    parser_submit.add_argument('-N', '--name', help='The quest name', metavar='Quest', required=True)
    parser_submit.add_argument('-F', '--files', help='Code files to submit', nargs='+', metavar='File', required=True)
    parser_submit.add_argument('-H', '--handle', help='Your secret handle', metavar='ID', required=True)

    return parser


def run_command(args):
    if args.command == 'submit':
        quest_name = args.name
        files = args.files
        handle_id = args.handle

        submit(quest_name, files, handle_id)
    else:
        print(args)


def init():
    parser = setup_argparse()
    args = parser.parse_args()

    if not args.command:
        QuesterShell().cmdloop()
    else:
        run_command(args)


if __name__ == '__main__':
    init()
