from lablift_client import Client, generate_token, Biofeature

token = generate_token()
client = Client(token=token)
biofeature = Biofeature(client=client)
items = [
    {"img":"face1.jpg"},
    {"img":"face2.jpg"},
]
response = biofeature.multiple_call(items)
print(response)
