from lablift_client import Client, generate_token, Biofeature

token = generate_token()
client = Client(token=token)
biofeature = Biofeature(client=client)
people_ids = [
    {"cpf": "11111111111"},
    {"cpf": "22222222222"},
    {"cpf": "33333333333"} ]
links = biofeature.generate_multiple_links(people_ids)