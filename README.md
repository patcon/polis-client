# polis-clients

OpenAPI-generated client libraries for interacting with Pol.is servers from Python or Typescript.

## The Client Libraries

### polis-client-py

See: [`python/README.md`](./python/README.md)

### polis-client-ts

Works on either backend server (Node) or frontend client (browser).

See: [`typescript/README.md`](./typescript/README.md)

## Development

Each of these client libraries is composed mostly of code auto-generated
from the OpenAPI spec available at [`openapi/polis.yml`](./openapi/polis.yml).

As such please do not modify any code in these locations:
- `python/src/polis_client/generated/`
- `typescript/src/polis_client/generated/` (and `typescript/dist/`)

To regenerate, run:

```
make regenerate
```

## License

The project is under the terms of the MIT License.
