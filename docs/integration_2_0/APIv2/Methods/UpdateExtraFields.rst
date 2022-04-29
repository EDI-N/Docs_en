.. deprecated (not for integrated users - web only) Ok, this is an exception for CONDRA (temporary) - delete when another api will be ready

######################################################################
**Indexes filling (adding / updating extra parameter fields)**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

.. important::
  Filling in indexes is necessary for correct display and search of documents. In fact it is a repetition of "Create CONDRA", but with different fields. If you receive an error in the previous step, you must interrupt further execution of requests.

.. csv-table:: 
  :file: UpdateExtraFields.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

Server code 200 (ok).

