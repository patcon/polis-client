import { client as GeneratedClient } from "./generated/client.gen.js";
import * as Comments from "./generated/sdk.gen.js";
import * as Reports from "./generated/sdk.gen.js";
import * as Conversations from "./generated/sdk.gen.js";
import * as Math from "./generated/sdk.gen.js";
import * as Votes from "./generated/sdk.gen.js"
import type {
  GetCommentsData,
  GetConversationData,
  GetMathData,
  GetVotesData,
  GetReportData,
} from "./generated/types.gen.js"


type CommentsQuery = GetCommentsData["query"];
type ExtraCommentsQuery = Omit<CommentsQuery, "conversation_id">;

type ConversationQuery = GetConversationData["query"];
type ExtraConversationQuery = Omit<ConversationQuery, "conversation_id">;

type MathQuery = GetMathData["query"];
type ExtraMathQuery = Omit<MathQuery, "conversation_id">;

type VotesQuery = GetVotesData["query"];
type ExtraVotesQuery = Omit<VotesQuery, "conversation_id">;

type ReportQuery = GetReportData["query"];
type ExtraReportQuery = Omit<ReportQuery, "report_id">;

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

  async getComments(conversationId: string, extraQuery: ExtraCommentsQuery = {}) {
    const defaultQuery: ExtraCommentsQuery = {
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

  async getReport(reportId: string, extraQuery: ExtraReportQuery = {}) {
    const res = await Reports.getReport({
      query: { report_id: reportId, ...extraQuery },
    });

    // Python version extracts the first item; do same here:
    const arr = res.data;
    return Array.isArray(arr) ? arr[0] : arr;
  }

  async getConversation(conversationId: string, extraQuery: ExtraConversationQuery = {}) {
    const res = await Conversations.getConversation({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }

  async getMath(conversationId: string, extraQuery: ExtraMathQuery = {}) {
    const res = await Math.getMath({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }

  async getVotes(conversationId: string, extraQuery: ExtraVotesQuery = {}) {
    const res = await Votes.getVotes({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }
}