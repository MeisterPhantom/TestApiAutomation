from utils.apirequest import APIRequest


class BaseClient:
    def __int__(self):
        self.apiRequest = APIRequest()
        self.headers = {
            "Content-Type": 'application/json',
            "Accept": 'application/json'
        }
        self.url = "https://api.nasa.gov/neo/rest/v1/"
        self.api_key = "vetkAHizYLcVaGtJhjiPBh6kgrlmOFTkDI8aiZH9"
