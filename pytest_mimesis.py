# -*- coding: utf-8 -*-

import pytest
from mimesis.locales import DEFAULT_LOCALE
from mimesis.schema import Field


@pytest.fixture(scope='session')
def _mimesis_cache():
    cached_instances = {}

    def _inner(locale):
        if locale not in cached_instances:
            cached_instances[locale] = Field(locale)
        return cached_instances[locale]

    return _inner


@pytest.fixture()
def mimesis_locale():
    """Specifies which locale to use."""
    return DEFAULT_LOCALE


@pytest.fixture()
def mimesis(_mimesis_cache, mimesis_locale):
    """Mimesis fixture to provide fake data using all built-in providers."""
    return _mimesis_cache(mimesis_locale)
