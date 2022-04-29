######################################################################
**Send a document (without creating a draft)**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

This POST method **/api/eds/doc/create_and_send** creates and sends the document at the same time. 

.. csv-table:: 
  :file: SendDocumentWithoutDraft.csv
  :widths:  10, 41
  :stub-columns: 0

.. note::
	With specifying of ``application/pkcs7-signature``, the possibility of processing BASE64 format is available.

**RESPONSE**

**chain_uuid** - the identifier of the chain in which the document is located;

**doc_uuid** - document ID on the EDIN 2.0 platform;

**ticket_uuid** - ticket ID (for COMDOC documents).

**Response example (JSON):**

.. code:: json

	{
	  "chain_uuid": "7ccff78e-ea42-47ea-81e4-5508ed4fbd51",
	  "doc_uuid": "3698b501-e1ef-464d-a71a-58066f556114",
	  "ticket_uuid": "1003706c-3656-497b-9438-c6f33e27c36d"
	}





