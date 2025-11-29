import { client as GeneratedClient } from "./generated/client.gen.js";
import * as Comments from "./generated/sdk.gen.js";
import * as Reports from "./generated/sdk.gen.js";
import * as Conversations from "./generated/sdk.gen.js";
import * as Math from "./generated/sdk.gen.js";
import * as Votes from "./generated/sdk.gen.js";
import * as Initialization from "./generated/sdk.gen.js";
export const DEFAULT_BASE_URL = "https://pol.is";
export class PolisClient {
    constructor(options) {
        this.token = null;
        const { baseUrl = DEFAULT_BASE_URL, xid, headers } = options ?? {};
        this.baseUrl = `${baseUrl}/api/v3`;
        this.xid = xid;
        // configure the internal generated client once
        GeneratedClient.setConfig({
            baseUrl: this.baseUrl,
            headers,
        });
        // Request interceptor: inject auth and optional X-Id header
        GeneratedClient.interceptors.request.use(async (req) => {
            // Ensure token before sending request
            if (!this.token) {
                await this.fetchToken(req.url); // lazy token init
            }
            if (this.token) {
                req.headers.set("Authorization", `Bearer ${this.token}`);
            }
            return req;
        });
    }
    async fetchToken(conversationUrl) {
        // Extract conversationId if needed
        const conversationId = this.extractConversationId(conversationUrl);
        const res = await Initialization.getInitialization({
            query: { conversation_id: conversationId ?? "" },
        });
        this.token = res.data?.auth?.token ?? null;
    }
    extractConversationId(url) {
        // crude example: parse conversation_id from query string
        if (!url)
            return undefined;
        const match = url.match(/[?&]conversation_id=([^&]+)/);
        return match ? decodeURIComponent(match[1]) : undefined;
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
            query: {
                conversation_id: conversationId,
                ...defaultQuery,
                ...extraQuery,
            },
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
    async getInitialization(conversationId, extraQuery = {}) {
        const res = await Initialization.getInitialization({
            query: { conversation_id: conversationId, ...extraQuery },
        });
        return res.data;
    }
}
//# sourceMappingURL=index.js.map