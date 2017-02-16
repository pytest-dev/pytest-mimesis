Elizabeth_ integration with the pytest_ test runner
===============================================


pytest-elizabeth adds Elizabeth fixtures_ for easy use of Elizabeth_ for your tests under pytest_ runner.

.. _Elizabeth: https://github.com/lk-geimfari/elizabeth
.. _pytest: http://pytest.org/
.. _fixtures: https://pytest.org/latest/fixture.html

Install pytest-elizabeth
--------------------

::

    pip install pytest-elizabeth

Example
-------

An example of Elizabeth_ and pytest_ integration.


tests/test_plugin.py:

.. code-block:: python

    import elizabeth

    def test_generic(personal, elizabeth_locale):
    """Test elizabeth fixture."""
        assert isinstance(generic, elizabeth.Personal)
        assert personal.name()
        assert elizabeth_locale == 'en'


License
-------
pytest-elizabeth is licensed under the MIT License.