# -*- coding: utf-8 -*-

import string

import pytest
from mimesis.locales import DEFAULT_LOCALE


def test_locale(mimesis_locale, mimesis):
    assert mimesis_locale == DEFAULT_LOCALE
    assert mimesis.locale == DEFAULT_LOCALE  # we test caching here


@pytest.mark.parametrize('mimesis_locale', ['de'])
def test_locale_override(mimesis_locale, mimesis):
    assert mimesis_locale == 'de'
    assert mimesis.locale == 'de'


def test_mimesis_fixture(mimesis):
    age = 18

    assert mimesis('age', minimum=age, maximum=age) == age
    assert len(mimesis('full_name').split(' ')) > 1


@pytest.mark.parametrize('mimesis_locale', ['ru'])
def test_mimesis_fixture_with_overridden_locale(mimesis):
    assert mimesis.locale == 'ru'

    name = mimesis('full_name')
    for letter in name:  # russian letters are not in ASCII:
        assert letter not in string.ascii_letters
