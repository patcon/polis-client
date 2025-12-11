from polis_client import PolisClient

polis = PolisClient()

comments = polis.get_comments(conversation_id="2demo")
if comments:
    print(comments[0].to_dict())

report = polis.get_report(report_id="r68fknmmmyhdpi3sh4ctc")
if report:
    print(report.to_dict())

conversation = polis.get_conversation(conversation_id="2demo")
if conversation:
    print(conversation.to_dict())

math = polis.get_math(conversation_id="2demo")
print(math)

votes = polis.get_votes(conversation_id="2demo", pid=10)
if votes:
    print(votes[0].to_dict())

all_votes = polis.get_all_votes_slow(conversation_id="4cvkai2ctw")
if all_votes:
    print(f"Fetched all {len(all_votes)} votes...")


print("Testing the authenticated client...")
polis_auth = PolisClient(xid="foobar")
# polis_auth._client = debug_httpx_client

vote = polis_auth.create_vote(conversation_id="2demo", tid=3, vote=1)
if vote:
    print()
    print(vote.to_dict())

xids = polis_auth.get_xids(conversation_id="2demo")
if xids:
    my_pid = None
    for row in xids:
        if row["xid"] == "foobar":
            my_pid = row["participant"]
    my_votes = polis_auth.get_votes(conversation_id="2demo")
    if my_votes and not isinstance(my_votes, str):
        print()
        print("Printing my votes...")
        print([v.to_dict() for v in my_votes])