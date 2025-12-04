# polis-client-ts

An unofficial Typescript API client for communicating with any Polis servers.

(Supports running from node or browser.)

To be completed.

## Features

- [x] GET conversation
- [x] GET report
- [x] GET math
- [x] GET comments
- [ ] POST comments
- [x] GET votes
- [x] POST votes
- [x] GET xids
- [x] support for xid "authentication"
- [ ] support for JWT authentication
- [ ] simple auto-proxy for browser clients
- [ ] create new conversations (unauthenticated, via "site_id")
- [ ] download export CSVs (from report_id)

## Installation

```
npm install github:patcon/polis-client
```

## Usage

### Node

```js
import { PolisClient } from "polis-client";

const polis = new PolisClient();

// Fetch comments
const comments = await polis.getComments("2demo");
console.log("Comments:", comments);
// Example return:
// [
//   { txt: "I imagine new businesses...", tid: 0, created: "1403054214174", is_seed: false, is_meta: false, pid: 0 },
//   ...
// ]
//
// Or for less data returned (like in the raw API response):
// const comments = await polis.getComments(
//     "2demo",
//     {
//         moderation: false,
//         include_voting_patterns: false,
//     }
// );

// Fetch report
const report = await polis.getReport("r68fknmmmyhdpi3sh4ctc");
console.log("Report:", report);
// Example return:
// { report_id: "r68fknmmmyhdpi3sh4ctc", created: '1515990588733', conversation_id: '3ntrtcehas', ... }

// Fetch conversation
const convo = await polis.getConversation("2demo");
console.log("Conversation:", convo);
// Example return:
// { topic: "$15/hour", description: "'How do you think the...", participant_count: 6357, ... }

// Fetch math
const math = await polis.getMath("2demo");
console.log("Math:", math);
// Example return:
// { group-clusters: {...}, base-clusters: {...}, group-aware-consensus: {...}, ... }
```

### Browser

See: https://jsfiddle.net/patcon/yjq2aebh/latest

```js
// Use an ESM CDN URL pointing to your built file
import { PolisClient } from "https://cdn.jsdelivr.net/gh/patcon/polis-client@main/typescript/dist/index.js";

const DEFAULT_BASE_URL = "https://pol.is";
const PROXIED_BASE_URL = `https://corsproxy.io/?url=${DEFAULT_BASE_URL}`;
const CONVO_ID = "2demo";

const polis = new PolisClient({ baseUrl: PROXIED_BASE_URL });
const comments = await polis.getComments(CONVO_ID);
console.log("Comments:", comments);
```

## File Structure

```
./polis-client/
├── Makefile                    # Shared: Build scripts
├── README.md                   # Shared: Main project README
├── openapi
│   └── polis.yml               # Shared: OpenAPI spec
├── package.json                # Helper file to assist npm install
└── typescript
    ├── README.md               # JS/TS client README
    ├── debug.ts                # Messy testing file
    ├── dist/                   # Built JS files for CDN install
    ├── openapi-ts.config.ts    # Build tool config
    ├── package.json            # Javascript dependencies
    ├── src
    │   └── polis_client
    │   └── polis_client
    │       ├── generated/      # Auto-generated client code
    │       ├── globals.d.ts    # Bugfix
    │       └── index.ts        # Custom Typescript thin client
    └── tsconfig.json           # TS config file
```

## Development

From the root directory, run

```
make regenerate-ts
```