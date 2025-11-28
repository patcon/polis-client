import { client as GeneratedClient } from "./generated/client.gen.js";
import * as Comments from "./generated/sdk.gen.js";
import * as Reports from "./generated/sdk.gen.js";
import * as Conversations from "./generated/sdk.gen.js";
import * as Math from "./generated/sdk.gen.js";
import * as Votes from "./generated/sdk.gen.js";
export const DEFAULT_BASE_URL = "https://pol.is/api/v3";
export class PolisClient {
    constructor(options) {
        const { baseUrl = DEFAULT_BASE_URL, headers = {} } = options ?? {};
        // configure the internal generated client once
        GeneratedClient.setConfig({
            baseUrl,
            headers,
        });
    }
    // -------------------------------
    // Instance methods — Python style
    // -------------------------------
    async getComments(conversationId, extraQuery = {}) {
        const defaultQuery = {
            // Normally false by default.
            moderation: true,
            include_voting_patterns: true,
        };
        const res = await Comments.getComments({
            query: { conversation_id: conversationId, ...extraQuery },
        });
        return res.data;
    }
    async getReport(reportId, extraQuery = {}) {
        const res = await Reports.getReport({
            query: { report_id: reportId, ...extraQuery },
        });
        // Python version extracts the first item; do same here:
        const arr = res.data;
        return Array.isArray(arr) ? arr[0] : arr;
    }
    async getConversation(conversationId, extraQuery = {}) {
        const res = await Conversations.getConversation({
            query: { conversation_id: conversationId, ...extraQuery },
        });
        return res.data;
    }
    async getMath(conversationId, extraQuery = {}) {
        const res = await Math.getMath({
            query: { conversation_id: conversationId, ...extraQuery },
        });
        return res.data;
    }
    async getVotes(conversationId, extraQuery = {}) {
        const res = await Votes.getVotes({
            query: { conversation_id: conversationId, ...extraQuery },
        });
        return res.data;
    }
}
//# sourceMappingURL=index.js.map