import pytest
import elizabeth


# Fixture for locale already exist and default value is en (English for USA)
# @pytest.fixture(scope='session')
# def elizabeth_locale():
#     return 'ru'


def test_elizabeth_locale(elizabeth_locale):
    assert elizabeth_locale is not None
    assert elizabeth_locale == 'en'


def test_generic(generic):
    assert isinstance(generic, elizabeth.Generic)
    assert generic.personal.name()


def test_personal(personal):
    assert isinstance(personal, elizabeth.Personal)
    assert personal.name() != personal.name()
    assert personal.name()


def test_address(address):
    assert isinstance(address, elizabeth.Address)
    assert address.street_name()
