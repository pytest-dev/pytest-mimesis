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


@pytest.fixture()
def locale(locale_name=None):
    """
    Default is English.

    :return: en
    :rtype: str
    """
    if locale_name is None:
        return 'en'
    return locale_name


@pytest.fixture()
def generic(locale):
    """

    :param locale:
    :return: locale
    :rtype: object
    """
    return Generic(locale)


@pytest.fixture()
def personal(locale):
    """

    :param locale:
    :return:
    """
    return Personal(locale)


@pytest.fixture()
def address(locale):
    """

    :param locale:
    :return:
    """
    return Address(locale)


@pytest.fixture()
def business(locale):
    """

    :param locale:
    :return:
    """
    return Business(locale)


@pytest.fixture()
def clothing_sizes():
    """
    :return:
    """
    return ClothingSizes()


@pytest.fixture()
def code(locale):
    """

    :param locale:
    :return:
    """
    return Code(locale)


@pytest.fixture()
def datetime_el(locale):
    """

    :param locale:
    :return:
    """
    return Datetime(locale)


@pytest.fixture()
def development():
    """

    :return:
    """
    return Development()


@pytest.fixture()
def file_el():
    """

    :return:
    """
    return File()


@pytest.fixture()
def food(locale):
    """

    :return:
    """
    return Food(locale)


@pytest.fixture()
def hardware():
    """

    :return:
    """
    return Hardware()


@pytest.fixture()
def internet():
    """

    :return:
    """
    return Internet()


@pytest.fixture()
def network():
    """

    :return:
    """
    return Network()


@pytest.fixture()
def numbers():
    """

    :return:
    """
    return Numbers()


@pytest.fixture()
def path():
    """

    :return:
    """
    return Path()


@pytest.fixture()
def text(locale):
    """

    :param locale:
    :return:
    """
    return Text(locale)


@pytest.fixture()
def transport():
    """

    :param locale:
    :return:
    """
    return Transport()
