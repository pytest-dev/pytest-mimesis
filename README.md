## pytest-elizabeth


[![Build Status](https://travis-ci.org/lk-geimfari/pytest-elizabeth.svg?branch=master)](https://travis-ci.org/lk-geimfari/pytest-elizabeth)

**pytest-mimesis** is a pytest plugin that provides pytest fixtures for [Mimesis](https://github.com/lk-geimfari/mimesis) providers.  This allows you to quickly and easily use randomized, dummy data as part of your test suite.


#### Installation

```
pip install pytest-mimesis
```

or 
```
➜ ~ git clone https://github.com/lk-geimfari/pytest-mimesis.git
➜ ~ cd pytest-mimesis/
➜  make install
```

#### Examples

Using the personal provider as part of a test.

`your_module/__init__.py`

```python
def validate_email(email):
    # code that validates an e-mail address
    return True
```

`tests/test_email.py`:

```python
from your_module import validate_email

def test_validate_email(personal):
    assert validate_email(personal.email())
```

Specifying locales.

```python
@pytest.mark.parameterize('locale', 'de')  # use German locale
def test_create_user(personal):
    assert create_user(name=personal.full_name())
    

@pytest.mark.parameterize('locale', ['de', 'en', 'jp'])  # test multiple locales
def test_add_phone(user, personal):
    assert user.add_phone_number(name=personal.full_name())
```

#### Fixtures

The following fixtures are made available as part of pytest-elizabeth.

* generic
* personal
* address
* business
* clothing_sizes
* code
* datetime_el
* development
* file_el
* food
* hardware
* internet
* numbers
* path
* text
* transport


#### Testing
```
➜  make test
```

#### Authors
[Kevin Schellenberg](https://github.com/wikkiewikkie) and [Likid Geimfari](https://github.com/lk-geimfari).


#### License

pytest-elizabeth is licensed under the [MIT License](https://github.com/lk-geimfari/pytest-elizabeth/blob/master/LICENSE).
