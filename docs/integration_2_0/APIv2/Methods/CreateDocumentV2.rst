######################################################################
**Create a draft document**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

Using the POST method **/api/v2/eds/doc** it is possible to create a draft of the document of the specified type for the specified recipient.

.. csv-table:: 
  :file: CreateDocumentV2.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits data of the created document (object `XDoc <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/EveryBody/XDocPage.html>`__ ).
