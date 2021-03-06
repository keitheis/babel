.. -*- mode: rst; encoding: utf-8 -*-

============
Introduction
============

The functionality Babel provides for internationalization (I18n) and
localization (L10N) can be separated into two different aspects:

 * tools to build and work with ``gettext`` message catalogs, and
 * a Python interface to the CLDR (Common Locale Data Repository), providing
   access to various locale display names, localized number and date
   formatting, etc.


Message Catalogs
================

While the Python standard library includes a
`gettext <http://docs.python.org/lib/module-gettext.html>`_ module that enables
applications to use message catalogs, it requires developers to build these
catalogs using GNU tools such as ``xgettext``, ``msgmerge``, and ``msgfmt``.
And while ``xgettext`` does have support for extracting messages from Python
files, it does not know how to deal with other kinds of files commonly found
in Python web-applications, such as templates, nor does it provide an easy
extensibility mechanism to add such support.

Babel addresses this by providing a framework where various extraction methods
can be plugged in to a larger message extraction framework, and also removes
the dependency on the GNU ``gettext`` tools for common tasks, as these aren't
necessarily available on all platforms. See `Working with Message Catalogs`_
for details on this aspect of Babel.

.. _`Working with Message Catalogs`: messages.html


Locale Data
===========

Furthermore, while the Python standard library does include support for basic
localization with respect to the formatting of numbers and dates (the
`locale <http://docs.python.org/lib/module-locale.html>`_ module, among others),
this support is based on the assumption that there will be only one specific
locale used per process (at least simultaneously.) Also, it doesn't provide
access to other kinds of locale data, such as the localized names of countries,
languages, or time-zones, which are frequently needed in web-based applications.

For these requirements, Babel includes data extracted from the `Common Locale
Data Repository (CLDR) <http://unicode.org/cldr/>`_, and provides a number of
convenient methods for accessing and using this data. See `Locale Display
Names`_, `Date Formatting`_, and `Number Formatting`_ for more information on
this aspect of Babel.


.. _`Locale Display Names`: display.html
.. _`Date Formatting`: dates.html
.. _`Number Formatting`: numbers.html
