from src.base_client import BaseClient


class Pokemon(BaseClient):

    def __init__(self):
        super().__int__()

    def get_pokemon_list(self, limit, offset):
        return self.apiRequest.get(self.url + "?limit=" + str(limit) + "&offset=" + str(offset), self.headers)
