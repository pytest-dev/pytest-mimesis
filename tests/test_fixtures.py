import pytest
import mimesis


def test_locale(locale):
    assert isinstance(locale, str)
    assert locale == 'en'


@pytest.mark.parametrize('locale', ['de'])
def test_locale_override(locale):
    assert isinstance(locale, str)
    assert locale == 'de'


def test_generic(generic):
    assert isinstance(generic, mimesis.Generic)
    assert generic.locale == 'en'
    assert generic.personal.name()


@pytest.mark.parametrize('locale', ['de'])
def test_generic_override(generic):
    assert isinstance(generic, mimesis.Generic)
    assert generic.locale == 'de'


def test_personal(personal):
    assert isinstance(personal, mimesis.Personal)
    assert personal.name() != personal.name()
    assert personal.name()


def test_address(address):
    assert isinstance(address, mimesis.Address)
    assert address.street_name()


def test_business(business):
    assert isinstance(business, mimesis.Business)


def test_clothing_sizes(clothing_sizes):
    assert isinstance(clothing_sizes, mimesis.ClothingSizes)


def test_code(code):
    assert isinstance(code, mimesis.Code)


def test_datetime_el(datetime_el):
    assert isinstance(datetime_el, mimesis.Datetime)


def test_development(development):
    assert isinstance(development, mimesis.Development)


def test_file_el(file_el):
    assert isinstance(file_el, mimesis.File)


def test_food(food):
    assert isinstance(food, mimesis.Food)


def test_hardware(hardware):
    assert isinstance(hardware, mimesis.Hardware)


def test_internet(internet):
    assert isinstance(internet, mimesis.Internet)


def test_numbers(numbers):
    assert isinstance(numbers, mimesis.Numbers)


def test_path(path):
    assert isinstance(path, mimesis.Path)


def test_text(text):
    assert isinstance(text, mimesis.Text)


def test_transport(transport):
    assert isinstance(transport, mimesis.Transport)
