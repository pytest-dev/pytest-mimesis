# -*- coding: utf-8 -*-

import pytest
from mimesis.locales import DEFAULT_LOCALE
from mimesis.schema import Field


@pytest.fixture(scope='session')  # noqa: PT005
def _mimesis_cache():  # noqa: PT005
    cached_instances = {}

    def factory(locale):
        if locale not in cached_instances:
            cached_instances[locale] = Field(locale)
        return cached_instances[locale]

    return factory


@pytest.fixture()
def mimesis_locale():
    """Specifies which locale to use."""
    return DEFAULT_LOCALE


@pytest.fixture()
def mimesis(_mimesis_cache, mimesis_locale):
    """Mimesis fixture to provide fake data using all built-in providers."""
    return _mimesis_cache(mimesis_locale)
