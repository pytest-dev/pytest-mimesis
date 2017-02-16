import pytest
import elizabeth


# Fixture for locale already exist and default value is en (English for USA)
# @pytest.fixture(scope='session')
# def elizabeth_locale():
#     return 'ru'


def test_generic(generic, elizabeth_locale):
    """Test elizabeth fixture."""
    assert isinstance(generic, elizabeth.Generic)
    assert generic.personal.name() != generic.personal.name()
    assert generic.personal.name()
    assert elizabeth_locale == 'en'


def test_personal(personal, elizabeth_locale):
    assert isinstance(personal, elizabeth.Personal)
    assert personal.name() != personal.name()
    assert personal.name()
    assert elizabeth_locale == 'en'

    # TODO: Write test for all providers
