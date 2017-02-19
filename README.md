####Elizabeth integration with the pytest test runner
---
[![Build Status](https://travis-ci.org/lk-geimfari/pytest-elizabeth.svg?branch=master)](https://travis-ci.org/lk-geimfari/pytest-elizabeth)

_pytest-elizabeth_ adds Elizabeth fixtures for easy use of Elizabeth for your tests under pytest runner.


### Installation

```
pip install pytest-elizabeth
```

or 
```
➜ ~ git clone https://github.com/lk-geimfari/pytest-elizabeth.git
➜ ~ cd pytest-elizabeth
➜  make install
```

### Testing
```
➜  make test
```

### Example

An example of Elizabeth and pytest integration.

`tests/test_plugin.py`:

```python
import elizabeth

def test_generic(personal, elizabeth_locale):
    assert isinstance(personal, elizabeth.Personal)
    assert personal.name()
    assert elizabeth_locale == 'en'
```

### License

pytest-elizabeth is licensed under the MIT License.
