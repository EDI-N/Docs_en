#######################################################################################################
**Receive ticket data / content**
#######################################################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

.. csv-table:: 
  :file: GetTicketBody.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits depending on the parameter **body_type** `signature data <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/EveryBody/SignInfo.html>`__ (json) or signature content (base64). 