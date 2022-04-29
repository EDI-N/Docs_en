#######################################################################################################
**Creating a "Notice of refusal to sign the document" ticket on the server (COMDOC_021)**
#######################################################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

Using the GET method **api/v2/eds/comdoc/reject** it is possible to create a "Reject" COMDOC.

.. csv-table:: 
  :file: GetRejectTicketBody.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits the body of the generated COMDOC_021 in json format or format selected in the request with **response_type** (`response examples <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/EveryBody/GetRejectTicketBodyExample.html>`__ + `COMDOC_021 specification <https://wiki.edin.ua/uk/latest/XML/XML-structure.html#comdoc-021>`__)".

.. так тут спеціально два методи посилаються на одну сторінку (інших прикладів немає)