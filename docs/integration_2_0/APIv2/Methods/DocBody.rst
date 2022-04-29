######################################################################
**Receiving document content**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

With the **api/eds/doc/body** method, you can quickly get the content of a document without signatures / seals, as well as the body of the signature or the body of the seal. The request must contain an authorized user ID (GLN), document ID (doc_uuid), document body type.

.. csv-table:: 
  :file: DocBody.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits string of values in the Base64 format.

