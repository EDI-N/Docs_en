#######################################################################################################
**Download «Unstructured (Universal) Document» (CONDRA) as an archive**
#######################################################################################################

To work with this method, the user must be `authorized <https://wiki.edin.ua/en/latest/integration_2_0/APIv2/Methods/Authorization.html>`__.

.. csv-table:: 
  :file: GetCondraFile.csv
  :widths:  10, 41
  :stub-columns: 0

**RESPONSE**

**Response** transmits archive (.zip) which containing the body of the document CONDRA (.xml), the body of the signature (.p7s) and the signature letter (.pdf).

.. note::
    If the **file_type** parameter specifies a value other than **zip** or the parameter was not transmitted in the request, then only the body of the CONDRA document with the file name passed to **file_name** will be downloaded. 