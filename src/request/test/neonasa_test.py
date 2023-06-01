import pytest

from src.models.neo.neo_model import Neo
from src.request.assertions.assertion import *
from src.request.test.schemas.schema import *

neo = Neo()


@pytest.mark.parametrize(
    "start_date, end_date",
    [('2022-07-01', '2022-07-07')]
)
def test_get_list_neo(start_date, end_date):
    response = neo.get_neo_list(start_date, end_date)
    assert_status_code(response.status_code, 200)
    # assert_schema_response(response.as_dict, schema_get_list_neo_response)
    assert_not_null(response.as_dict['links'])


@pytest.mark.parametrize(
    "asteroid_id",
    ['2465633']
)
def test_get_lookup_neo(asteroid_id):
    response = neo.get_neo_lookup(asteroid_id)
    assert_status_code(response.status_code, 200)


def test_browse_neo():
    response = neo.get_browse_neo()
    assert_status_code(response.status_code, 200)
