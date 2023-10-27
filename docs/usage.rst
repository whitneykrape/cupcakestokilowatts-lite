Usage
=====

.. _installation:

Installation
------------

To use Cupcakes to Kilowatts, first install it using pip:

.. code-block:: console

   (.venv) $ pip install cupcakestokilowatts_docs

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

