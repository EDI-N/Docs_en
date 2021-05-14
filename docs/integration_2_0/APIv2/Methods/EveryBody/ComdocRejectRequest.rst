#############################################################
**Data for the reject operation**
#############################################################

**JSON:**

.. code:: json

  {
    "signInfo": {
      "certData": [
        {
          "EDRPOUCode": "",
          "isTimeStamp": true,
          "ownerName": "ЕДІН Тест ФОП",
          "serial": "1A15A67BC8E82F4C040000003AFA04000F890B00",
          "signDate": "08.08.2019 13:46 ",
          "subjOrg": "ЕДІН Тест ФОП",
          "subjTitle": "ЕДІН Тест ФОП"
        }
      ],
      "count": 1,
      "date": null,
      "hash": "3BC3AF062BCC00D51EC20EEDF6D4D7A7"
    },
    "signs": [
      {
        "sign": "MIIX0Q...Q5/XCjmk1pXR8mrASIx3U1zV0=",
        "type": 1
      }
    ]
  }

Table 1 - Description of json parameters

+---------------+------------------------+-------------------+--------------------------------------+
| **Parameter** | **Mandatory/Optional** |    **Format**     |           **Description**            |
+===============+========================+===================+======================================+
| signs         | M                      | ArrayList<Signs_> | Array of objects; signatures         |
+---------------+------------------------+-------------------+--------------------------------------+
| signInfo      | M                      | SignInfo_         | Object; information about signatures |
+---------------+------------------------+-------------------+--------------------------------------+

Table 2 - Parameters description of object **Signs**

.. csv-table:: 
  :file: for_csv/Signs.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 3 - Parameters description of object **SignInfo**

.. csv-table:: 
  :file: for_csv/SignInfo.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0

