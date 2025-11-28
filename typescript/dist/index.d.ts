export declare const DEFAULT_BASE_URL = "https://pol.is/api/v3";
export declare class PolisClient {
    constructor(options?: {
        baseUrl?: string;
        headers?: Record<string, string>;
    });
    getComments(conversationId: string): Promise<import("./generated/types.gen.js").ArrayOfComment | import("./generated/types.gen.js").ArrayOfCommentMod | import("./generated/types.gen.js").ArrayOfCommentModVoting | undefined>;
    getReport(reportId: string): Promise<import("./generated/types.gen.js").Report | undefined>;
    getConversation(conversationId: string): Promise<import("./generated/types.gen.js").Conversation | undefined>;
    getMath(conversationId: string): Promise<import("./generated/types.gen.js")._Math | undefined>;
}
//# sourceMappingURL=index.d.ts.map