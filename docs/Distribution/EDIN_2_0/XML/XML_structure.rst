EDIN-Distribution XML Specifications 
##########################################

.. contents:: Contents:

---------

Price list (document PRICAT)
========================================

.. csv-table:: Price list (document PRICAT) serves to describe goods and services. This document is sent by the Producer; the document indicates the barcode of the product, its description, price, VAT rate. You can also use the PRICAT to specify price changes (increase / decrease).
  :file: files/PRICAT.csv
  :widths:  20, 11, 29, 37
  :header-rows: 1

:download:`PRICAT example<examples/pricat_example.xml>`

---------

Order (document ORDER)
==============================================

.. csv-table:: Order (document ORDER) is sent for delivery by the Distributor; the document indicates the barcode of the product, its description, ordered quantity, price and other necessary information.
  :file: files/ORDER.csv
  :widths:  20, 11, 29, 37
  :header-rows: 1

:download:`ORDER example<examples/order_example.xml>`

---------

Limitation (document LIMITS)
==============================================

.. csv-table:: Limitation (document LIMITS) to order is sent by the Producer; the document indicates the prices and quantities for the formation of the order from the specified Distributor.
  :file: files/LIMITS.csv
  :widths:  20, 11, 29, 37
  :header-rows: 1

:download:`LIMITS example<examples/distribex_limits_example.xml>`

-------------------------

.. [#] The definition of an abbreviated notation:

   * M (mandatory);
   * O (optional).



