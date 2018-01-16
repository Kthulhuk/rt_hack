Download and Installation
=========================

Overview
--------

0. Install `Python 3 <https://www.python.org/downloads/>`_.
1. Download and install RT_Hack.

Install RT_Hack
---------------

The following steps describe how to install (or update) RT_Hack itself.

.. code-block:: bash

   $ git clone https://github.com/Kthulhuk/rt_hack
   $ cd rt_hack
   $ python3 setup.py install

Build the documentation offline
-------------------------------

The RT_Hack project's documentation is written using reStructuredText (files *.rst*) and can be built using the Sphinx python library. Go to the rt_hack folder and execute this command :

.. code-block:: bash

   $ make doc

The offline documentation should now be in rt_hack/docs/_build/html.