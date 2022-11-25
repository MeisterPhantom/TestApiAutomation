from utils.apirequest import APIRequest


class BaseClient:
    def __int__(self):
        self.apiRequest = APIRequest()
        self.headers = {
            "Content-Type": 'application/json',
            "Accept": 'application/json'
        }
        self.url = "https://pokeapi.co/api/v2/pokemon"
