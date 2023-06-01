from src.base_client import BaseClient


class Neo(BaseClient):

    def __init__(self):
        super().__int__()

    def get_neo_list(self, start_date, end_date):
        return self.apiRequest.get(self.url + "feed?start_date=" + str(start_date)
                                   + "&end_date=" + str(end_date) + "&api_key=" + self.api_key, self.headers)
