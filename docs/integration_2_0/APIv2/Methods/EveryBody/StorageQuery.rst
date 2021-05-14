#############################################################
**Data for filtering (StorageQuery object)**
#############################################################

**JSON:**

Get all incoming "Expense Invoices" in the status "Requires signing by the recipient" 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

	{
	  "statuses": [4, 5, 6],
	  "type": [
	    {
	      "type": 28
	    }
	  ],
	  "limit": {
	    "offset": "0",
	    "count": 21
	  },
	  "exchangeStatus": [
	    1
	  ],
	  "extraParams": [
	    {
	      "operator": "AND",
	      "type": "EQUALS",
	      "value": "6",
	      "fieldName": "sub_doc_type_id"
	    },
	    {
	      "operator": "AND",
	      "type": "EQUALS",
	      "value": "1",
	      "fieldName": "sub_status_id"
	    }
	  ],
	  "tags": [],
	  "archive": false,
	  "direction": {
	    "type": "EQ",
	    "receiver": [
	      "9864066822430"
	    ],
	    "sender": []
	  },
	  "family": 1
	}

Get all documents except drafts ("statuses" array does not contain "1"), in which the recipient is GLN 9864232304302 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

    {
        "direction": {
            "sender": [],
            "receiver": ["9864232304302"],
            "type": "EQ"
        },
        "exchangeStatus": [],
        "family": "1",
        "statuses": ["2","3","4","5","6","7"],
        "type": [
            {
                "type": "0"
            }
        ]
    }

Get all documents except drafts ("statuses" array does not contain "1"), in which the sender is GLN 9864232304302 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

    {
        "direction": {
            "sender": ["9864232304302"],
            "receiver": [],
            "type": "EQ"
        },
        "exchangeStatus": [],
        "family": "1",
        "statuses": ["2","3","4","5","6","7"],
        "type": [
            {
                "type": "0"
            }
        ]
    }

Get all incoming documents (recipient's GLN 9864232304302)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

    {
        "direction": {
            "sender": [],
            "receiver": ["9864232304302"],
            "type": "EQ"
        },
        "exchangeStatus": [],
        "family": "1",
        "statuses": ["4","5","6"],
        "type": [
            {
                "type": "0"
            }
        ]
    }

Get all sent documents (GLN of sender 9864232304302) 
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

    {
        "direction": {
            "sender": ["9864232304302"],
            "receiver": [],
            "type": "EQ"
        },
        "exchangeStatus": [],
        "family": "1",
        "statuses": ["2","3","6"],
        "type": [
            {
                "type": "0"
            }
        ]
    }

Get all documents numbered "1001" (search among all documents except drafts) in which the recipient is GLN 9864232304302
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

    {
        "direction": {
            "sender": [],
            "receiver": ["9864232304302"],
            "type": "EQ"
        },
        "exchangeStatus": [],
        "family": "1",
        "statuses": ["2","3","4","5","6","7"],
        "number": "1001",
        "type": [
            {
                "type": "0"
            }
        ]
    }

Get all documents except drafts for sender GLN 9864232304302, created in May 2019 (startTimestamp and finishTimestamp dates in UNIX-timestamp format according to Kyiv time relative to UTC) 
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code:: json

    {
        "direction": {
            "sender": ["9864232304302"],
            "receiver": [],
            "type": "EQ"
        },
        "exchangeStatus": [],
        "family": "1",
        "statuses": ["2","3","4","5","6","7"],
        "type": [
            {
                "type": "0"
            }
        ],
        "docDate": {
            "startTimestamp": "1556668800",
            "finishTimestamp": "1559347199"
        }
    }

.. _Таблиця_2:

Table 2 - Parameters description of object **StorageQuery**

.. csv-table:: 
  :file: for_csv/StorageQuery.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 3 - Parameters description of object **ExtraQueryParameters**

.. csv-table:: 
  :file: for_csv/ExtraQueryParameters.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 4 - Parameters description of object **Direction**

.. csv-table:: 
  :file: for_csv/Direction.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 5 - Parameters description of object **Limitation**

.. csv-table:: 
  :file: for_csv/Limitation.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 6 - Parameters description of object **DateTimeRange**

.. csv-table:: 
  :file: for_csv/DateTimeRange.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 7 - Parameters description of object **XDocType**

.. csv-table:: 
  :file: for_csv/XDocType.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

.. _fieldName:

Table 8 - **fieldName** description (object ExtraQueryParameters_)

.. csv-table:: 
  :file: for_csv/extra_fields.csv
  :widths:  1, 2, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

.. _param-desc:

Table 9 - **DocType** description (object XDocType_)

.. csv-table:: 
  :file: for_csv/xdoctype_p.csv
  :widths:  1, 19, 41
  :header-rows: 1
  :stub-columns: 0

.. _опис_підтипів:

Table 10 - COMDOC subtypes description

.. csv-table:: 
  :file: for_csv/sub_doc_type_id.csv
  :widths:  1, 7
  :header-rows: 1
  :stub-columns: 0