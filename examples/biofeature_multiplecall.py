from lablift_client import Client, generate_token, Biofeature

token = generate_token()
client = Client(token=token)
biofeature = Biofeature(client=client)
items = [
    {"img":"face.jpg"},
    {"img":"face.jpg"},
]
response = biofeature.multiple_call(items)
print(response)
