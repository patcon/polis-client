import type { GetCommentsData, GetConversationData, GetMathData, GetVotesData, GetReportData, GetInitializationData } from "./generated/types.gen.js";
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
type InitializationQuery = GetInitializationData["query"];
type ExtraInitializationQuery = Omit<InitializationQuery, "conversation_id">;
export declare const DEFAULT_BASE_URL = "https://pol.is";
export declare class PolisClient {
    private token;
    private xid?;
    private readonly baseUrl;
    constructor(options?: {
        baseUrl?: string;
        xid?: string;
        headers?: Record<string, string>;
    });
    private fetchToken;
    private extractConversationId;
    getComments(conversationId: string, extraQuery?: ExtraCommentsQuery): Promise<import("./generated/types.gen.js").ArrayOfComment | import("./generated/types.gen.js").ArrayOfCommentMod | import("./generated/types.gen.js").ArrayOfCommentModVoting | undefined>;
    getReport(reportId: string, extraQuery?: ExtraReportQuery): Promise<import("./generated/types.gen.js").Report | undefined>;
    getConversation(conversationId: string, extraQuery?: ExtraConversationQuery): Promise<import("./generated/types.gen.js").Conversation | undefined>;
    getMath(conversationId: string, extraQuery?: ExtraMathQuery): Promise<import("./generated/types.gen.js").MathV3 | undefined>;
    getVotes(conversationId: string, extraQuery?: ExtraVotesQuery): Promise<import("./generated/types.gen.js").ArrayOfVote | undefined>;
    getInitialization(conversationId: string, extraQuery?: ExtraInitializationQuery): Promise<import("./generated/types.gen.js").ParticipationInit | undefined>;
}
export {};
//# sourceMappingURL=index.d.ts.map