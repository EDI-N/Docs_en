######################
**Authorization**
######################

After service activation the user receives a login and password for authorization and can work with the API. 

.. csv-table:: 
  :file: Authorization.csv
  :widths:  10, 41
  :stub-columns: 0

**Request example:**

.. code:: none

  email=EDSsender&password=12345

**RESPONSE**

The **response body** (json-format) transfer the "session key" which is necessary for the further work. Further each request (method call) must contain HTTP header (Authorization), which for the correct execution of requests must contain a token "SID" with the value obtained during authorization. 

**Response example (JSON):**

.. code:: json

  {"SID": "65daca25-74ba-4c85-8183-71b404a348c0"}

.. hint::
  The duration of the session when the user is idle is 20 minutes (meaning that the key will be deleted in 20 minutes if the user is not active (will not send HTTP requests)).


