from polis_client.client import PolisClient

polis = PolisClient()

comments = polis.get_comments(conversation_id="2demo")
if comments:
    for c in comments:
        print(c.to_dict())

resp = polis.get_comments_raw(conversation_id="2demo")
if resp.status_code == 200 and resp.parsed:
    for c in resp.parsed:
        print(c.to_dict())

conversation = polis.get_conversation(conversation_id="2demo")
if conversation:
    print(conversation.to_dict())

resp = polis.get_conversation_raw(conversation_id="2demo")
if resp.status_code == 200 and resp.parsed:
    print(resp.parsed.to_dict())