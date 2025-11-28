import type { Client, Options as Options2, TDataShape } from './client/index.js';
import type { GetCommentsData, GetCommentsErrors, GetCommentsResponses, GetConversationData, GetConversationErrors, GetConversationResponses, GetMathData, GetMathErrors, GetMathResponses, GetReportData, GetReportErrors, GetReportResponses, GetVotesData, GetVotesErrors, GetVotesResponses } from './types.gen.js';
export type Options<TData extends TDataShape = TDataShape, ThrowOnError extends boolean = boolean> = Options2<TData, ThrowOnError> & {
    /**
     * You can provide a client instance returned by `createClient()` instead of
     * individual options. This might be also useful if you want to implement a
     * custom client.
     */
    client?: Client;
    /**
     * You can pass arbitrary values through the `meta` object. This can be
     * used to access values that aren't defined as part of the SDK function.
     */
    meta?: Record<string, unknown>;
};
export declare const getReport: <ThrowOnError extends boolean = false>(options?: Options<GetReportData, ThrowOnError>) => import("./client/types.gen.js").RequestResult<GetReportResponses, GetReportErrors, ThrowOnError, "fields">;
export declare const getConversation: <ThrowOnError extends boolean = false>(options: Options<GetConversationData, ThrowOnError>) => import("./client/types.gen.js").RequestResult<GetConversationResponses, GetConversationErrors, ThrowOnError, "fields">;
export declare const getVotes: <ThrowOnError extends boolean = false>(options: Options<GetVotesData, ThrowOnError>) => import("./client/types.gen.js").RequestResult<GetVotesResponses, GetVotesErrors, ThrowOnError, "fields">;
export declare const getMath: <ThrowOnError extends boolean = false>(options: Options<GetMathData, ThrowOnError>) => import("./client/types.gen.js").RequestResult<GetMathResponses, GetMathErrors, ThrowOnError, "fields">;
/**
 * List comments
 *
 * Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nunc interdum tristique neque, id sollicitudin tortor sollicitudin vitae.
 */
export declare const getComments: <ThrowOnError extends boolean = false>(options: Options<GetCommentsData, ThrowOnError>) => import("./client/types.gen.js").RequestResult<GetCommentsResponses, GetCommentsErrors, ThrowOnError, "fields">;
//# sourceMappingURL=sdk.gen.d.ts.map