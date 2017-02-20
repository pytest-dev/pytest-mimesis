import pytest
import elizabeth


def test_locale(locale):
    assert isinstance(locale, str)
    assert locale == 'en'


@pytest.mark.parametrize('locale', ['de'])
def test_locale_override(locale):
    assert isinstance(locale, str)
    assert locale == 'de'


def test_generic(generic):
    assert isinstance(generic, elizabeth.Generic)
    assert generic.locale == 'en'
    assert generic.personal.name()


@pytest.mark.parametrize('locale', ['de'])
def test_generic_override(generic):
    assert isinstance(generic, elizabeth.Generic)
    assert generic.locale == 'de'


def test_personal(personal):
    assert isinstance(personal, elizabeth.Personal)
    assert personal.name() != personal.name()
    assert personal.name()


def test_address(address):
    assert isinstance(address, elizabeth.Address)
    assert address.street_name()


def test_business(business):
    assert isinstance(business, elizabeth.Business)


def test_clothing_sizes(clothing_sizes):
    assert isinstance(clothing_sizes, elizabeth.ClothingSizes)


def test_code(code):
    assert isinstance(code, elizabeth.Code)


def test_datetime_el(datetime_el):
    assert isinstance(datetime_el, elizabeth.Datetime)


def test_development(development):
    assert isinstance(development, elizabeth.Development)


def test_file_el(file_el):
    assert isinstance(file_el, elizabeth.File)


def test_food(food):
    assert isinstance(food, elizabeth.Food)


def test_hardware(hardware):
    assert isinstance(hardware, elizabeth.Hardware)


def test_internet(internet):
    assert isinstance(internet, elizabeth.Internet)


def test_network(network):
    assert isinstance(network, elizabeth.Network)


def test_numbers(numbers):
    assert isinstance(numbers, elizabeth.Numbers)


def test_path(path):
    assert isinstance(path, elizabeth.Path)


def test_text(text):
    assert isinstance(text, elizabeth.Text)


def test_transport(transport):
    assert isinstance(transport, elizabeth.Transport)
