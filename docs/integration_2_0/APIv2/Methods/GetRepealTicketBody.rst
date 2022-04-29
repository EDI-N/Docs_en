#######################################################################################################
**Creating a "Cancellation" ticket on the Server (COMDOC_019)**
#######################################################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

Using the GET method **api/v2/eds/comdoc/repeal** it is possible to create a "Repeal" COMDOC.

.. csv-table:: 
  :file: GetRepealTicketBody.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits the body of the generated COMDOC_019 in json format or format selected in the request with **response_type** (`response examples <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/EveryBody/GetRejectTicketBodyExample.html>`__ + `COMDOC_019 specification <https://wiki.edin.ua/uk/latest/XML/XML-structure.html#comdoc-019>`__)".

.. так тут спеціально два методи посилаються на одну сторінку (інших прикладів немає)
