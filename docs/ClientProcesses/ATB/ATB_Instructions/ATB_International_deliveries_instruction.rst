######################################################################################################################################################
Document flow with the Grocery Store Chain "ATB" on the EDI Network 2.0 platform: "International deliveries". Instruction for the Supplier
######################################################################################################################################################

.. сюда закину немного картинок для текста

.. |лупа| image:: pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_003.png

.. |будинок| image:: pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_004.png

.. |прокрутка1| image:: /retail_2.0/pics_formuvannia_Condra/formuvannia_Condra_026.png

.. |прокрутка2| image:: /retail_2.0/pics_formuvannia_Condra/formuvannia_Condra_027.png

.. |trash| image:: /retail_2.0/pics_formuvannia_Condra/formuvannia_Condra_025.png

.. role:: red

.. contents:: Contents:
   :depth: 2

---------

Introduction
====================================

This instruction describes the document flow procedure with Grocery Store Chain "ATB" on the EDI Network 2.0 platform according to the scheme provided for international deliveries. Document flow is organized by the following documents:

- `Purchase Order <https://wiki.edin.ua/uk/latest/ClientProcesses/ATB/ATB_XML-structure.html#order>`__
- `Purchase Order Response <https://wiki.edin.ua/uk/latest/ClientProcesses/ATB/ATB_XML-structure.html#ordrsp>`__
- `Despatch Advice <https://wiki.edin.ua/uk/latest/ClientProcesses/ATB/ATB_XML-structure.html#desadv>`__
- `Invoice <https://wiki.edin.ua/uk/latest/XML/XML-structure.html#invoice>`__
- `Universal Document <https://wiki.edin.ua/uk/latest/XML/XML-structure.html#condra>`__

**General document flow scheme:**

.. image:: pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_053.png
   :height: 700px
   :align: center

.. початок блоку для Universal_International_transportation

1 Login to the platform
====================================

.. include:: /general_2_0/rabota_s_platformoj_EDIN_2.0.rst
   :start-after: .. початок блоку для Enter
   :end-before: .. кінець блоку для Enter

After successful authorization, the main menu will open, where You need to select the **"EDI+UZD"** service in the **"Services"** EDIN tab:

.. image:: /_constant/pics_landing/landing_edi.png
   :align: center

.. _ordrsp-create:

2 Formation of "Purchase Order Response" (ORDRSP) based on incoming "Purchase Order" (ORDER)
==============================================================================================================

Grocery Store Chain is the initiator of the document flow and sends the "Purchase Order" (ORDER). To form a "Purchase Order Response" (ORDRSP), you need to select "Purchase Order" (ORDER) in the **"Inbox"** folder, which You need to confirm (for convenience You can use `search <https://wiki.edin.ua/uk/latest/general_2_0/rabota_s_platformoj_EDIN_2.0.html#doc-search>`__):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_054.png
   :align: center

It is necessary to open the incoming "Purchase Order" (ORDER) with the left mouse button and create a "Purchase Order Response" (ORDRSP) for Grocery Store Chain with **"Create document"** button in the block `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ :

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_055.png
   :align: center

In the open "Purchase Order Response" (ORDRSP) form, some fields are filled automatically from the associated "Purchase Order" (mandatory fields are marked with a red asterisk :red:`*`):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_056.png
   :align: center

**Sender** / **Recipient** data are filled in automatically from the base document and the selected company and cannot be edited. Document subtype **Purchase Order Response** (*Purchase Order Response*, *Purchase Order Response Replacement*, *Deleting a Purchase Order Response*), **Number**, **Date** / time of the document are filled automatically, but available for editing as necessary. **Buyer**, **Supplier**, **Shipping Address** data are also filled in automatically - they can be edited using the "Search counterparty" buttons (|лупа|) or "Point yourself" (|будинок|);

.. hint::
   With **"Search counterparty"** (|лупа|) button or **"Point yourself"** (|будинок|) button it is possible to specify or change the data of counterparties. When using **"Search counterparty"** (|лупа|), enter the company name, GLN or TIN in the window that appears:

   .. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_005.png
      :align: center

In the same way, it is possible to add (optionally) information about **Final recipient**, **Payer**, **Shipments point**, **Consignee**. Data from "Purchase Order" is transferred automatically and cannot be edited.

You must select a order currency from the drop-down list (UAH / EUR / USD):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_070.png
   :align: center

The **Additional Information** and **Ramps** blocks are optional and "collapsed" by default. Block **Total** is calculated automatically after filling table positions.

The tabular part displays basic information on the ordered **goods items**. **Items** are carried from "Purchase Order" and "Will be delivered" by default. It is possible to adjust the value of **Confirmed quantity** of the product directly in the table (with adjustments at the same time the item automatically will receive "Quantity change"):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_057.png
   :align: center

.. attention::
   The confirmed quantity of product items cannot exceed the ordered quantity indicated in the "Purchase Order"!

It is also possible to choose (mark with a checker) the items for which you need to change the delivery status to **Will be delivered** (**Confirmed quantity** = **Ordered quantity**) or **Denied** (**Confirmed quantity** =0) using the **"Actions on selected"** button:

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_058.png
   :align: center

:red:`All changes in positions must be made only after coordination with the Grocery Store Chain!`

The Supplier can edit "Confirmed quantity" and "Price without VAT" directly in the table or **"Change"** item data in the advanced form "Position info" after clicking on the barcode of the item:

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_068.png
   :align: center

If there will be no delivery for some of the items, they must be marked with a check mark and **"Delete"**. It is also possible to **"+Add"** new product positions, but these actions must be coordinated with the Grocery Store Chain.

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_069.png
   :align: center

After entering all the data in the document, press the button **"Save"** (1), then **"Send"** (2):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_059.png
   :align: center

The sent document automatically placed into the **"Outbox"** folder and will be in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ documents together with "Purchase Order":

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_060.png
   :align: center

.. _desadv-create:

3 Formation of "Despatch Advice" (DESADV)
=========================================================================================================================

The formation of the "Despatch Advice" (DESADV) document on the EDI Network platform can be carried out on the basis of "Purchase Order" (ORDER) as well as on the basis of "Purchase Order Response" (ORDRSP).

Let's consider the formation of the "Despatch Advice" (DESADV) document on the basis of "Purchase Order Response" (ORDRSP).

For this, You need to select "Purchase Order Response" (ORDRSP) for which you need to make a shipment in the **"Outbox"** folder (for convenience You can use `search <https://wiki.edin.ua/uk/latest/general_2_0/rabota_s_platformoj_EDIN_2.0.html#doc-search>`__): 

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_061.png
   :align: center

It is necessary to open the sent "Purchase Order Response" (ORDRSP) with the left mouse button and create a "Despatch Advice" (DESADV) for Grocery Store Chain using the **"Create document"** button in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ block:

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_062.png
   :align: center

In the open "Despatch Advice" (DESADV) form, almost all fields are filled in automatically from the associated base document (mandatory fields are marked with a red asterisk :red:`*`):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_063.png
   :align: center

**Sender** data is automatically filled in from the selected company and cannot be edited. The data of the **Recipient** are also filled in automatically (from the base document) - they can be edited using the "Search counterparty" button (|лупа|). **Document number** matches the base document number, **Date** / time of the document, which are filled automatically, are also available for editing if necessary. **Supplier**, **Buyer**, **Shipment Address** data are also filled in automatically - they can be edited using the "Search counterparty" (|лупа|) or "Point yourself" (|будинок|) buttons;

.. hint::
   With **"Search counterparty"** (|лупа|) button or **"Point yourself"** (|будинок|) button it is possible to specify or change the data of counterparties. When using **"Search counterparty"** (|лупа|), enter the company name, GLN or TIN in the window that appears:

   .. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_005.png
      :align: center

In the same way, it is possible to add (optionally) information about the **Final Recipient**. Data from "Purchase Order" is transferred automatically and cannot be edited. **Additional information** and **Transportation** blocks are optional and "collapsed" by default. The **Total** block is calculated automatically after filling in the table positions.

:red:`All changes in positions must be made only after coordination with the Grocery Store Chain!`

The supplier can edit the "Delivered Quantity", "Price without VAT" and "VAT rate" directly in the table or **"Change"** the data of the item in the advanced form "Position info" after clicking on the bar code of the item:

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_064.png
   :align: center

.. attention::
   The confirmed quantity of product items cannot exceed the ordered quantity indicated in the "Purchase Order"!

If there will be no delivery for some of the items, they must be marked with a check mark and **"Delete"**. It is also possible to **"+Add"** new product positions, but these actions must be coordinated with the Grocery Store Chain.

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_065.png
   :align: center

After entering all the data in the document, press the button **"Save"** (1), then **"Send"** (2):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_066.png
   :align: center

The sent document automatically placed into the **"Outbox"** folder and will be in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ documents together with "Purchase Order" and "Purchase Order Response" (the number indicates an amount of documents in the chain):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_067.png
   :align: center

.. _invoice-create:

4 Formation of "Invoice" (INVOICE)
=========================================================================================================================

.. зараз все стандартно, тому копіпастимо сюди:

.. include:: /retail_2.0/formirovanie_otpravka_dokumenta_Schetfaktura_INVOICE_na_EDI_Network_2.0.rst
   :start-after: .. початок блоку для INVOICE_standart
   :end-before: .. кінець блоку для INVOICE_standart

.. _condra-create:

5 Formation of the "Universal Document" (CONDRA) on the basis of the sent "Despatch Advice" (DESADV)
=========================================================================================================================

To form "Universal Document" (CONDRA) at first You need to select "Despatch Advice" (DESADV) for which you need to make a shipment in the **"Outbox"** folder (for convenience You can use `search <https://wiki.edin.ua/uk/latest/general_2_0/rabota_s_platformoj_EDIN_2.0.html#doc-search>`__):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_071.png
   :align: center

It is necessary to open the sent "Despatch Advice" (DESADV) with the left mouse button and create a "Universal Document" (CONDRA) for Grocery Store Chain using the **"Create document"** button in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ block:

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_072.png
   :align: center

In the open "Universal Document" (CONDRA) form, some fields are filled in automatically from the associated base document (mandatory fields are marked with a red asterisk :red:`*`):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_073.png
   :align: center

**Sender** data is automatically filled in from the selected company and cannot be edited. The data of the **Recipient** are also filled in automatically (from the base document) - they can be edited using the "Search counterparty" button (|лупа|). **Document number** matches the base document number, **Date** of the document, which are filled automatically, are also available for editing if necessary.

Optionally, it is possible to choose the type of document, specify the contract number/date; the number and date of the basic document filled in automatically.

**Supplier**, **Buyer**, **Shipment Address** data are also filled in automatically - they can be edited using the "Search counterparty" (|лупа|) or "Point yourself" (|будинок|) buttons;

.. hint::
   With **"Search counterparty"** (|лупа|) button or **"Point yourself"** (|будинок|) button it is possible to specify or change the data of counterparties. When using **"Search counterparty"** (|лупа|), enter the company name, GLN or TIN in the window that appears:

   .. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_005.png
      :align: center

With the **"Choose file"** button, it is possible to select and add accompanying documents in the form of pdf files, for example, a certificate (files are selected from your local media):

.. include:: /retail_2.0/formuvannia_universalnoho_dokumenta_Condra.rst
   :start-after: .. початок блоку для CONDRA_standart
   :end-before: .. кінець блоку для CONDRA_standart

After entering all the data in the document, press the button **"Save"** (1), then **"Send"** (2) without signing:

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_074.png
   :align: center

The sent document automatically placed into the **"Outbox"** folder and will be in the `document chain <https://wiki.edin.ua/uk/latest/_constant/chain/chain.html>`__ documents together with other documents (the number indicates the amount of documents in the chain):

.. image:: /ClientProcesses/ATB/ATB_Instructions/pics_ATB_International_deliveries_instruction/ATB_International_deliveries_instruction_075.png
   :align: center

If necessary, Grocery Store Chain may create a "Universal Document" (CONDRA) in response, along with suggested edits and comments.

.. кінець блоку для Universal_International_transportation

-------------------------------------

.. include:: /_constant/kontakti.rst
