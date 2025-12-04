from polis_client import PolisClient

polis = PolisClient()

comments = polis.get_comments(conversation_id="2demo")
if isinstance(comments, list) and len(comments) > 0:
    print(comments[0].to_dict())

report = polis.get_report(report_id="r68fknmmmyhdpi3sh4ctc")
if report:
    print(report.to_dict())

conversation = polis.get_conversation(conversation_id="2demo")
if conversation and not isinstance(conversation, str):
    print(conversation.to_dict())

math = polis.get_math(conversation_id="2demo")
print(math)

votes = polis.get_votes(conversation_id="2demo", pid=10)
if isinstance(votes, list) and len(votes) > 0:
    print(votes[0].to_dict())

polis_auth = PolisClient(xid="foobar")
polis_auth._ensure_token(conversation_id="2demo")
xids = polis_auth.get_conversation_xids(conversation_id="2demo")
if xids:
    print(xids)