from typing import Callable

import pytest
from mimesis.locales import DEFAULT_LOCALE
from mimesis.schema import Field

_CacheCallable = Callable[[str], Field]


@pytest.fixture(scope='session')  # noqa: PT005
def _mimesis_cache() -> _CacheCallable:  # noqa: PT005
    cached_instances = {}

    def factory(locale: str) -> Field:
        if locale not in cached_instances:
            cached_instances[locale] = Field(locale)
        return cached_instances[locale]

    return factory


@pytest.fixture()
def mimesis_locale() -> str:
    """Specifies which locale to use."""
    return DEFAULT_LOCALE


@pytest.fixture()
def mimesis(_mimesis_cache: _CacheCallable, mimesis_locale: str) -> Field:
    """Mimesis fixture to provide fake data using all built-in providers."""
    return _mimesis_cache(mimesis_locale)
