#####################################################################################################
**Details of the "Order" (ORDER) document creation result (Response)**
#####################################################################################################

Successful request fulfillment:

**JSON:**

.. code:: json

	{
	    "status": "OK",
	    "doc_uuid": "80928188-e10b-4f99-9db9-604addb77264",
	    "errors": []
	}

Table 1 - Description of parameters

.. csv-table:: 
  :file: for_csv/DistribexOrderResult.csv
  :widths:  1, 12, 41
  :header-rows: 1
  :stub-columns: 0

Examples of response with errors in "Order" formation:

**JSON:**

.. code:: json

	1. {
	    "status": "ERROR",
	    "errors": [
	        "The ordered quantity exceeds the established quota [1]"
	    ]
	}

	2. {
	    "status": "ERROR",
	    "errors": [
	        "The ordered quantity exceeds the available balance [1]"
	    ]
	}

	3. {
	    "status": "ERROR",
	    "errors": [
	        "The order amount is less than the minimum amount"
	    ]
	}

	4. {
	    "status": "ERROR",
	    "errors": [
	        "Order amount exceeds the maximum amount"
	    ]
	}

	5. {
	    "status": "ERROR",
	    "errors": [
	        "Maximum order weight exceeded"
	    ]
	}

	6. {
	    "status": "ERROR",
	    "errors": [
	        "Exceeded the maximum number of items in the order"
	    ]
	}

	7. {
	    "status": "ERROR",
	    "errors": [
	        "Maximum number of boxes per order exceeded"
	    ]
	}

	8. {
	    "status": "ERROR",
	    "errors": [
	        "The maximum number of pallets in the order has been exceeded"
	    ]
	}

	9. {
	    "status": "ERROR",
	    "errors": [
	        "The ordered quantity is not a multiple of the package [1]"
	    ]
	}

	------------------------------


	{
	    "status": "ERROR",
	    "errors": [
	        "The ordered quantity exceeds the established quota [1]",
	        "The ordered quantity exceeds the available balance [1]",
	        "The order amount is less than the minimum amount",
	        "Order amount exceeds the maximum amount",
	        "Maximum order weight exceeded",
	        "Exceeded the maximum number of items in the order",
	        "Maximum number of boxes per order exceeded",
	        "The maximum number of pallets in the order has been exceeded",
	        "The ordered quantity is not a multiple of the package [1]"
	    ]
	}

