import os
import re
import urllib
import requests
import webbrowser

from .term_utils import spinner

BASE_URL = 'https://quests.nonlinearmedia.org'


def get_trophy_data(quest_handle):
    res = requests.post(f'{BASE_URL}/q/php/get-scores.php', data={'i': quest_handle})
    res.raise_for_status()

    return res.json()


def open_spec(quest_name):
    query = urllib.parse.urlencode({"id": quest_name.lower()})
    webbrowser.open(f'{BASE_URL}/php/q-get-spec.php?{query}')


def upload(quest_name, files, handle_id):
    res = requests.post(
        f'{BASE_URL}/php/q-upload.php',
        files={f'file[{idx}]': _parse_file(path, handle_id) for idx, path in enumerate(files)},
        data=[('id', quest_name.lower())] * len(files)
    )
    res.raise_for_status()
    data = res.json()

    print(f'[quest] Uploaded code (ID is {data["code"]})')

    return data['code']


def run_tests(upload_id):
    with spinner('[quest] Running tests', '[quest] Ran tests'):
        res = requests.post(f'{BASE_URL}/php/q-do-code-test.php', data={'code': upload_id})

    res.raise_for_status()

    data = res.json()
    return data


def _parse_file(filepath, handle_id):
    f = open(filepath, 'r')
    content = f.read()

    if handle_id:
        content = re.sub(r'^\/\/ ?Student ID: .*$', f'// Student ID: {handle_id}', content, flags=re.MULTILINE)

    return (os.path.basename(filepath), content)
