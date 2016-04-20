Documentation and Coding Standards
==================================

Naming Conventions
------------------

-  Choose short and concise names that reflect usage
-  Never use the characters 'l' (lowercase letter el), 'O' (uppercase
   letter oh), or 'I' (uppercase letter eye) as single character
   variable names
-  *Package and Module Names*:
-  Use all-lowercase names
-  Use underscores when appropriate in module names but not package
   names
-  *Class Names*:
-  Use ``CapWords`` convention
-  *Function and Variable Names*:
-  ``lower_case_with_underscores``
-  Use a descriptive verb in function names
-  *Constants*:
-  Use all capital letters with underscores separating words (e.g.
   ``YELLOW_MARINE``)

Indentation
-----------

-  Use 4 spaces per indentation level
-  Continuation lines should align wrapped elements vertically using
   Python's implicit line joining inside parentheses, brackets and
   braces

   .. code:: python

       # Aligned with opening delimiter
       nacho_cheese = not_your_cheese(cheddar, pepperjack,
                                      provolone, brie)

-  The closing brace/bracket/parenthesis on multi-line constructs should
   line up under the first non-whitespace character of the last line of
   list

   .. code:: python

       six_afraid_of_seven = [
           7, 8, 9,
           1, 0, 1
           ]

Docstrings
----------

-  We will be following
   `numpy <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`__
   conventions.
-  What is a Docstring?
-  A docstring is a string literal that occurs as the first statement in
   a module, function, class, or method definition. Such a docstring
   becomes the \_\ *doc\_* special attribute of that object.
-  When do we use docstrings?
-  All modules should normally have docstrings, and all functions and
   classes exported by a module should also have docstrings. Public
   methods (including the \_\ *init\_* constructor) should also have
   docstrings. A package may be documented in the module docstring of
   the \_\ *init\_*.py file in the package directory.
-  Formatting by type of object
-  The docstring of a **script** should be usable as its "usage"
   message, printed when the script is invoked with incorrect or missing
   arguments. Such a docstring should document the script's function and
   command line syntax, environment variables, and files. Usage messages
   should be sufficient for a new user to use the command properly, as
   well as a complete quick reference to all options and arguments for
   the sophisticated user.
-  If the stand-alone script uses another module for handling options,
   such as the argparse module, then option information is moved from
   the docstring to the module's utilities.
-  The docstring for a **module** should generally list the classes,
   exceptions, and functions that are exported by the module, with a
   one-line summary of each.
-  The docstring for a **package** (i.e., the \_\ *init\_*.py module)
   should also list the modules and subpackages exported by the package.
-  The docstring of a **function** or **method** is a phrase ending in a
   period. It prescribes the function or method's effect as a command
   ("Do this", "Return that"), not as a description; e.g. don't write
   "Returns the pathname ...". A multiline-docstring for a function or
   method should summarize its behavior and document its arguments,
   return value(s), side effects, exceptions raised, and restrictions on
   when it can be called. Optional arguments should be indicated. It
   should be documented whether keyword arguments are part of the
   interface.
-  The docstring for a **class** should summarize its behavior and list
   the public methods and instance variables. If the class is intended
   to be subclassed, and has an additional interface for subclasses,
   this interface should be listed separately. The class constructor
   should be documented in the docstring for its \_\ *init\_* method.
   Individual methods should be documented by their own docstring.
-  Example docstring
-  For consistency, always use ``"""triple double quotes"""`` around
   docstrings. Use ``r"""raw triple double quotes"""`` if you use any
   backslashes in your docstrings. For Unicode docstrings, use
   ``u"""Unicode triple-quoted strings"""`` .

   .. code:: python

       def foo(var1, var2, long_var_name='hi') :
           r"""A one-line summary that does not use variable names or the
           function name.

           Several sentences providing an extended description. Refer to
           variables using back-ticks, e.g. `var`.

           Parameters
           ----------
           var1 : array_like
               Array_like means all those objects -- lists, nested lists, etc. --
               that can be converted to an array.  We can also refer to
               variables like `var1`.
           var2 : int
               The type above can either refer to an actual Python type
               (e.g. ``int``), or describe the type of the variable in more
               detail, e.g. ``(N,) ndarray`` or ``array_like``.
           long_var_name : {'hi', 'ho'}, optional
               Choices in brackets, default first when optional.

           Returns
           -------
           type
               Explanation of anonymous return value of type ``type``.
           describe : type
               Explanation of return value named `describe`.
           out : type
               Explanation of `out`.

           Other Parameters
           ----------------
           only_seldom_used_keywords : type
               Explanation
           common_parameters_listed_above : type
               Explanation

           Raises
           ------
           BadException
               Because you shouldn't have done that.

           See Also
           --------
           otherfunc : relationship (optional)
           newfunc : Relationship (optional), which could be fairly long, in which
               case the line wraps here.
           thirdfunc, fourthfunc, fifthfunc

           Notes
           -----
           Notes about the implementation algorithm (if needed).

           This can have multiple paragraphs.

           You may include some math:

           .. math:: X(e^{j\omega } ) = x(n)e^{ - j\omega n}

           And even use a greek symbol like :math:`omega` inline.

           References
           ----------
           Cite the relevant literature, e.g. [1]_.  You may also cite these
           references in the notes section above.

           .. [1] O. McNoleg, "The integration of GIS, remote sensing,
               expert systems and adaptive co-kriging for environmental habitat
               modelling of the Highland Haggis using object-oriented, fuzzy-logic
               and neural-network techniques," Computers & Geosciences, vol. 22,
               pp. 585-588, 1996.

           Examples
           --------
           These are written in doctest format, and should illustrate how to
           use the function.

           >>> a=[1,2,3]
           >>> print [x + 3 for x in a]
           [4, 5, 6]
           >>> print "a\n\nb"
           a
           b

           """

           pass

           ...


Comments
--------

-  Use complete sentences; if a comment is a phrase or sentence, its
   first word should be capitalized, unless it is an identifier that
   begins with a lowercase letter
-  Use two spaces after a sentence-ending period
-  Indent block comments to the same level as the code below; start each
   line of a block comment with a # and a single space (unless it is
   indented text inside the comment)
-  Separate paragraphs inside a block comment by a line containing a
   single #

``python   # How dows a mouse feel after it takes a shower?   # Squeaky clean.   #    # How do you save a drowning mouse?   # Use mouse to mouse resuscitation.   not_your_cheese(marscapone, maasdam, camembert, roquefort)``
- Use inline comments sparingly

``python   not_your_cheese(gorgonzola, munster, limburger, doppelrhamstufel) # Not your cheese, my cheese.``

.. raw:: html

   <div id='blank-lines'/>

Blank Lines
-----------

-  Surround top-level function and class definitions with two blank
   lines
-  Surround method definitions inside a class with a single blank line
-  Use extra blank lines sparingly to separate groups of related
   functions; omit blank lines between related one-liners (e.g. a set of
   dummy implementations) if desired
-  Use blank lines in functions sparingly to indicate logical sections

.. raw:: html

   <div id='whitespace'/>

Whitespace
----------

-  Avoid extraneous whitespace:
-  Immediately inside parentheses, brackets, or braces
-  Immediately before a comma, semicolon, or colon
-  Immediately before the open parenthesis that starts the argument list
   of a function call
-  Immediately before the open parenthesis that starts an indexing or
   slicing
-  More than one space around an assignment (or other) operator to align
   it with another
-  Always surround these binary operators with a single space on either
   side: assignment ( = ), augmented assignment ( += , -= etc.),
   comparisons ( == , < , > , != , <> , <= , >= , in , not in , is , is
   not ), Booleans ( and , or , not )
-  If operators with different priorities are used, consider adding
   whitespace around the operators with the lowest priority(ies); never
   use more than one space, and always have the same amount of
   whitespace on both sides of a binary operator

``python   eyes = e + yes   cyclops = eyes*4 - 3   c = (a+b) * (a-b)`` -
Do not use spaces around the = sign when used to indicate a keyword
argument or a default parameter value

::

    ```python

def not\_your\_cheese(cheese1=smelly, cheese2=stinky, cheese3=noxious,
cheese4=bad) return my\_cheese(r=real, i=imag) \`\`\` - Avoid compound
statements (multiple statements on the same line) - Never put an
if/for/while with a multi-clause statement on the same line

String Quotes
-------------

-  Generally, use double-quotes for strings, but if a string contains a
   double-quote, then use single quotes
-  Keep string quotes consistent for readability

Imports
-------

-  Put imports on separate lines, e.g.:

``python   import os   import sys   from subprocess import Popen, PIPE``
- Put imports at the top of the file, just after any module comments and
docstrings, and before module globals and constants - Avoid wildcard
imports ( from import \* ) as they make it unclear which names are
present in the namespace, confusing both readers and many automated
tools

Maximum Line Length
-------------------

-  Limit all lines to a maximum of 79 characters
-  Use backslashes when implicit continuation fails

``python   with open("/why/did/the/chicken/cross/the/road") as chicken, \        open("/to/get/to/the/other/side", "w") as waffles:        waffles.write(chicken.read())``

For more information, please refer to: `Style Guide for Python
Code <https://www.python.org/dev/peps/pep-0008/>`__ and `Docstring
Guide <https://github.com/numpy/numpy/blob/master/doc/HOWTO_DOCUMENT.rst.txt>`__
