######################################################################
**Obtaining information on the authorized user**
######################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

Using the **api/oas/user** method it is possible to obtain user information such as user ID, account ID, login, does the user have "administrator rights" (true / false), platform information, and other identifiers. 

.. csv-table:: 
  :file: OasUser.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

User information is transmitted in the body of the **response** (object `User <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/EveryBody/User.html>`__).
