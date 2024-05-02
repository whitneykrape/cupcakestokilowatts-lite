Usage
=====

.. _installation:

Installation
------------

To use Cupcakes to kiloWatts, first ensure you have Docker and Docker Compose installed.

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``cupcakestokilowatts_docs.get_random()`` function:

.. autofunction:: cupcakestokilowatts_docs.get_random

The ``kind`` parameter should be either ``"one"``, ``"other"``,
or ``"third"``. Otherwise, :py:func:`cupcakestokilowatts_docs.get_random`
will raise an exception.

.. autoexception:: cupcakestokilowatts_docs.InvalidKindError

For example:

>>> import cupcakestokilowatts_docs
>>> cupcakestokilowatts_docs.get_random()
['one', 'other']

