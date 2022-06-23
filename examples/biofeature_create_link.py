from lablift_client import Client, generate_token, Biofeature

token = generate_token()
client = Client(token=token)
biofeature = Biofeature(client=client)
link = biofeature.generate_link(cpf="12345678911")