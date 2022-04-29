######################################################################
**Drafts sending**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

Using the method **/api/eds/doc/send** it is possible to send a draft (with additional features of sending). 

.. note:: The presence of a retailer in the document flow is automatically determined by the platform (ie if the Sender or Recipient is a retailer, the created chain will be marked by a specific retailer)

.. attention::
  The body of the request and all its parameters are optional!

.. csv-table:: 
  :file: SendDocument.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

Server code 200 (ok).
