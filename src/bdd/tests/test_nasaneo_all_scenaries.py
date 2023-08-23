from src.models.neo.neo_model import Neo
from pytest_bdd import scenarios, given, then
from pytest_bdd import parsers

neo = Neo()


scenarios('../features/test_nasaneo.feature')


@given(
    parsers.cfparse("the API requires {start_date:Date} and {end_date:Date} data date", extra_types={"Date": str}),
    target_fixture="run_get_list_neo")
def run_get_list_neo(start_date, end_date):
    return neo.get_neo_list(start_date, end_date)


@given(parsers.cfparse("the API requires {asteroid_id:Number} asteroid id", extra_types={"Number": int}),
       target_fixture="run_get_lookup_neo")
def run_get_lookup_neo(asteroid_id):
    return neo.get_neo_lookup(asteroid_id)


@given("the API to get all data of asteroids", target_fixture="run_get_browse_neo")
def run_get_browse_neo():
    return neo.get_browse_neo()


@then(parsers.cfparse("the API status code response es equal to {status_code:Number}", extra_types={"Number": int}))
def validate_status(run_get_list_neo, run_get_lookup_neo, run_get_browse_neo, status_code):
    if run_get_list_neo.as_dict:
        assert run_get_list_neo.status_code == status_code
    elif run_get_lookup_neo.as_dict:
        assert run_get_lookup_neo.status_code == status_code
    elif run_get_browse_neo.as_dict:
        assert run_get_browse_neo.status_code == status_code
