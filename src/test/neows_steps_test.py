from pytest_bdd import scenarios, given, when, then, scenario
from src.neo.neo_model import *

request = Neo

scenarios('../features/neows.feature')


@given('the NeoWS API required  the start date "<start_date>" and end date "<end_date>" data')
def run(start_date, end_date):
    return request.get_neo_list(start_date, end_date)


@then('the response status code is "<code_status>"')
def validate_status(run, code_status):
    assert run.status_code == code_status
