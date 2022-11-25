import json
from dataclasses import dataclass
import requests


@dataclass
class Response:
    status_code: int
    text: str
    as_dict: object
    headers: dict


class APIRequest:

    def get(self, url, headers):
        response = requests.get(url, headers=headers)
        return self.__get_response(response)

    def post(self, url, payload, headers):
        response = requests.post(url, data=payload, headers=headers)
        return self.__get_response(response)

    @staticmethod
    def __get_response(response):
        status_code = response.status_code
        text = response.text
        headers = response.headers

        try:
            as_dict = json.loads(response.text)
        except Exception:
            as_dict = {}

        return Response(
            status_code, text, as_dict, headers
        )