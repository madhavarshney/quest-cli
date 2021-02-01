import os
import textwrap
import tempfile
import webbrowser

from .quest_utils import get_trophy_data, upload, run_tests
from .html import create_html_file


def submit(quest_name, files, handle_id):
    print(f"[quest] {quest_name.title()}")
    print(f"[quest] Files: {', '.join(files)}")

    upload_id = upload(quest_name, files, handle_id)
    results = run_tests(upload_id)
    html_file = create_html_file(quest_name, results)

    _print_result(results, html_file.name)
    webbrowser.open('file://' + os.path.realpath(html_file.name))


def _print_result(results, html_file_name):
    print(
f"""
{textwrap.indent(_clean(results['b']), '[build] ', lambda line: True)}

{textwrap.indent(_clean(results['t']), '[test] ', lambda line: True)}

See more at {html_file_name}
"""
    )


def _clean(text: str) -> str:
    return text.replace('<PRE>', '').replace('</PRE>', '').replace('\n\n', '\n').strip()
