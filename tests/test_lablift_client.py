import pytest
from lablift_client import Client, generate_token, Biofeature, __version__

#GET CREDENTIALS TO TEST API CALLS

@pytest.fixture(scope="session")
def user(pytestconfig):
    return pytestconfig.getoption("user")

@pytest.fixture(scope="session")
def password(pytestconfig):
    return pytestconfig.getoption("password")

def test_version():
    assert __version__ == '0.1.2'

def test_token_generation(user, password):
    token = generate_token(username=user, password=password)
    assert type(token)==str

def test_generate_key(user, password):
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    id = biofeature.generate_key("12345678911", "PYTEST API TEST")
    assert type(id)==str
    assert '://' not in id, f"Generate key created a link instead of an id by default. {id}"

def test_generate_key_without_name(user, password):
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    id = biofeature.generate_key("12345678911")
    assert type(id)==str
    assert '://' not in id, f"Generate key created a link instead of an id by default. {id}"

def test_generate_link(user, password):
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    link = biofeature.generate_link("12345678911", "PYTEST API TEST")
    assert type(link)==str
    assert 'https://' in link[:8], f"Generate link did not create a valid URL. {link}"

def test_generate_link_without_name(user, password):
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    link = biofeature.generate_link("12345678911")
    assert type(link)==str
    assert 'https://' in link[:8], f"Generate link did not create a valid URL. {link}"

def test_generate_multiple_links(user, password):
    fake_people = [
        {"cpf": "11111111111", "name": "PYTEST API TEST Fake 1"},
        {"cpf": "22222222222", "name": "PYTEST API TEST Fake 2"},
        {"cpf": "33333333333"},
        {"cpf": "44444444444", "name": "PYTEST API TEST Fake 4"}
    ]
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    links = biofeature.generate_multiple_links(fake_people)
    assert len(links) == len(fake_people)
    for link in links:
        assert type(link)==str
        assert 'https://' in link[:8], f"Generate link did not create a valid URL. {link}"

def test_call(user, password):
    cpf = "11111111111"
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    response = biofeature.call(img="../examples/face.jpg", cpf=cpf)
    assert response['cpf'] == cpf, f"CPF returned ({response['cpf']}) does not match CPF sent ({cpf})"
    assert "bmi" in response.keys() 
    assert "age" in response.keys() 

def test_multiple_call(user, password):
    fake_people = [
        {"img": "../examples/face.jpg", "cpf": "11111111111"},
        {"img": "../examples/face.jpg", "cpf": "22222222222"},
        {"img": "../examples/face.jpg"},
        {"img": "../examples/face.jpg", "cpf": "44444444444"}
    ]
    token = generate_token(username=user, password=password)
    client = Client(token=token)
    biofeature = Biofeature(client=client)
    predictions = biofeature.multiple_call(fake_people)
    assert len(predictions) == len(fake_people)
    for i in range(len(predictions)):
        assert predictions[i]['cpf'] == fake_people[i]['cpf'], f"CPF returned ({predictions[i]['cpf']}) does not match CPF sent ({fake_people[i]['cpf']})"
        assert "bmi" in predictions[i].keys() 
        assert "age" in predictions[i].keys() 