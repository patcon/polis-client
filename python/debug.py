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

# import httpx
# import json

# class DebugTransport(httpx.BaseTransport):
#     def __init__(self, wrapped):
#         self.wrapped = wrapped

#     def handle_request(self, request: httpx.Request) -> httpx.Response:
#         print("\n======= OUTGOING REQUEST =======")
#         print(f"{request.method} {request.url}")

#         print("\n-- Headers --")
#         for k, v in request.headers.items():
#             print(f"{k}: {v}")

#         content = request.read()
#         if content:
#             try:
#                 print("\n-- JSON Body --")
#                 print(json.dumps(json.loads(content), indent=2))
#             except Exception:
#                 print("\n-- Raw Body --")
#                 print(content.decode(errors="ignore"))

#         print("================================\n")

#         # Forward request to the wrapped transport
#         return self.wrapped.handle_request(request)

# # Use the debugging transport
# transport = DebugTransport(httpx.HTTPTransport())
# client = httpx.Client(transport=transport)

# debug_httpx_client = httpx.Client(base_url="https://pol.is/api/v3", transport=DebugTransport(httpx.HTTPTransport()))


print("Testing the authenticated client...")
polis_auth = PolisClient(xid="foobar")
# polis_auth._client = debug_httpx_client

vote = polis_auth.create_vote(conversation_id="2demo", tid=3, vote=1)
if vote and not isinstance(vote, str):
    print()
    print(vote.to_dict())

xids = polis_auth.get_conversation_xids(conversation_id="2demo")
if xids:
    print()
    print(xids)

    import csv
    from io import StringIO

    csv_file = StringIO(xids)
    reader = csv.DictReader(csv_file)

    my_pid = None
    for row in reader:
        if row["xid"] == "foobar":
            my_pid = row["participant"]
    my_votes = polis_auth.get_votes(conversation_id="2demo")
    if my_votes and not isinstance(my_votes, str):
        print()
        print("Printing my votes...")
        print([v.to_dict() for v in my_votes])