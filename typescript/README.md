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
- [ ] POST votes
- [ ] GET xids
- [ ] support for xid "authentication"
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

See: https://jsfiddle.net/5wL6xcum/1/

```js
// Use an ESM CDN URL pointing to your built file
import { PolisClient } from "https://cdn.jsdelivr.net/gh/patcon/polis-client@main/typescript/dist/index.js";

const DEFAULT_BASE_URL = "https://pol.is/api/v3";
const PROXIED_BASE_URL = `https://corsproxy.io/?url=${DEFAULT_BASE_URL}`;

const convoId = "2demo";
const polis = new PolisClient({ baseUrl: PROXIED_BASE_URL });
const comments = await polis.getComments(convoId);
console.log("Comments:", comments);
```

## Development

From the root directory, run

```
make regenerate-ts
```