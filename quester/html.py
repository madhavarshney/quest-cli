import textwrap
import tempfile


def create_html_file(quest_name, results):
    html = _generate_html_content(quest_name, results)

    temp_file = tempfile.NamedTemporaryFile(prefix='quest-', suffix='.html', mode='w', delete=False)
    temp_file.write(html)
    temp_file.flush()

    return temp_file


def _generate_html_content(quest_name, output):
    return textwrap.dedent(f"""
    <!DOCTYPE html>
    <html>
        <head>
            <title>Quest</title>
            <style>
                html {{
                    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif, "Apple Color Emoji", "Segoe UI Emoji", "Segoe UI Symbol";
                }}
                html, body {{
                    margin: 0;
                    padding: 0;
                }}
                body {{
                    padding: 1em;
                }}
                .results {{
                    display: grid;
                    grid-template-columns: 1fr 1fr;
                    gap: 2em;
                }}
                pre {{
                    white-space: pre-wrap;`
                }}
            </style>
        </head>

        <body>
            <h1>{quest_name.title()}</h1>
            <div class="results">
                <div>
                    <h2>Build Output</h2>
                    <div>{output['b']}</div>
                    <h2>Test Output</h2>
                    <div>{output['t']}</div>
                </div>
                <div>
                    <h2>Memory Check</h2>
                    <div>{output['m']}</div>
                    <h2>Additional Info</h2>
                    <div><pre>{output['s']}</pre></div>
                </div>
            </div>
        </body>
    </html>
    """)
