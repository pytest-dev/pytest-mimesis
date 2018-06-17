## pytest-mimesis


[![Build Status](https://travis-ci.org/mimesis-lab/pytest-mimesis.svg?branch=master)](https://travis-ci.org/mimesis-lab/pytest-mimesis)

**pytest-mimesis** is a pytest plugin that provides pytest fixtures for [Mimesis](https://github.com/lk-geimfari/mimesis) providers.  This allows you to quickly and easily use randomized, dummy data as part of your test suite.


#### Installation

```
pip install pytest-mimesis
```

or
```
➜ ~ git clone https://github.com/mimesis-lab/pytest-mimesis.git
➜ ~ cd pytest-mimesis/
➜  make install
```

#### Examples

Using the personal provider as part of a test.

`your_module/__init__.py`:

```python
def validate_email(email):
    # code that validates an e-mail address
    return True
```

`tests/test_email.py`:

```python
from your_module import validate_email

def test_validate_email(mimesis):
    assert validate_email(mimesis('email'))
```

Specifying locales:

```python
@pytest.mark.parameterize('mimesis_locale', 'de')  # use German locale
def test_create_user(mimesis):
    assert create_user(name=mimesis('full_name'))


@pytest.mark.parameterize('mimesis_locale', ['de', 'en', 'jp'])  # test multiple locales
def test_add_phone(user, mimesis):
    assert user.add_phone_number(name=mimesis('full_name'))
```

#### Fixtures

We provide two public fixtures: `mimesis_locale` and `mimesis`.
While `mimesis_locale` is just a string (like: `en`, `ru`), 
`mimesis` is an instance of `mimesis.schema.Field`.

We use caching of `mimesis` instances for different locales for the whole
test session, so creating new instances is cheap. 


#### License

pytest-mimesis is licensed under the [MIT License](https://github.com/mimesis-lab/pytest-mimesis/blob/master/LICENSE).
