// debug.ts
import { PolisClient } from "./src/polis_client";

async function main() {
  console.log("Creating an anonymous client…");
  const polis = new PolisClient();

  try {
    console.log("Fetching comments…");
    const comments = await polis.getComments("2demo");
    // For less data returned, like in raw API response:
    // const comments = await polis.getComments("2demo", { moderation: false, include_voting_patterns: false } );
    console.log("Comments count:", comments?.length);
    console.log("Sample comment:", comments?.[0]);

    console.log("\nFetching report…");
    const report = await polis.getReport("r68fknmmmyhdpi3sh4ctc");
    console.log("Report:", report);

    console.log("\nFetching conversation…");
    const convo = await polis.getConversation("2demo");
    console.log("Conversation:", convo);

    console.log("\nFetching math…");
    const math = await polis.getMath("2demo");
    console.log("Math:", math);

    console.log("\nFetching participationInit…");
    const init = await polis.getInitialization("2demo");
    console.log("ParticipationInit:", init);

  } catch (err) {
    console.error("\n❌ Error during anon debug run:");
    console.error(err);
    // @ts-expect-error
    process.exit(1);
  }

  console.log("Creating an authenticated xid client…");
  const polisAuth = new PolisClient({ xid: "foobar" });

  try {
    console.log("Fetching an auth token…");
    await polisAuth.fetchToken("2demo");

    console.log("\nFetching conversation uuid…");
    const conversationUuid = await polisAuth.getConversationUuid("2demo") ?? {} ;
    console.log(conversationUuid);

  } catch (err) {
    console.error("\n❌ Error during anon debug run:");
    console.error(err);
    // @ts-expect-error
    process.exit(1);
  }
}

main();
