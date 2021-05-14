#######################################################################################################
**Obtaining information about subscribers**
#######################################################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__ .

.. csv-table:: 
  :file: GetSignersInfo.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits information about subscribers (array of `ExEndUserSignInfo <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/EveryBody/ExEndUserSignInfo.html>`__ objects).

.. note::
  If the ticket does not contain a body with transaction type 1 or more, then the method response transmits an empty array of signatories (for example, when revoking the signing of a COMDOC document). 