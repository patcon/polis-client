import { client as GeneratedClient } from "./generated/client.gen";
import * as Comments from "./generated/sdk.gen";
import * as Reports from "./generated/sdk.gen";
import * as Conversations from "./generated/sdk.gen";
import * as MathAPI from "./generated/sdk.gen";
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
    async getComments(conversationId) {
        const res = await Comments.getComments({
            query: { conversation_id: conversationId },
        });
        return res.data;
    }
    async getReport(reportId) {
        const res = await Reports.getReport({
            query: { report_id: reportId },
        });
        // Python version extracts the first item; do same here:
        const arr = res.data;
        return Array.isArray(arr) ? arr[0] : arr;
    }
    async getConversation(conversationId) {
        const res = await Conversations.getConversation({
            query: { conversation_id: conversationId },
        });
        return res.data;
    }
    async getMath(conversationId) {
        const res = await MathAPI.getMath({
            query: { conversation_id: conversationId },
        });
        return res.data;
    }
}
//# sourceMappingURL=index.js.map