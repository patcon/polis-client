import { client as GeneratedClient } from "./generated/client.gen.js";
import * as Comments from "./generated/sdk.gen.js";
import * as Reports from "./generated/sdk.gen.js";
import * as Conversations from "./generated/sdk.gen.js";
import * as Math from "./generated/sdk.gen.js";
import * as Votes from "./generated/sdk.gen.js";
import * as Initialization from "./generated/sdk.gen.js";
import type {
  GetCommentsData,
  GetConversationData,
  GetMathData,
  GetVotesData,
  GetReportData,
  GetInitializationData,
  CreateVoteData,
  CreateCommentData,
} from "./generated/types.gen.js"


type CommentsQuery = GetCommentsData["query"];
type ExtraCommentsQuery = Omit<CommentsQuery, "conversation_id">;

type ConversationQuery = GetConversationData["query"];
type ExtraConversationQuery = Omit<ConversationQuery, "conversation_id">;

type MathQuery = GetMathData["query"];
type ExtraMathQuery = Omit<MathQuery, "conversation_id">;

type VotesQuery = GetVotesData["query"];
type ExtraVotesQuery = Omit<VotesQuery, "conversation_id">;

type VoteBody = CreateVoteData["body"];

type ReportQuery = GetReportData["query"];
type ExtraReportQuery = Omit<ReportQuery, "report_id">;

type InitializationQuery = GetInitializationData["query"];
type ExtraInitializationQuery = Omit<InitializationQuery, "conversation_id">;

export const DEFAULT_BASE_URL = "https://pol.is";

export class PolisClient {
  private token: string | null = null;
  private xid?: string;
  private readonly baseUrl: string;

  constructor(options?: {
    baseUrl?: string;
    xid?: string;
    headers?: Record<string, string>
  }) {
    const { baseUrl = DEFAULT_BASE_URL, xid, headers } = options ?? {};
    this.baseUrl = `${baseUrl}/api/v3`;
    this.xid = xid;

    // configure the internal generated client once
    GeneratedClient.setConfig({
      baseUrl: this.baseUrl,
      headers,
    });

    // Request interceptor: inject auth
    GeneratedClient.interceptors.request.use(async (req, options) => {
      const conversationId = options.query?.conversation_id as string | undefined;

      // Bail if we're already grabbing a token
      if (options.url.includes("participationInit")) return req

      // Ensure token before sending request
      if (!this.token && this.xid && conversationId) {
        await this.fetchToken(conversationId, this.xid); // lazy token init
      }

      if (this.token) {
        req.headers.set("Authorization", `Bearer ${this.token}`);
      }

      return req;
    });
  }

  async fetchToken(conversationId: string, xid?: string) {
    const res = await Initialization.getInitialization({
      query: { conversation_id: conversationId, xid: xid || this.xid },
    });
    this.token = res.data?.auth?.token ?? null;
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

  async getConversationUuid(conversationId: string) {
    const res = await Conversations.getConversationUuid({
      query: { conversation_id: conversationId },
    });
    return res.data;
  }

  async getConversationXidsByUuid(conversationUuid: string) {
    const res = await Conversations.getConversationXidsByUuid({
      path: { conversation_uuid: conversationUuid },
    });
    return res.data;
  }

  async getConversationXidsById(conversationId: string) {
    const { conversation_uuid: conversationUuid } = await this.getConversationUuid(conversationId) ?? {};
    return this.getConversationXidsByUuid(conversationUuid!);
  }

  async getConversationXids(conversationId: string) {
    return this.getConversationXidsById(conversationId)
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

  async createVote(conversationId: string, body: VoteBody) {
    const res = await Votes.createVote({
      body: {...body, conversation_id: conversationId},
    });
    return res.data;
  }

  async getInitialization(conversationId: string, extraQuery: ExtraInitializationQuery = {}) {
    const res = await Initialization.getInitialization({
      query: { conversation_id: conversationId, ...extraQuery },
    });
    return res.data;
  }
}