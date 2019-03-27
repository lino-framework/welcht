.. _welcht.about:

======================
About this application
======================


.. py2rst::

  from lino_welcht import SETUP_INFO
  print(SETUP_INFO['long_description'])


Complexity factors:

.. py2rst::

  from lino.utils.diag import analyzer
  print(analyzer.show_complexity_factors())

