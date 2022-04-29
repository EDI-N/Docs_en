######################################################################
**Creating a ticket №14 (revoke COMDOC signing)**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

.. important:: Only the sender of the document can revoke the signing of the COMDOC document before the document changes its status to:

- revoked (the document has ticket №14)
- rejected (the document has ticket №13)
- repealed (the document has ticket №12)
- accepted (the document has ticket №2)

The value *[ЕлектроннийДокумент/Відхилив/GLN]* must match the *gln* parameter in the request. The USREOU must comply with the signature *[КодКонтрагента]* or *[ІПН]* in one of the blocks *[ЕлектроннийДокумент/Сторони/Контрагент]*

.. csv-table:: 
  :file: ComdocRevoke.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits:

**chain_uuid** - the identifier of the chain in which the document is located

**doc_uuid** - document ID with a ticket

**ticket_uuid** - ticket ID

**Example (JSON):**

.. code:: json

	{
	  "chain_uuid": "7b6aef20-9f42-460e-9031-bb81c91e3b03",
	  "doc_uuid": "e013510a-4267-4553-80f0-eb5ebabdfd05",
	  "ticket_uuid": "1003706c-3656-497b-9438-c6f33e27c36d"
	}