#############################################################
**Directory of units of measurement (array of objects)**
#############################################################

**JSON:**

.. code:: json

	[
	  {
	    "id": 1,
	    "name": "GRM",
	    "nameOKEI": "Грамм",
	    "shortNameOKEI": "г",
	    "OKEI": "163",
	    "KSPOVO": "0303"
	  },
	  {
	    "id": 2,
	    "name": "KGM",
	    "nameOKEI": "Килограмм",
	    "shortNameOKEI": "кг",
	    "OKEI": "166",
	    "KSPOVO": "0301"
	  },
	  {
	    "id": 3,
	    "name": "LTR",
	    "nameOKEI": "Литр",
	    "shortNameOKEI": "л",
	    "OKEI": "112",
	    "KSPOVO": "0138"
	  },
	  ...
	  {
	    "id": 45,
	    "name": "OD",
	    "nameOKEI": "Единица (продукции)",
	    "shortNameOKEI": "од",
	    "KSPOVO": "2431"
	  }
	]

Table 1 - Description of response parameters (json)

+---------------+------------+---------------------------------------------+
| **Parameter** | **Format** |               **Description**               |
+===============+============+=============================================+
| id            | long       | unit identifier                             |
+---------------+------------+---------------------------------------------+
| name          | String     | name                                        |
+---------------+------------+---------------------------------------------+
| nameOKEI      | String     | name according to the state classifier      |
+---------------+------------+---------------------------------------------+
| shortNameOKEI | String     | reduction according to the state classifier |
+---------------+------------+---------------------------------------------+
| OKEI          | String     | state classifier code                       |
+---------------+------------+---------------------------------------------+
| KSPOVO        | String     | CSDUMA code                                 |
+---------------+------------+---------------------------------------------+
