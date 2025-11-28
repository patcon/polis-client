# polis-client-ts

An unofficial Typescript API client for communicating with any Polis servers.

(Supports running from node or browser.)

To be completed.

## Installation

```
npm install patcon/polis-client#main
```

## Usage

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

## Development

From the root directory, run

```
make regenerate-ts
```