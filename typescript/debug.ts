// debug.ts
import { PolisClient } from "./src/polis_client";

async function main() {
  const polis = new PolisClient();

  try {
    console.log("Fetching comments…");
    const comments = await polis.getComments("2demo");
    console.log("Comments count:", comments?.length);
    console.log("Sample comment:", comments?.[0]);

    console.log("\nFetching report…");
    const report = await polis.getReport("2demo");
    console.log("Report:", report);

    console.log("\nFetching conversation…");
    const convo = await polis.getConversation("2demo");
    console.log("Conversation:", convo);

    console.log("\nFetching math…");
    const math = await polis.getMath("2demo");
    console.log("Math:", math);

  } catch (err) {
    console.error("\n❌ Error during debug run:");
    console.error(err);
    process.exit(1);
  }
}

main();
