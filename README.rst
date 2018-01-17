=======
RT_Hack
=======

About Attack Toolkit
--------------------

The Attack Toolkit By JH is a simple CLI (command-line interface) allowing the user to perform attacks against another interface. This toolkit was made as a third-year project at ENSEA in the Networks and Communications Branch under the supervision of Christophe BARES. It was built upon the work of Giuliani Carlo and Montini Nicola from the University of Padova.

There are two types of functions in the toolkit : 

- Reconnaisance functions
- Denial of service functions

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

Starting RT_Hack
----------------

RT_Hack's interactive shell is run in a terminal session. Root privileges are needed to send the packets, so we’re using sudo here:

.. code-block:: bash

   $ sudo rt_hack

Then, simply follow the interactive shell. Below, you'll find a small description of each function.