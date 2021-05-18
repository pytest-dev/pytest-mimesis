## pytest-mimesis

[![test](https://github.com/pytest-dev/pytest-mimesis/actions/workflows/test.yml/badge.svg)](https://github.com/pytest-dev/pytest-mimesis/actions/workflows/test.yml)
[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)
[![Python Version](https://img.shields.io/pypi/pyversions/pytest-mimesis.svg)](https://pypi.org/project/pytest-mimesis/)

**pytest-mimesis** is a pytest plugin that provides pytest fixtures for [Mimesis](https://github.com/lk-geimfari/mimesis) providers. This allows you to quickly and easily use randomized, dummy data as part of your test suite.


## Installation

```bash
pip install pytest-mimesis
```


## Examples

Using the personal provider as part of a test.

```python
# your_module/__init__.py

def validate_email(email):
    # code that validates an e-mail address
    return True
```

And your test file:

```python
# tests/test_email.py

from your_module import validate_email

def test_validate_email(mimesis):
    assert validate_email(mimesis('email'))
```

You can also specify locales:

```python
@pytest.mark.parameterize('mimesis_locale', ['de'])  # use German locale
def test_create_user(mimesis):
    assert create_user(name=mimesis('full_name'))


@pytest.mark.parameterize('mimesis_locale', ['de', 'en', 'jp'])  # test multiple locales
def test_add_phone(user, mimesis):
    assert user.add_phone_number(name=mimesis('full_name'))
```


## Fixtures

We provide two public fixtures: `mimesis_locale` and `mimesis`.
While `mimesis_locale` is just a string (like: `en`, `ru`),
`mimesis` is an instance of `mimesis.schema.Field`.

We use caching of `mimesis` instances for different locales for the whole
test session, so creating new instances is cheap.


## Related projects

You might also be interested in:

- [mimesis](https://github.com/lk-geimfari/mimesis) itself, it is awesome!
- [mimesis-factory](https://github.com/mimesis-lab/mimesis-factory) which brings `factory_boy` integration to `mimesis`


## License

pytest-mimesis is licensed under the [MIT License](https://github.com/pytest-dev/pytest-mimesis/blob/master/LICENSE).
