#########################################################################
**Counterparty search parameters (EDistribexPriceQuery object)**
#########################################################################

.. note::
   For the key: "Region or country of availability of goods" the search works only by full match (by the full name of the region or country), and for the keys: "Company name", "Product category" the search works by both full and partial match.

**JSON:**

.. code:: json

   {
      "producerName": "Сухаренко",
      "categoryName": "Чай",
      "regions": [
         "Одеська",
         "Полтавська"
      ]
   }

Table 1 - Parameters description of object **EDistribexPriceQuery**

.. csv-table:: 
  :file: for_csv/EDistribexPriceQuery.csv
  :widths:  1, 12, 41
  :header-rows: 1
  :stub-columns: 0

Table 2 - Parameters description of object **Limitation**

.. csv-table:: 
  :file: ../../../API_ETTN/Methods/EveryBody/for_csv/Limitation.csv
  :widths:  1, 7, 12, 41
  :header-rows: 1
  :stub-columns: 0