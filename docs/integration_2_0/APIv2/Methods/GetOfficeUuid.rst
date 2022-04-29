.. deprecated (not for integrated users - web only) Ok, this is an exception for CONDRA (temporary) - delete when another api will be ready

#######################################################################################################
**Getting the UUID (for CONDRA)**
#######################################################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

Using **/api/office/uuid** GET method generate one UUID. To create a CONDRA, you must run the method twice.

.. csv-table:: 
  :file: GetOfficeUuid.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits **uuid** - generated a unique identifier in text form: 

.. code:: json

  c48f97e9-8d98-4c52-8635-675a6145f570