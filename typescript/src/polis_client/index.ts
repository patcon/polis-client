import { client as GeneratedClient } from "./generated/client.gen.js";
import * as Comments from "./generated/sdk.gen.js";
import * as Reports from "./generated/sdk.gen.js";
import * as Conversations from "./generated/sdk.gen.js";
import * as MathAPI from "./generated/sdk.gen.js";

export const DEFAULT_BASE_URL = "https://pol.is/api/v3";

export class PolisClient {
  constructor(options?: { baseUrl?: string; headers?: Record<string, string> }) {
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

  async getComments(conversationId: string, extraQuery: Record<string, any> = {}) {
    const res = await Comments.getComments({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }

  async getReport(reportId: string, extraQuery: Record<string, any> = {}) {
    const res = await Reports.getReport({
      query: { report_id: reportId, ...extraQuery },
    });

    // Python version extracts the first item; do same here:
    const arr = res.data;
    return Array.isArray(arr) ? arr[0] : arr;
  }

  async getConversation(conversationId: string, extraQuery: Record<string, any> = {}) {
    const res = await Conversations.getConversation({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }

  async getMath(conversationId: string, extraQuery: Record<string, any> = {}) {
    const res = await MathAPI.getMath({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }
}