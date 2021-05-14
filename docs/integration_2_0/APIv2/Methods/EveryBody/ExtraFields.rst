#############################################################
**Additional fields**
#############################################################

**JSON:**

.. code:: json

	{
	  "extra_fields": {
	    "sender": "4820128010004",
	    "doc_num": "ORG00000014",
	    "buyer_uuid": "4820128010004",
	    "delivery_date": "1551477600",
	    "order_number": "6422722fb78c4509b06eac43758e1545",
	    "supplier_uuid": "9864065702429",
	    "contract_number": "334455",
	    "delivery_place_uuid": "4820128019007",
	    "order_date": "1550181600",
	    "doc_date": "1555432208",
	    "action": "29"
	  }
	}

Table 1 - Description of json parameters

+------------------------+-------------------------------+--------------------------------------------------------------------+
|     **Parameter**      |          **Format**           |                          **Description**                           |
+========================+===============================+====================================================================+
| **extra_fields**       | **Map<String, String>**       | array of objects; set of indexes                                   |
+------------------------+-------------------------------+--------------------------------------------------------------------+
| **multi_extra_fields** | **Map<String, List<String>>** | array of objects; multiindex. Can be used to index string elements |
+------------------------+-------------------------------+--------------------------------------------------------------------+

Table 2 - **extra_fields** description

.. csv-table:: 
  :file: for_csv/extra_fields.csv
  :widths:  1, 2, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

