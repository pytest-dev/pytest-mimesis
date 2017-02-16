import pytest

from elizabeth import (
    Address,
    Business,
    ClothingSizes,
    Code,
    Datetime,
    Development,
    File,
    Food,
    Hardware,
    Internet,
    Network,
    Numbers,
    Path,
    Personal,
    Text,
    Transport,
    Generic
)


@pytest.fixture(scope='session')
def elizabeth_locale():
    """
    Default is English.

    :return: en
    :rtype: str
    """
    return 'en'


@pytest.fixture(scope='session')
def generic(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return: locale
    :rtype: object
    """
    return Generic(elizabeth_locale)


@pytest.fixture(scope='session')
def personal(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return:
    """
    return Personal(elizabeth_locale)


@pytest.fixture(scope='session')
def address(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return:
    """
    return Address(elizabeth_locale)


@pytest.fixture(scope='session')
def business(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return:
    """
    return Business(elizabeth_locale)


@pytest.fixture(scope='session')
def clothing_sizes():
    """
    :return:
    """
    return ClothingSizes()


@pytest.fixture(scope='session')
def code(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return:
    """
    return Code(elizabeth_locale)


@pytest.fixture(scope='session')
def datetime_el(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return:
    """
    return Datetime(elizabeth_locale)


@pytest.fixture(scope='session')
def development():
    """

    :return:
    """
    return Development()


@pytest.fixture(scope='session')
def file_el():
    """

    :return:
    """
    return File()


@pytest.fixture(scope='session')
def food():
    """

    :return:
    """
    return Food(elizabeth_locale)


@pytest.fixture(scope='session')
def hardware():
    """

    :return:
    """
    return Hardware()


@pytest.fixture(scope='session')
def internet():
    """

    :return:
    """
    return Internet()


@pytest.fixture(scope='session')
def network():
    """

    :return:
    """
    return Network()


@pytest.fixture(scope='session')
def numbers():
    """

    :return:
    """
    return Numbers()


@pytest.fixture(scope='session')
def path():
    """

    :return:
    """
    return Path()


@pytest.fixture(scope='session')
def text(elizabeth_locale):
    """

    :param elizabeth_locale:
    :return:
    """
    return Text(elizabeth_locale)


@pytest.fixture(scope='session')
def transport():
    """

    :param elizabeth_locale:
    :return:
    """
    return Transport()
