# polis-client-py

An unofficial Python API client for communicating with any Polis servers.

It will start off as read-only, but I intend to add helpers for handling
POST requests via xid, and maybe jwt.

This will eventually be used in the `red-dwarf` algorithm library,
doing much of the work of that library's current "data loader".

## Installation

```
pip install git+https://github.com/patcon/polis-client
```

## Usage

See: [`examples.ipynb`](examples.ipynb)

## File Structure

```
./polis-client/
├── Makefile                    # Shared: Build scripts
├── README.md                   # Shared: Main project README
├── openapi
│   └── polis.yml               # Shared: OpenAPI spec
├── pyproject.toml              # Python dependencies
└── python
    ├── README.md               # Python client README
    ├── debug.py                # Messy testing file
    ├── examples.ipynb          # Primary documentation
    └── src
        └── polis_client
            ├── client.py       # Custom Python thin client
            └── generated/      # Auto-generated client code
```

## Development

(We use `uv`, but you can use any Python environment.)

This project is structured around an OpenAPI definition at `../openapi/polis.yml`,
from which most of the code in this repository is auto-generated.

We have written a thin custom client around the auto-generated client code
that is built (from the repository root) with:

    $ uv run make regenerate-py

This command must be run whenever you update the YAML spec file. For legibility
of commit history, any updates to auto-generated should be committed in a batch
separate from your own changes. (e.g. "Adding auto-generated code.")
