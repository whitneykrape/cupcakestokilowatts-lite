"""
Cupcakes to kiloWatts - Python library for docs.

This is a Python docstring, we can use reStructuredText syntax here!

.. code-block:: python

    # Import cupcakestokilowatts_docs
    import cupcakestokilowatts_docs

    # Call its only function
    get_random(kind=["watts"])
"""

__version__ = "0.1.0"


class InvalidKindError(Exception):
    """Raised if the kind is invalid."""

    pass


def get_random(kind=None):
    """
    Return a list of random strings.
    """
    return ["watts", "kilowatts"]