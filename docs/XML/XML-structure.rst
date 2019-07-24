XML Specifications
######################

**XML specification of electronic documents**

The specification describes the fields XML-documents, which are used in EDI-N electronic data exchange platform.

Field type abbreviation:
– M (mandatory);
– O (optional).

---------

.. contents:: Contents:

---------

Order (document ORDER)
=============

.. csv-table:: The buyer send the "order for delivery" (ORDER) to the supplier. ORDER contents the barcode of the product, product description, ordered quantity, price and other necessary information.
  :file: files/ORDER.csv
  :widths:  40, 7, 12, 41
  :header-rows: 1

.. include:: units.rst

---------

Order Confirmation (document ORDRSP)
=============================

.. csv-table:: Order confirmation (ORDRSP) is a response document to order (ORDER). It is an order confirmation for each product (whether it will be delivered; price; amount changed or refuse delivery of goods info)
  :file: files/ORDRSP.csv
  :widths:  40, 7, 12, 41
  :header-rows: 1

.. include:: units.rst

---------

Shipping notice (document DESADV)
================================

.. csv-table:: The supplier sends a Shipping Notice (DESADV) in response to an Order (ORDER). In this case, the supplier can change the quantity of goods ordered, the date and time of delivery, specify additional information. This document is an waybill analog
  :file: files/DESADV.csv
  :widths:  40, 7, 12, 41
  :header-rows: 1

.. include:: units.rst

---------

Commercial document (document COMDOC)
==============================

.. csv-table:: COMDOC (ElectronicDocument) – a document intended for electronic exchange of legally significant documents (subject to conclusion by contracting parties of the agreement "On the recognition of electronic documents" and the use of electronic-digital signature)
  :file: files/COMDOC.csv
  :widths:  40, 7, 12, 41
  :header-rows: 1


.. include:: units.rst


