import pytest

from src.models.neo.neo_model import Neo
from src.request.assertions.assertion import *
from src.request.test.schemas.schema import *

neo = Neo()


@pytest.mark.parametrize(
    "start_date, end_date",
    [(100, 100),
     (200, 200),
     (1, 100)]
)
def test_get_list_neo(start_date, end_date):
    response = neo.get_neo_list(start_date, end_date)
    assert_status_code(response.status_code, 200)
    assert_schema_response(response.as_dict, schema_get_list_neo_response)
    assert_not_null(response.as_dict['links'])
