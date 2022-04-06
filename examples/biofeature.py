from lablift_client import Client, generate_token, Biofeature

token = generate_token()
client = Client(token=token)
biofeature = Biofeature(client=client)
response = biofeature.call(img="face.jpg")
print(response)
