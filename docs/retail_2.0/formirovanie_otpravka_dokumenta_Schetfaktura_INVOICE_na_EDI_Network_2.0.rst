##################################################################################################################
Creating an "Invoice" (INVOICE) document based on other electronic documents
##################################################################################################################

.. сюда закину немного картинок для текста

.. |лупа| image:: pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_004.png

.. |будинок| image:: pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_005.png

.. role:: red

.. contents:: Contents:
   :depth: 2

---------

Introduction
====================================

This instruction describes the procedure for forming and sending the document "Invoice" (INVOICE) - this is a bill for payment, which is usually sent by the Supplier to the Grocery Store Chain for the final price agreement.

1 Formation of an "Invoice" (INVOICE) document on the basis of "Purchase Order" (ORDER) / "Purchase Order Response" (ORDRSP)
================================================================================================================================

.. початок блоку для INVOICE_standart

Formation of the "Invoice" document (INVOICE) on the EDI Network platform can be provided on the basis of "Purchase Order" (ORDER), as well as on the basis of "Purchase Order Response" (ORDRSP).

Let's consider the formation of the document "Invoice" (INVOICE) on the basis of "Purchase Order Response" (ORDRSP).

For this, You need to select "Purchase Order Response" (ORDRSP) for which you need to make a shipment in the **"Outbox"** folder (for convenience You can use `search <https://wiki.edin.ua/uk/latest/general_2_0/rabota_s_platformoj_EDIN_2.0.html#doc-search>`__):

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_001.png
   :align: center

It is necessary to open the sent "Purchase Order Response" (ORDRSP) with the left mouse button and create a "Invoice" (INVOICE) for Grocery Store Chain using the **"Create document"** button in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ block:

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_002.png
   :align: center

In the open "Invoice" (INVOICE) form, almost all fields are filled in automatically from the associated base document (mandatory fields are marked with a red asterisk :red:`*`):

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_003.png
   :align: center

**Sender** data is automatically filled in from the selected company and cannot be edited. The data of the **Recipient** are also filled in automatically (from the base document) - they can be edited using the "Search counterparty" button (|лупа|). **Document number** matches the base document number, **Date** of the document, which are filled automatically, are also available for editing if necessary. **Supplier**, **Buyer**, **Shipment Address** data are also filled in automatically - they can be edited using the "Search counterparty" (|лупа|) or "Point yourself" (|будинок|) buttons;

.. hint::
   With **"Search counterparty"** (|лупа|) button or **"Point yourself"** (|будинок|) button it is possible to specify or change the data of counterparties. When using **"Search counterparty"** (|лупа|), enter the company name, GLN or TIN in the window that appears:

   .. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_011.png
      :align: center

In the same way, it is possible to add (optionally) information about **Consignor**, **Consignee**, **Final recipient**, **Customer**, **Payer**.

You need to fill in next fields by selecting values from the drop-down list:

#. **Account currency** - choose a currency: UAH / EUR / USD
#. **With VAT rate** - choose a value added tax rate: 0% / 7% / 19% / 20%

In addition, it is important to specify **Delivery note №** / **from** - number and date of the original document - :red:`must completely match the number/date of the original paper waybill!`. It is also important to choose a delivery date (**Delivery must be made** field):

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_006.png
   :align: center

Data from "Purchase Order" is transferred automatically and cannot be edited. **Additional information** and **Supplier information** blocks are optional and "collapsed" by default. The **Total** block is calculated automatically after filling in the table positions.

:red:`All changes in positions must be made only after coordination with the Grocery Store Chain!`

The Supplier can edit the "Quantity", "Price without VAT" directly in the table or **"Change"** the data of the item in the advanced form "Position info" after clicking on the bar code of the item:

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_007.png
   :align: center

If there will be no delivery for some of the items, they must be marked with a check mark and **"Delete"**. It is also possible to **"+Add"** new product positions, but these actions must be coordinated with the Grocery Store Chain.

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_008.png
   :align: center

After entering all the data in the document, press the button **"Save"** (1), then **"Send"** (2):

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_009.png
   :align: center

The sent document automatically placed into the **"Outbox"** folder and will be in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ documents together with other documents (the number indicates the amount of documents in the chain):

.. image:: /retail_2.0/pics_INVOICE_na_EDI_Network_2.0/INVOICE_na_EDI_Network_010.png
   :align: center

.. кінець блоку для INVOICE_standart

-------------------------------------

.. include:: /_constant/kontakti.rst