from __future__ import annotations
from multiprocessing import Pool
from .client import Client
from .config import api_urls
from typing import Union


class Biofeature:
    def __init__(self, client: Client) -> None:
        self.client = client

    def generate_key(self, cpf: str, name: Union[None, str] = None, api_return_key:str = 'id') -> str:
        if api_return_key not in ['id', 'link']:
            raise Exception(f"[Error] api_return_key must be either `id` or `link`.")
        data = {"cpf": cpf}
        if name != None:
            data["name"] = name
        response = self.client.request("post", f"{api_urls['biofeatureai']}/keys", json=data)
        if response and api_return_key in response.json():
            return response.json()[api_return_key]
        raise Exception(f"[Error] Key generation failed. {response.content}")

    def generate_link(self, cpf: str, name: Union[None, str] = None) -> str:
        """ Wrapper to help generate Biofeature links through generate_keys()."""
        link = self.generate_key(cpf=cpf, name=name, api_return_key='link')
        return link

    def generate_multiple_links(self, items: list[dict[str, str]]) -> list[str]:
        for i in range(len(items)):
            item = items[i]
            if not "cpf" in item:
                raise Exception(f"[Error] Missing cpf key on index {i} element.")
        with Pool() as pool:
            response = pool.starmap(self.generate_link, [(
                item["cpf"], item["name"] if "name" in item else None) for item in items])
        return response

    def call(self, img: str, cpf: Union[None, str] = None) -> dict:
        response = self.client.request(
            "post", f"{api_urls['biofeatureai']}/predict", files={"file": open(img, 'rb')}, json={"cpf": cpf})
        if not (response.status_code == 201 or response.status_code == 422):
            raise Exception(f"[Error] Prediction failed. {response.content}")
        return response.json()

    def multiple_call(self, items: list[dict[str, str]]) -> list[dict]:
        for item in items:
            if not "img" in item:
                raise Exception(f"[Error] Missing img key on dict {item}.")
        with Pool() as pool:
            response = pool.starmap(self.call, [(
                item["img"], item["cpf"] if "cpf" in item else None) for item in items])
        return response
