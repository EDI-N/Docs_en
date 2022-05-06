########################################################################################################################
Transport search (integration with Lardi Trans)
########################################################################################################################

.. початок блоку для TransportSearch

.. role:: green

.. role:: red

.. |trans| image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_009.png

When viewing `Order (ORDERS) <https://wiki.edin.ua/uk/latest/XML/XML-structure.html#order>`__ in **"Have Product"** or **"EDI+UZD"** services there is an opportunity **"Find transport"** within the program of integration with the **Lardi Trans** logistics platform:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_001.png
   :align: center

At the initial registration on the website of our partner (Lardi Trans) you need to enter the authorization token (in the token entry window all the actions are described in details):

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_002.png
   :align: center

You need to enter a token in the window and **"Save"**:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_003.png
   :align: center

.. hint::
   If necessary, it is always possible to **"Edit token"** in the "Transport search order" form.

At all subsequent attempts **"Find transport"** it is not necessary to enter the token (authorization with **Lardi Trans** is performed automatically). Then the **"Transport search order"** modal window opens:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_004.png
   :align: center

All required fields are marked with a red asterisk :red:`*`. The search is performed when you specify the location (from where and where you want to carry out transportation), as well as the typical cargo - you need to choose the founded values from list:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_005.gif
   :align: center

After you have filled in all the required request fields and agreed with the rules for placing request for **Lardi Trans** You can **"Publish"** it:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_006.png
   :align: center

.. important::
   Only one "Transport search order" can be issued for one "Order"!

When viewing "Order" with "Transport search order" the status of the those order is specified:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_007.png
   :align: center

* :green:`Published` - transport order is published on **Lardi Trans** platform;
* :red:`Deleted` - transport order is deleted from **Lardi Trans** platform;

"Order" with "Transport search order" are marked in the "Inbox" / "Outbox" document journal with |trans| icon. Those docs are easy to find using the `Search bar <https://wiki.edin.ua/uk/latest/ClientProcesses/Clients_list.html>`__ with *#TransportationOrder* key:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_008.png
   :align: center

When you click on the **"Order created"** button in the :green:`Published` status a modal window with the data on which the order was created opens. In the form it is possible to get acquainted with the data of transport search, **"Edit token"**, send the order **"To trash"** - delete the application from the **Lardi Trans** platform:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_010.png
   :align: center

.. hint::
   "Transport order" is sent **"To trash"** in case when the vehicle was found or mistakes were made in the order. When "Transport order" is sent **"To trash"** order changes it status at :red:`Deleted`.

When "Transport order" is sent **"To trash"** order is available for viewing, You may **"Restore"** it (order returns to :green:`Published` status) or You may irrevocably **"Delete"** it:

.. image:: /Openprice/Instructions/pics_Transport_Search/Transport_Search_011.png
   :align: center

.. hint::
   Only after deleting the "Transport order" it can be re-created (refilled) for this "Order" document!

.. кінець блоку для TransportSearch


