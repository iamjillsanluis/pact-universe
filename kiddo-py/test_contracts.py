from pactman import Consumer, Provider
import atexit
import pytest


from kid import Kid


@pytest.fixture(scope="module")
def mommy_pact():
    pact = Consumer('Kid').has_pact_with(Provider('Mommy'), host_name='mommy', port=5000, pact_dir='/code/pacts')
    pact.start_service()
    atexit.register(pact.stop_service)

    return pact


class TestGetMommyContract(object):
    def test_get_food(self, mommy_pact):
        response = {
            'answer': 'yes',
        }

        (mommy_pact
         .given('some prep work by mom')
         .upon_receiving('a request for food')
         .with_request('get', '/food')
         .will_respond_with(200, body=response)
         )

        with mommy_pact:
            answer = Kid().ask_mommy_for_food()

        assert answer == 'yes'


@pytest.fixture(scope="module")
def daddy_pact():
    pact = Consumer('Kid').has_pact_with(Provider('Daddy'), host_name='daddy', port=4567, pact_dir='/code/pacts')
    pact.start_service()
    atexit.register(pact.stop_service)

    return pact


class TestGetDaddyContract(object):
    def test_get_food(self, daddy_pact):
        response = {
            'answer': 'yes',
        }

        (daddy_pact
         .given('some prep work by dad')
         .upon_receiving('a request for food')
         .with_request('get', '/food')
         .will_respond_with(200, body=response)
         )

        with daddy_pact:
            answer = Kid().ask_daddy_for_food()

        assert answer == 'yes'
