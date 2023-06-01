from ..neo.neo_model import Neo
from pytest_bdd import scenario, given, when, then

request = Neo


@given('the API requires "<start_date>" and "<end_date>" data date', target_fixture='run')
def run(start_date, end_date):
    return request.get_neo_list(start_date, end_date)


@then('the API status code response es equal to "<status_code>"')
def validate_status(run, status_code):
    assert run.status_code == status_code