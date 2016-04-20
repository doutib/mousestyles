Writing tests
=============

We need to create unit tests for each module and test each function of the module.

An introductory example
-----------------------

Suppose we have a file called *data_utils.py* with two functions ``func1`` and ``func2``, we should have a corresponding test file called *test_data_utils.py* with two corresponding test functions called ``test_func1`` and ``test_func2`` and *data_utils.py* imported.

- Note that we use ``pytest`` in our framework. Always import pytest at the top of the test file.
- Please follow the naming convention: `test_\*.py` for test file and `test_\*` for test functions.

.. code:: python

   # content of mousestyles/mousestyles/utils.py
   def func1():
      return 3

   def func2(x):
      return x + 1

.. code:: python

   # content of mousestyles/mousestyles/tests/test_utils.py
   from __future__ import (absolute_import,
                           division, print_function,
                           unicode_literals)

   import pytest

   from mousestyles.utils import func1, func2

   def test_func1():
      assert f() == 3

   def test_func2():
      assert func(3) == 4

Run all the tests for mousestyles
---------------------------------

-  For our ``mousestyles`` package, you can run all the tests with
   ``make test``. Note that ``make test`` always run make ``make install``,
   thus you do not need to install beforehand.

-  Run ``make test-fast`` for quicker (but less foolproof) development. 

-  If you want to look at the details, code for ``make`` command can be
   found `here <https://github.com/berkeley-stat222/mousestyles/blob/master/Makefile>`__.

Pytest: basic usage
-------------------

Installation:

.. code:: 

   pip install -U pytest

Run all files in the current directory and its subdirectories of the form
`test_*.py` or `*_test.py`:

.. code:: 

   $ py.test

Or you may run one test file with or without "quiet" reporting mode:

.. code:: 

   $ py.test test_data_utils.py
   $ py.test -q test_data_utils.py

Pytest: writing and reporting of assertions
-------------------------------------------

``pytest`` allows you to use the standard python ``assert`` for verifying
expectations and values. For example:

.. code:: python

   # contents of example1.py
   def f():
      return 3

   def test_function():
      assert f() == 4

If we run ``example1.py`` using ``py.test example1.py``, it will fail because
the expected value is 4, but ``f`` return 3.

We can also specify a message with the assertion like this:

.. code:: python

   assert a % 2 == 0, "value was odd, should be even"

In order to write assertions about raised exceptions, you can use pytest.raises
as a context manager like this:

.. code:: python

   import pytest

   def test_zero_division():
      with pytest.raises(ZeroDivisionError):
         1 / 0

   def test_exception():
      with pytest.raises(Exception):
         x = 1 / 0


See  `Built-in Exceptions
<https://docs.python.org/2/library/exceptions.html>`__ for more about raising
errors.

If you need to have access to the actual exception info you may use:

.. code:: python

   def test_recursion_depth():
      with pytest.raises(RuntimeError) as excinfo:
         def f():
            f()
         f()
    assert 'maximum recursion' in str(excinfo.value)

Pytest also support expected warnings, see `pytest.warn
<https://pytest.org/latest/recwarn.html#warns>`__

For more about assertions, see `Assertions in pytest
<https://pytest.org/latest/assert.html#assert>`__

What aspects of a function need to be tested:
---------------------------------------------

-  check if it returns correct type of object
-  check if it returns correct dimension
-  check if it returns the correct value, by

   -  prior knowledge
   -  different implementation: i.e. use R vs Python; use
      $Var(X)$ vs. $E(X^2) - E(X)^2$
   -  theoretical derivation

-  "regression": if the function is improved (by speed, efficiency)
   while has same functionality, check the output is the same with older
   version.
-  assert errors occured: i.e. when the function takes three arguements
   while we only give two, make sure the function will throw an error
   message

Reference
---------

Most example above comes from Pytest documentation. See `Pytest Documentation
<https://pytest.org/latest/index.html>`__ for more detail. 
