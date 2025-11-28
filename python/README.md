# polis-client-py

An unofficial Python API client for communicating with any Polis servers.

It will start off as read-only, but I intend to add helpers for handling
POST requests via xid, and maybe jwt.

This will eventually be used in the `red-dwarf` algorithm library,
doing much of the work of that library's current "data loader".

## Installation

```
uv add git+https://github.com/patcon/polis-client.git@main#subdirectory=python
```

## Usage

See: [`examples.ipynb`](examples.ipynb)

## Development

This project is structured around an OpenAPI definition at `../openapi/polis.yml`.

(We use `uv`, but you can use any virtualenv or not as a Python environment.)

We have written a thin custom client around the auto-generated client code
that is built (from the repository root) with:

    $ uv run make regenerate-py

This command must be run whenever you update the YAML spec file, and
the generated code committed.
