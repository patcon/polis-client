# python-polis-client

This is a stub of a Python client for communicating with a Polis server API.

It will start off as read-only, but I intend to add helpers for handling
POST requests via xid, and maybe jwt.

This will eventually be used in the `red-dwarf` algorithm library,
doing much of the work of that library's current "data loader".

## Installation

```
uv add git+http://github.com/patcon/polis-client.git@main
```

## Usage

```py
from polis_client import PolisClient

polis = PolisClient()

comments = polis.get_comments(conversation_id="2demo")
if isinstance(comments, list) and len(comments) > 0:
    print(comments[0].to_dict())

report = polis.get_report(report_id="r2dfw8eambusb8buvecjt")
if report:
    print(report.to_dict())

conversation = polis.get_conversation(conversation_id="2demo")
if conversation and not isinstance(conversation, str):
    print(conversation.to_dict())

math = polis.get_math(conversation_id="2demo")
print(math)

votes = polis.get_votes(conversation_id="2demo", pid=10)
if isinstance(votes, list) and len(votes) > 0:
    print(votes[0].to_dict())
```

## Development

This project is structured around an OpenAPI definition at `openapi/polis.yml`.

We have written a thin custom client around the auto-generated client code
that is built with:

    $ uv run make regenerate

This command must be run whenever you update the YAML spec file, and
the generated code committed.