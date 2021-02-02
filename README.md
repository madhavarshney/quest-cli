# `quest-cli`

A CLI to [quest](https://quests.nonlinearmedia.org/) faster & more efficiently, built for power users.

## Setup

*Note: this is currently a developer-oriented setup and not meant for the general public—but wait, aren't questers developers?*

Install Python 3.7+, then install `requests`:

```sh
python3 -m pip install requests
```

Clone the repo:

```sh
git clone https://github.com/madhavarshney/quest-cli.git
cd quest-cli
```

## Usage

### Running the CLI

Here's how to run the CLI:

```bash
./quest-cli.py # for 'nix systems (linux/macOS)
python3 ./quest-cli.py # for everywhere (including Windows)
```

*TODO: Add setup steps for directly running the CLI with `$ quest-cli [...]`.*

### Interactive Mode (AKA a shell)

If you run the CLI without any options, it will start an interactive shell. Here's how to use it:

Command | Utility
------- | ---------
`help [<COMMAND>]` | Get help, optionally for a particular comamnd
`handle <ID>` | Set your secret handle (usually student ID)
`quest <NAME>` | Start working on a quest
`trophies` | View your loot / trophies
`spec` | Open the quest spec (PDF)
`submit <PATH> [<PATH>]` | Submit your code, run the tests, and view results

<details>
<summary>Show it to me!</summary>

```bash
# Start the interactive shell
~/quest-cli $ python3 ./quest-cli.py

# Set your secret handle to `12345678`
> handle 12345678

# Check current loot
12345678 > trophies
A Very Cool CLI - 8
A Tiger Named Fangs - 0

# Let's quest 'A Tiger Named Fangs'
12345678 > quest A Tiger Named Fangs

# Open the quest spec
12345678 on A Tiger Named Fangs > spec

# Upload and test code, then show results
12345678 on A Tiger Named Fangs > submit ../cs2a/helloworld.cpp ../cs2a/helloworld.h

# Let's check our loot again!
12345678 on A Tiger Named Fangs > trophies
A Very Cool CLI - 8
A Tiger Named Fangs - 1

# Alright, we're done for the day
12345678 on A Tiger Named Fangs > exit

# Back to main shell
~/quest-cli $
```

</details>

### CLI Commands

You can also use the CLI commands directly (WIP). View the help text with `python3 ./quest-cli.py --help`.

<details>
<summary>Examples</summary>

```bash
~/quest-cli $ python3 ./quest-cli.py --help
# ... a bunch help text ...

~/quest-cli $ python3 ./quest-cli.py submit --name "A Tiger Named Fangs" --handle 12345678 --files ../cs2a/helloworld.cpp ../cs2a/helloworld.h
# ... submission output ...
```

</details>

## About

*More info TBA.*
