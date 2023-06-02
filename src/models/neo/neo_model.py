from src.base_client import BaseClient


class Neo(BaseClient):

    def __init__(self):
        super().__int__()

    def get_neo_list(self, start_date, end_date):
        return self.apiRequest.get(self.url + "feed?start_date=" + start_date
                                   + "&end_date=" + end_date + "&api_key=" + self.api_key, self.headers)

    def get_neo_lookup(self, asteroid_id):
        return self.apiRequest.get(self.url + "neo/" + str(asteroid_id) + "?api_key=" + self.api_key, self.headers)

    def get_browse_neo(self):
        return self.apiRequest.get(self.url + "neo/browse?api_key=" + self.api_key, self.headers)
