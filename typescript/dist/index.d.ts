export declare const DEFAULT_BASE_URL = "https://pol.is/api/v3";
export declare class PolisClient {
    constructor(options?: {
        baseUrl?: string;
        headers?: Record<string, string>;
    });
    getComments(conversationId: string): Promise<import("./generated").ArrayOfComment | import("./generated").ArrayOfCommentMod | import("./generated").ArrayOfCommentModVoting | undefined>;
    getReport(reportId: string): Promise<import("./generated").Report | undefined>;
    getConversation(conversationId: string): Promise<import("./generated").Conversation | undefined>;
    getMath(conversationId: string): Promise<import("./generated")._Math | undefined>;
}
//# sourceMappingURL=index.d.ts.map