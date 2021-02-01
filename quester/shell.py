import os
import cmd
import shlex

from .quest_utils import open_spec, get_trophy_data
from .commands import submit
from .term_utils import colorize

try:
    import readline
except ImportError:
    readline = None

histfile = os.path.expanduser('~/.quester_history')
histfile_size = 1000


class QuesterShell(cmd.Cmd):
    prompt = '> '
    ruler = '-'
    doc_header = "Commands (type help <command>):"

    # Shell state
    current_quest = None
    current_handle = None

    def preloop(self):
        if readline and os.path.exists(histfile):
            readline.read_history_file(histfile)

    def postloop(self):
        if readline:
            readline.set_history_length(histfile_size)
            readline.write_history_file(histfile)

    def cmdloop(self, intro=None):
        while True:
            try:
                super().cmdloop(intro=intro)
                break
            except KeyboardInterrupt:
                print("")
        self.postloop()

    def emptyline(self):
        pass

    def do_quest(self, arg):
        """Set a quest."""

        if not arg:
            print('Error: no quest name specified')
            return

        self.current_quest = arg
        self._set_prompt()

    def do_handle(self, arg):
        """Set a quest handle."""

        if not arg:
            print('Error: no handle specified')
            return

        self.current_handle = arg
        self._set_prompt()

    def do_trophies(self, arg):
        """View trophies for the current handle."""
        if not self.current_handle:
            print('Error: questing handle is not set')
            return

        trophy_data = get_trophy_data(self.current_handle)

        if trophy_data:
            for name, attempts in trophy_data.items():
                print(f'{name} - {list(attempts[0].values())[0]}')
        else:
            print('Nothing found!')

    def do_spec(self, arg):
        """Open the quest spec"""
        if not self.current_quest:
            print('Error: quest name is not set')
            return

        open_spec(self.current_quest.lower())

    def do_submit(self, arg):
        """Submit files for quest."""

        if not self.current_handle or not self.current_quest:
            print('Error: handle or quest name not specified')
            return

        files = shlex.split(arg)

        if not len(files):
            print('Error: submission files not specified')
            return

        submit(self.current_quest, files, self.current_handle)

    def do_exit(self, arg):
        """Exit the shell."""
        return True

    def do_EOF(self, arg):
        """Exit the shell."""
        return True

    def _set_prompt(self):
        handle_info = f'{colorize("1;32;49m", self.current_handle)} ' if self.current_handle else ''
        quest_info = f'on {colorize("1;36;49m", self.current_quest)} ' if self.current_quest else ''
        self.prompt = f'{handle_info}{quest_info}> '
