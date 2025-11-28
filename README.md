# polis-clients

OpenAPI-supported client libraries for interacting with Polis servers in Python and Typescript.

## The Client Libraries

### polis-client-py

See: [`README.python.md`](./README.python.md)

### polis-client-ts

See: [`README.typescript.md`](./README.typescript.md)

## Development

Each of these client libraries is composed mostly of code auto-generated
from the OpenAPI spec available at [`openapi/polis.yml`](./openapi/polis.yml).

As such please do not modify any code in these locations:
- `src/polis_client/generated/`
- `typescript/polis_client/generated/`

To regenerate, run:

```
uv run make regenerate
```