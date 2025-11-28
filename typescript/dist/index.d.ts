import type { GetCommentsData, GetConversationData, GetMathData, GetVotesData, GetReportData } from "./generated/types.gen.js";
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
export declare const DEFAULT_BASE_URL = "https://pol.is/api/v3";
export declare class PolisClient {
    constructor(options?: {
        baseUrl?: string;
        headers?: Record<string, string>;
    });
    getComments(conversationId: string, extraQuery?: ExtraCommentsQuery): Promise<import("./generated/types.gen.js").ArrayOfComment | import("./generated/types.gen.js").ArrayOfCommentMod | import("./generated/types.gen.js").ArrayOfCommentModVoting | undefined>;
    getReport(reportId: string, extraQuery?: ExtraReportQuery): Promise<import("./generated/types.gen.js").Report | undefined>;
    getConversation(conversationId: string, extraQuery?: ExtraConversationQuery): Promise<import("./generated/types.gen.js").Conversation | undefined>;
    getMath(conversationId: string, extraQuery?: ExtraMathQuery): Promise<import("./generated/types.gen.js")._Math | undefined>;
    getVotes(conversationId: string, extraQuery?: ExtraVotesQuery): Promise<import("./generated/types.gen.js").ArrayOfVote | undefined>;
}
export {};
//# sourceMappingURL=index.d.ts.map