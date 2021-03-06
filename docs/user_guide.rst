==========
User Guide
==========

What is the Devinstaller system?
================================

The ``spec`` file is where all your instructions are written. Some
people call it the config file, others the bootstrap script but we call
it the ``spec`` file.

The ``spec`` file is super easy to create and it can handle any types of
needs.

The Schema for the ``spec`` file was designed with care taken for its
scaling needs. Your spec file should scale according to your needs.

If its a small need then it should be very simple and if its a very
complicated need then you should have all the tools you need.

This is where things gets interesting. Where other tools can't meet your
complicated needs you end up writing shell script or some other script.
But we all know the problems with that.

Shell scripts often feels hacky and it doesn't give you the full
features of a programming language like Python.

If you go with the Python script or other similar route then everyone
needs to be onboard with it.

Some technology stack doesn't go hand in hand with Python. Say you are
working with a team on web development or some NodeJS based application
not everyone will feel comfortable with a Python script laying around
for bootstrapping your new team members onto the project.

This is where Devinstaller comes in. The Devinstaller Schema for the
spec file is completely blind to the application which executes it.

So the same spec file can be run by a Devinstaller application written
in Python as well as another Devinstaller application written in Java,
Go etc.

So this gives us a declarative way of specifying what your needs are.

But now you might feel that the spec file may not have the full power of
a real programming language and you are right.

And here comes the ``prog`` file.

``prog`` file are scripts written in any programming language that your
Devinstaller application supports. But the main feature of it is that
``prog`` files are completely integrated into the Devinstaller
Specification so ``prog`` files when executed gets full access into the
``spec`` file.

This means the static ``spec`` file you are holding now can be read,
modified and executed in any order and in any way your ``prog`` file
wants to do.

This integration by the Devinstaller Specification makes it possible.

So for all your regular needs the ``spec`` file should do the trick, but
when push comes to shove you have full power of a real programming
language in your hands.

So for most cases you never need to write the ``prog`` file. And the
Devinstaller Specification for the ``spec`` file is always evolving so
the need for your ``prog`` file today might end up being solved by the
``spec`` file tomorrow.

And even if its not you can always extend the Devinstaller
Specification. The Specification makes sure it itself is highly
customizable and you can create an application to execute it.

The best part being you don't have to create a whole Devinstaller
application from scratch.

You can import ``Devin,`` you can customize it to suit your needs and
you can use your new customized Devinstaller engine to create a whole
brand of applications for your needs specifcally.

What is this library?
=====================

This library is an application engine which you can use to create
applications which can create, read, modify and execute the
``devinstaller files``.

This library is the primary engine behind the **Devinstaller** family of
applications.

Nicknamed: ``Devin``

What is ``devinstaller files``?
-------------------------------

The Devinstaller files is a pair of

-  Static config file and
-  Dynamic script (Example: Python script file)

How it works?
-------------

Step 1: Identify your needs
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to do something programatically like installing bunch of
softwares in your machine, migrating files folders and applications from
one machine to another. Setup the developer environment for your new
recruit on your project and any other needs like that.

Step 2: Install a Devinstaller application for that need
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

All Devinstaller application are not the same. Some does one thing
another does completely different thing.

But one thing is sure all the Devinstaller applications can handle the
``devinstaller files``. All of them can read the same but all of them
may not interpret it the same.

These applications are powered by ``Devin``.

Once you find the application install it by referring its install guide.

Step 3: Write the ``spec`` file to execute your instructions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You create a simple config file in one of the file format below:

-  ``Toml``
-  ``Yaml``
-  ``JSON``

and describe what you want to do in it using the Schema specified by the
`Devinstaller specification <https://gitlab.com/devinstaller/deps>`__.

Step 4: Execute
~~~~~~~~~~~~~~~

How to use this library?
========================
