import pytest

from src.neo.neo_model import Pokemon
from src.assertions.assertion import *
from src.test.schema import *

pokemon = Pokemon()


@pytest.mark.parametrize(
    "limit, offset",
    [(100, 100),
     (200, 200),
     (1, 100)]
)
def test_get_list_pokemon(limit, offset):
    response = pokemon.get_pokemon_list(limit, offset)
    assert_status_code(response.status_code, 200)
    assert_schema_response(response.as_dict, schema_get_list_pokemon_response)
    assert_not_null(response.as_dict['results'])
