Tables test
################################################################################

.. contents:: Contents:
   :depth: 3

-------------------------------------

.. raw:: html

    <embed>
    <iframe src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTRUek19RSIDfO8n6iMPbTw4HwDaI_eimm3Fpdr7DuQgw6iuzW4LlZ6f5ixEH98Ew/pubhtml?gid=1934956634&amp;single=true&amp;widget=true&amp;headers=false" width="1100" height="900" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe>
    </embed>

.. hmm comment

    1
                Посилання на приклад XML						
    2
                Посилання на друковану форму (з тегами)						
    3
                Посилання на друковану форму (шаблон)						
    4
                ТОВАРНО-ТРАНСПОРТНА НАКЛАДНА						UN/CEFACT
    5
        № з/п		Назва тегу Uncefact	Тип даних	Значення тегу	Обмеження	Обов'язковість	Зміст тегу (як заповнювати)	Посилання на документацію UN/CEFACT
                                        
    6
        I		eCMR						MMT CCBDA e-CMR Message Structure
    7
        1		ExchangedDocumentContext		Технічні дані		mandatory		BSP Master. Exchanged Document_ Context
    8
        1.1		ExchangedDocumentContext.SpecifiedTransactionID	string	версія документа		mandatory	Номер версії документа (транзакції) в ланцюгу підписання документів	Exchanged Document_ Context. Specified_ Transaction. Identifier
    9
        1.2		ExchangedDocumentContext.BusinessProcessSpecifiedDocumentContextParameter.ID	string	код документа		mandatory		Exchanged Document_ Context. Business Process_ Specified. Document Context_ Parameter
    10
        1.3		ExchangedDocumentContext.GuidelineSpecifiedDocumentContextParameter.ID	unsignedByte	підтип документа	001 - generic (default)	mandatory	Тип е-ТТН залежно від виду вантажу:
    - основний	Exchanged Document_ Context. Guideline_ Specified. Document Context_ Parameter
    11
        2		ExchangedDocument		Реквізити ТТН		mandatory		BSP Master. Exchanged_ Document
    12
        2.1		ExchangedDocument. ID	string	Номер документа		mandatory	порядковий номер (серія) ТТН	Exchanged_ Document. Identification. Identifier
    13
        2.2		ExchangedDocument.IssueDateTime	datetime	Дата і час складання документа	yyyy:mm:dd hh:mm:ss	mandatory	дату виписування ТТН	Exchanged_ Document. Issue. Date Time
    14
        2.3		ExchangedDocument.IssueLogisticsLocation.Name + ExchangedDocument.IssueLogisticsLocation.Description	string	Місце складання		mandatory	найменування та опис (адреса) місця складання ТТН	Logistics_ Location. Name. Text + Logistics_ Location. Description.Text
    15
        3		SpecifiedSupplyChainConsignment		Інформація про перевезення		mandatory		BSP Master. Specified. Supply Chain_ Consignment
    16
        3.1		GrossWeightMeasure	decimal	Маса брутто, кг	0,1	mandatory	загальна вага перевезення в кг з точністю до 0,1	Supply Chain_ Consignment. Gross Weight. Measure
    17
        3.2		AssociatedInvoiceAmount	decimal	Усього відпущено на загальну суму, грн	0,01	mandatory	загальна вартість відвантажених товарів з урахуванням ПДВ та акцизного збору (якщо останній сплачується)	Supply Chain_ Consignment. Associated Invoice. Amount
    18
        3.3		ConsignmentItemQuantity	decimal	Кількість місць		mandatory	вказується загальна кількість місць вантажу (контейнерів)	Supply Chain_ Consignment. Consignment Item. Quantity
    19
        3.5		DeliveryInstructions (код TRANSPORTATION_TYPE)		Вид перевезень		optional		Supply Chain_ Consignment. Delivery. Delivery_ Instructions
    20
        3.5.1		DeliveryInstructions.Description	string	Опис		mandatory	вид роботи перевізника: за відрядним тарифом, за погодинним тарифом, за покілометровим тарифом, централізовані перевезення тощо	Delivery_ Instructions. Description. Text
    21
        3.5.2		DeliveryInstructions.DescriptionCode	string	Код	TRANSPORTATION_TYPE	mandatory		Delivery_ Instructions. Description. Code
    22
        3.6		ConsignorTradeParty		Вантажовідправник		mandatory		Supply Chain_ Consignment. Consignor. Trade_ Party
    23
        3.6.1		ConsignorTradeParty. ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Вантажовідправник	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ідентифікаційний код підприємства (ЄДРПОУ юридичної особи або РНОКПП фізичної-особи підприємця), що проводить відвантаження (списання) перелічених в ТТН товарно-матеріальних цінностей	Trade_ Party. Identification. Identifier
    24
        3.6.2		ConsignorTradeParty.Name	string	Повне найменування Вантажовідправник		mandatory	найменування підприємства (юридичної особи або ПІБ фізичної-особи підприємця), що проводить відвантаження (списання) перелічених в ТТН товарно-матеріальних цінностей	Trade_ Party. Name. Text
    25
        3.6.3		ConsignorTradeParty.RoleCode	string	Роль учасника	вантажовідправник CZ	mandatory	довідник ролей	Trade_ Party. Role. Code
    26
        3.6.4		ConsignorTradeParty.PostalTradeAddress		Юридична адреса Вантажовідправник		mandatory	юридична адреса юридичної особи або адреса реєстрації фізичної особи-підприємця	Trade_ Party. Postal. Trade_ Address
    27
        3.6.4.1		ConsignorTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    28
        3.6.4.2		ConsignorTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    29
        3.6.4.3		ConsignorTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    30
        3.6.4.4		ConsignorTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    31
        3.6.4.5		ConsignorTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    32
        3.6.5		ConsignorTradeParty.DefinedTradeContact		Контактні/відповідальні особи Вантажовідправник		optional		Trade_ Party. Defined. Trade_ Contact
    33
        3.6.5.1		ConsignorTradeParty.DefinedTradeContact.PersonName	string	ПІБ		optional		Trade_ Contact. Person Name. Text
    34
        3.6.5.2		ConsignorTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    35
        3.6.5.3		ConsignorTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    36
        3.6.5.4		ConsignorTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    37
        3.6.6		ConsignorTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код в.о.		optional	РНОКПП відповідальної особи за необхідності	Trade_ Party. Specified. Tax_ Registration
    38
        3.7		ConsigneeTradeParty		Вантажоодержувач		mandatory		Supply Chain_ Consignment. Consignee. Trade_ Party
    39
        3.7.1		ConsigneeTradeParty. ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Вантажоодержувач	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ідентифікаційний код підприємства (ЄДРПОУ юридичної особи або РНОКПП фізичної-особи підприємця), що проводить одержання (оприбуткування) перелічених в ТТН товарно-матеріальних цінностей	Trade_ Party. Identification. Identifier
    40
        3.7.2		ConsigneeTradeParty.Name	string	Повне найменування Вантажоодержувач		mandatory	найменування підприємства (юридичної особи або ПІБ фізичної-особи підприємця), що проводить одержання (оприбуткування) перелічених в ТТН товарно-матеріальних цінностей	Trade_ Party. Name. Text
    41
        3.7.3		ConsigneeTradeParty.RoleCode	string	Роль учасника	вантажоодержувач CN	mandatory	довідник ролей	Trade_ Party. Role. Code
    42
        3.7.4		ConsigneeTradeParty.PostalTradeAddress		Юридична адреса Вантажоодержувач		mandatory	юридична адреса юридичної особи або адреса реєстрації фізичної особи-підприємця	Trade_ Party. Postal. Trade_ Address
    43
        3.7.4.1		ConsigneeTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    44
        3.7.4.2		ConsigneeTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    45
        3.7.4.3		ConsigneeTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    46
        3.7.4.4		ConsigneeTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    47
        3.7.4.5		ConsigneeTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    48
        3.7.5		ConsigneeTradeParty.DefinedTradeContact		Контактні/відповідальні особи Вантажоодержувач		optional		Trade_ Party. Defined. Trade_ Contact
    49
        3.7.5.1		ConsigneeTradeParty.DefinedTradeContact.PersonName	string	ПІБ		optional		Trade_ Contact. Person Name. Text
    50
        3.7.5.2		ConsigneeTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    51
        3.7.5.3		ConsigneeTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    52
        3.7.5.4		ConsigneeTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    53
        3.7.6		ConsigneeTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код в.о.		optional	РНОКПП відповідальної особи за необхідності	Trade_ Party. Specified. Tax_ Registration
    54
        3.8		CarrierTradeParty		Перевізник		mandatory		Supply Chain_ Consignment. Carrier. Trade_ Party
    55
        3.8.1		CarrierTradeParty. ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Перевізник	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ЄДРПОУ суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або РНОКПП фізичної особи, з яким вантажовідправник уклав договір на надання транспортних послуг	Trade_ Party. Identification. Identifier
    56
        3.8.2		CarrierTradeParty.Name	string	Повне найменування Перевізник		mandatory	найменування суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або прізвище, ім’я, по батькові фізичної особи, з яким вантажовідправник уклав договір на надання транспортних послуг	Trade_ Party. Name. Text
    57
        3.8.3		CarrierTradeParty.RoleCode	string	Роль учасника	перевізник CA	mandatory	довідник ролей	Trade_ Party. Role. Code
    58
        3.8.4		CarrierTradeParty.PostalTradeAddress	string	Юридична адреса Перевізник		mandatory	юридична адреса суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або адреса реєстрації фізичної особи, з яким вантажовідправник уклав договір на надання транспортних послуг	Trade_ Party. Postal. Trade_ Address
    59
        3.8.4.1		CarrierTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    60
        3.8.4.2		CarrierTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    61
        3.8.4.3		CarrierTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    62
        3.8.4.4		CarrierTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    63
        3.8.4.5		CarrierTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    64
        3.8.5		CarrierTradeParty.DefinedTradeContact		Контактні/відповідальні особи Перевізник		mandatory		Trade_ Party. Defined. Trade_ Contact
    65
        3.8.5.1		CarrierTradeParty.DefinedTradeContact.PersonName	string	ПІБ Водій		mandatory	ПІБ водія, що керуватиме ТЗ при перевезенні вантажу	Trade_ Contact. Person Name. Text
    66
        3.8.5.2		CarrierTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    67
        3.8.5.3		CarrierTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    68
        3.8.5.4		CarrierTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    69
        3.8.6		CarrierTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код Водій	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	РНКОПП водія	Trade_ Party. Specified. Tax_ Registration
    70
        3.8.7		CarrierTradeParty.SpecifiedGovernmentRegistration.ID	string	Номер посвідчення Водій	1. лише кирилиця
    2. має відповідати одному з патернів водійського посвідчення
    (новий формат: три літери + шість цифр)	mandatory	серія та номер водійського посвідчення водія	Trade_ Party. Specified. Government_ Registration (Government_ Registration. Identification. Identifier)
    71
        3.9		NotifiedTradeParty (роль - FW)		Експедитор		optional		Supply Chain_ Consignment. Notified. Trade_ Party
    72
        3.9.1		NotifiedTradeParty.ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Експедитор	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ЄДРПОУ суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або РНОКПП фізичної особи, з яким вантажовідправник (замовник) уклав договір траспортного експедирування	Trade_ Party. Identification. Identifier
    73
        3.9.2		NotifiedTradeParty.Name	string	Повне найменування Експедитор		mandatory	найменування суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або прізвище, ім’я, по батькові фізичної особи, з яким вантажовідправник (замовник) уклав договір траспортного експедирування	Trade_ Party. Name. Text
    74
        3.9.3		NotifiedTradeParty.RoleCode	string	Роль учасника	експедитор FW	mandatory	довідник ролей	Trade_ Party. Role. Code
    75
        3.9.4		NotifiedTradeParty.PostalTradeAddress	string	Юридична адреса Експедитор		optional	юридична адреса суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або адреса реєстрації фізичної особи, з яким вантажовідправник (замовник) уклав договір траспортного експедирування	Trade_ Party. Postal. Trade_ Address
    76
        3.9.4.1		NotifiedTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    77
        3.9.4.2		NotifiedTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    78
        3.9.4.3		NotifiedTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    79
        3.9.4.4		NotifiedTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    80
        3.9.4.5		NotifiedTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    81
        3.9.5		NotifiedTradeParty.DefinedTradeContact		Контактні/відповідальні особи Експедитор		optional		Trade_ Party. Defined. Trade_ Contact
    82
        3.9.5.1		NotifiedTradeParty.DefinedTradeContact.PersonName	string	ПІБ		optional		Trade_ Contact. Person Name. Text
    83
        3.9.5.2		NotifiedTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    84
        3.9.5.3		NotifiedTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    85
        3.9.5.4		NotifiedTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    86
        3.9.6		NotifiedTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код в.о.		optional	РНОКПП відповідальної особи за необхідності	Trade_ Party. Specified. Tax_ Registration
    87
        3.10		NotifiedTradeParty (роль - OB)		Замовник		mandatory		Supply Chain_ Consignment. Notified. Trade_ Party
    88
        3.10.1		NotifiedTradeParty.ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Замовник	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ЄДРПОУ суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або РНОКПП фізичної особи, що проводить оплату транспортної роботи і послуг	Trade_ Party. Identification. Identifier
    89
        3.10.2		NotifiedTradeParty.Name	string	Найменування Замовник		mandatory	найменування суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або прізвище, ім’я, по батькові фізичної особи, що проводить оплату транспортної роботи і послуг	Trade_ Party. Name. Text
    90
        3.10.3		NotifiedTradeParty.RoleCode	string	Роль учасника	замовник OB	mandatory	довідник ролей	Trade_ Party. Role. Code
    91
        3.10.4		NotifiedTradeParty.PostalTradeAddress		Юридична адреса Замовник		mandatory	юридична адреса суб’єкта господарювання (юридичної особи або фізичної особи - підприємця) або адреса реєстрації фізичної особи, що проводить оплату транспортної роботи і послуг	Trade_ Party. Postal. Trade_ Address
    92
        3.10.4.1		NotifiedTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    93
        3.10.4.2		NotifiedTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    94
        3.10.4.3		NotifiedTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    95
        3.10.4.4		NotifiedTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    96
        3.10.4.5		NotifiedTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    97
        3.10.5		NotifiedTradeParty.DefinedTradeContact		Контактні/відповідальні особи Замовник		optional		Trade_ Party. Defined. Trade_ Contact
    98
        3.10.5.1		NotifiedTradeParty.DefinedTradeContact.PersonName	string	ПІБ		optional		Trade_ Contact. Person Name. Text
    99
        3.10.5.2		NotifiedTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    100
        3.10.5.3		NotifiedTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    101
        3.10.5.4		NotifiedTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    102
        3.10.6		NotifiedTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код в.о.		optional	РНОКПП відповідальної особи за необхідності	Trade_ Party. Specified. Tax_ Registration
    103
        3.11		NotifiedTradeParty (роль - WD)		Проміжний склад		optional	Опційний блок.
    Більш детальна інформація про проміжні перевантаження, якщо вона є, надається Перевізником у блоці "Маршрутизація"	Supply Chain_ Consignment. Notified. Trade_ Party
    104
        3.11.1		NotifiedTradeParty.ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Проміжний склад	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ЄДРПОУ підприємства (Вантажовідправник/Перевізник/Експедитор/Вантажоодержувач/Товарний склад), що приймає від Перевізника на тимчасове зберігання вантаж 	Trade_ Party. Identification. Identifier
    105
        3.11.2		NotifiedTradeParty.Name	string	Повне найменування Проміжний склад		mandatory	Повне найменування підприємства (Вантажовідправник/Перевізник/Експедитор/Вантажоодержувач/Товарний склад), що приймає від Перевізника на тимчасове зберігання вантаж 	Trade_ Party. Name. Text
    106
        3.11.3		NotifiedTradeParty.RoleCode	string	Роль учасника	проміжний склад WD	mandatory	довідник ролей	Trade_ Party. Role. Code
    107
        3.11.4		NotifiedTradeParty.PostalTradeAddress		Юридична адреса Проміжний склад		optional	Юридична адреса підприємства (Вантажовідправник/Перевізник/Експедитор/Вантажоодержувач/Товарний склад), що приймає від Перевізника на тимчасове зберігання вантаж 	Trade_ Party. Postal. Trade_ Address
    108
        3.11.4.1		NotifiedTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    109
        3.11.4.2		NotifiedTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    110
        3.11.4.3		NotifiedTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    111
        3.11.4.4		NotifiedTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    112
        3.11.4.5		NotifiedTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    113
        3.11.5		NotifiedTradeParty.DefinedTradeContact		Контактні/відповідальні особи Проміжний склад		optional		Trade_ Party. Defined. Trade_ Contact
    114
        3.11.5.1		NotifiedTradeParty.DefinedTradeContact.PersonName	string	ПІБ		optional		Trade_ Contact. Person Name. Text
    115
        3.11.5.2		NotifiedTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    116
        3.11.5.3		NotifiedTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    117
        3.11.5.4		NotifiedTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    118
        3.11.6		NotifiedTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код в.о.		optional	РНОКПП відповідальної особи за необхідності	Trade_ Party. Specified. Tax_ Registration
    119
        3.12		NotifiedTradeParty (роль - COP)		Компанія, що надає охоронні послуги		optional		Supply Chain_ Consignment. Notified. Trade_ Party
    120
        3.12.1		NotifiedTradeParty.ID (schemeAgencyID="ЄДРПОУ")	string	Ідентифікаційний код Охоронна компанія	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ЄДРПОУ підприємства, що надає охоронні послуги вантажу під час перевезення 	Trade_ Party. Identification. Identifier
    121
        3.12.2		NotifiedTradeParty.Name	string	Повне найменування Охоронна компанія		mandatory	Повне найменування підприємства, що надає охоронні послуги вантажу під час перевезення	Trade_ Party. Name. Text
    122
        3.12.3		NotifiedTradeParty.RoleCode	string	Роль учасника	охоронна фірма COP	mandatory	довідник ролей	Trade_ Party. Role. Code
    123
        3.12.4		NotifiedTradeParty.DefinedTradeContact.PersonName	string	ПІБ відп. особи		optional	ПІБ представника Замовника, який уповноважений супроводжувати вантаж, що підлягає спеціальній охороні	Trade_ Contact. Person Name. Text
    124
        3.13		CarrierAcceptanceLogisticsLocation		Пункт навантаження		mandatory		Supply Chain_ Consignment. Carrier Acceptance. Logistics_ Location
    125
        3.13.1		CarrierAcceptanceLogisticsLocation.ID (schemeAgencyID="КАТОТТГ")	string	Код КАТОТТГ пункту навантаження	валідація за кодифікатором	mandatory	код пункту навантаження відповідно до Кодифікатора адміністративно-територіальних одиниць та територій територіальних громад	Logistics_ Location. Identification. Identifier
    126
        3.13.2		CarrierAcceptanceLogisticsLocation.TypeCode	string	Тип операції	5	mandatory	5 - навантаження
    10 - розвантаження	Logistics_ Location. Type. Code
    127
        3.13.3		CarrierAcceptanceLogisticsLocation.Name + CarrierAcceptanceLogisticsLocation.Description	string	Місцезнаходження пункту навантаження		mandatory	Найменування та опис (адреса) пункту навантаження	Logistics_ Location. Name. Text + Logistics_ Location. Description. Text
    128
        3.13.4		CarrierAcceptanceLogisticsLocation. PhysicalGeographicalCoordinate. LatitudeMeasure +
    CarrierAcceptanceLogisticsLocation. PhysicalGeographicalCoordinate. LongitudeMeasure	string	Географічні координати		optional	широта та довгота	Logistics_ Location. Physical. Geographical Coordinate
    129
        3.14		ConsigneeReceiptLogisticsLocation		Пункт розвантаження		mandatory		Supply Chain_ Consignment. Consignee Receipt. Logistics_ Location
    130
        3.14.1		ConsigneeReceiptLogisticsLocation. ID (schemeAgencyID="КАТОТТГ")	string	Код КАТОТТГ пункту розвантаження	валідація за кодифікатором	mandatory	код пункту розвантаження відповідно до Кодифікатора адміністративно-територіальних одиниць та територій територіальних громад	Logistics_ Location. Identification. Identifier
    131
        3.14.2		ConsigneeAcceptanceLogisticsLocation.TypeCode	string	Тип операції	10	mandatory	5 - навантаження
    10 - розвантаження	Logistics_ Location. Type. Code
    132
        3.14.3		ConsigneeReceiptLogisticsLocation.Name + ConsigneeReceiptLogisticsLocation.Description	string	Місцезнаходження пункту розвантаження		mandatory	Найменування та опис (адреса) пункту розвантаження	Logistics_ Location. Name. Text + Logistics_ Location. Description. Text
    133
        3.14.4		ConsigneeAcceptanceLogisticsLocation. PhysicalGeographicalCoordinate. LatitudeMeasure +
    ConsigneeAcceptanceLogisticsLocation. PhysicalGeographicalCoordinate. LongitudeMeasure	string	Географічні координати		optional	широта та довгота	Logistics_ Location. Physical. Geographical Coordinate
    134
        3.15		AssociatedReferencedDocument		Супровідні документи на вантаж		optional		Supply Chain_ Consignment. Associated. Referenced_ Document
    135
        3.15.1		AssociatedReferencedDocument (TypeCode=723)	string	Документ, що підтверджує охоронні послуги		optional		Supply Chain_ Consignment. Associated. Referenced_ Document
    136
        13.15.1.1		AssociatedReferencedDocument.TypeCode	string	Тип	723	mandatory	довідник кодів документів	Referenced_ Document. Type. Code
    137
        13.15.1.2		AssociatedReferencedDocument.ID + AssociatedReferencedDocument.Remarks	string	Назва та номер документа		mandatory	Документ, згідно з яким представник Замовника уповноважений супроводжувати вантаж, який підлягає спеціальній охороні	Referenced_ Document. Identification. Identifier + Referenced_ Document. Remarks. Text
    138
        13.15.1.3		AssociatedReferencedDocument.FormattedIssueDateTime	datetime	Дата складання документа	yyyy:mm:dd hh:mm:ss	optional		Referenced_ Document. Formatted_ Issue. Date Time
    139
        3.15.2		AssociatedReferencedDocument (TypeCode=290)		Запис про передачу права на пред'явлення претензії		optional		Supply Chain_ Consignment. Associated. Referenced_ Document
    140
        3.15.2.1		AssociatedReferencedDocument.TypeCode	string	Тип	290	mandatory	довідник кодів документів	Referenced_ Document. Type. Code
    141
        3.15.2.2		AssociatedReferencedDocument.Remarks	string	Право на пред'явлення претензії передане		mandatory	Передача права на пред'явлення претензії засвідчується написом на ТТН такого змісту: "Право на пред'явлення претензії передане П.І.Б. " (довірена особа)	Referenced_ Document. Remarks. Text
    142
        3.15.2.3		AssociatedReferencedDocument.FormattedIssueDateTime	datetime	Дата складання документа	yyyy:mm:dd hh:mm:ss	optional		Referenced_ Document. Formatted_ Issue. Date Time
    143
        3.15.3		AssociatedReferencedDocument (TypeCode=916)		Коригуючі акти		optional		Supply Chain_ Consignment. Associated. Referenced_ Document
    144
        3.15.3.1		AssociatedReferencedDocument.TypeCode	string	Тип	916	mandatory	довідник кодів документів	Referenced_ Document. Type. Code
    145
        3.15.3.2		AssociatedReferencedDocument.ID + AssociatedReferencedDocument.Remarks	string	Назва та номер акта		mandatory		Referenced_ Document. Identification. Identifier + Referenced_ Document. Remarks. Text
    146
        3.15.3.3		AssociatedReferencedDocument.FormattedIssueDateTime	datetime	Дата акта	yyyy:mm:dd hh:mm:ss	optional		Referenced_ Document. Formatted_ Issue. Date Time
    147
        3.15.4		AssociatedReferencedDocument		Інші супровідні документи		optional		Supply Chain_ Consignment. Associated. Referenced_ Document
    148
        3.15.4.1		AssociatedReferencedDocument.TypeCode	string	Тип	вибір значення із довідника	optional	довідник кодів документів якщо код не присвоєно цим довідником, його (код) можна не вказувати	Referenced_ Document. Type. Code
    149
        3.15.4.2		AssociatedReferencedDocument.ID + AssociatedReferencedDocument.Remarks	string	Назва та номер документа		mandatory		Referenced_ Document. Identification. Identifier + Referenced_ Document. Remarks. Text
    150
        3.15.4.3		AssociatedReferencedDocument.FormattedIssueDateTime	datetime	Дата документа	yyyy:mm:dd hh:mm:ss	optional		Referenced_ Document. Formatted_ Issue. Date Time
    151
        3.16		DeliveryTransportEvent		Розвантажувальні роботи		mandatory		Supply Chain_ Consignment. Delivery. Transport_ Event
    152
        3.16.1		DeliveryTransportEvent.ApplicableNote (з кодом GROSSWEIGHT)	decimal	Маса брутто, кг	0,1	optional	маса отриманого вантажу в місці розвантаження в кілограмах з точністю до 0,1	Transport_ Event. Applicable. Note
    153
        3.16.2		DeliveryTransportEvent.ActualOccurrenceDateTime	datetime	Дата і час прибуття	yyyy:mm:dd hh:mm:ss	optional	дата і час прибуття автомобіля на розвантаження	Transport_ Event. Actual_ Occurrence. Date Time
    154
        3.16.3		DeliveryTransportEvent.ScheduledOccurrenceDateTime	datetime	Дата і час відправлення	yyyy:mm:dd hh:mm:ss	optional	дата і час відправлення автомобіля з-під розвантаження	Transport_ Event. Scheduled_ Occurrence. Date Time
    155
        3.16.4		DeliveryTransportEvent.ApplicableNote (з кодом DOWNTIME)	unsignedByte	Час простою		optional	час (години) простою під розвантаженням	Transport_ Event. Applicable. Note
    156
        3.16.5		DeliveryTransportEvent.CertifyingTradeParty (RoleCode=CN)		
    Інформація про відповідальних осіб Вантажоодержувача
            mandatory		Transport_ Event. Certifying. Trade_ Party
    157
        3.16.5.1		DeliveryTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	посада матеріально відповідальної особи вантажоодержувача	Trade_ Party. Name. Text
    158
        3.16.5.2		DeliveryTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	вантажоодержувач CN	mandatory	роль - вантажоодержувач	Trade_ Party. Role. Code
    159
        3.16.5.3		DeliveryTransportEvent.CertifyingTradeParty.DefinedTradeContact.Person Name	string	П.І.Б.		mandatory	ПІБ матеріально відповідальної особи вантажоодержувача	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    160
        3.16.5.4		DeliveryTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП матеріально відповідальної особи вантажоодержувача	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    161
        3.16.6		DeliveryTransportEvent.CertifyingTradeParty (RoleCode=DR)		Інформація про водія Перевізника		mandatory		Transport_ Event. Certifying. Trade_ Party
    162
        3.16.6.1		DeliveryTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	посада водія, що здав вантаж	Trade_ Party. Name. Text
    163
        3.16.6.2		DeliveryTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	водій DR	mandatory	роль - водій	Trade_ Party. Role. Code
    164
        3.16.6.3		DeliveryTransportEvent.CertifyingTradeParty.DefinedTradeContact.PersonName	string	П.І.Б.		mandatory	ПІБ водія, що здав вантаж 	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    165
        3.16.6.4		DeliveryTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП водія	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    166
        3.16.7		DeliveryTransportEvent.CertifyingTradeParty (RoleCode=CA)		
    Інформація про відповідальних осіб Перевізника
            optional		Transport_ Event. Certifying. Trade_ Party
    167
        3.16.7.1		DeliveryTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	Посада відповідальної особи Перевізника	Trade_ Party. Name. Text
    168
        3.16.7.2		DeliveryTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	перевізник СА	mandatory	роль - перевізник	Trade_ Party. Role. Code
    169
        3.16.7.3		DeliveryTransportEvent.CertifyingTradeParty.DefinedTradeContact.Person Name	string	П.І.Б.		mandatory	П.І.Б. відповідальної особи Перевізника	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    170
        3.16.7.4		DeliveryTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП відповідальної особи Перевізника	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    171
        3.16.8		DeliveryTransportEvent.CertifyingTradeParty (RoleCode=FW)		
    Інформація про відповідальних осіб Експедитора
            optional		Transport_ Event. Certifying. Trade_ Party
    172
        3.16.8.1		DeliveryTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	посада відповідальної особи Експедитора	Trade_ Party. Name. Text
    173
        3.16.8.2		DeliveryTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	експедитор FW	mandatory	роль - експедитор	Trade_ Party. Role. Code
    174
        3.16.8.3		DeliveryTransportEvent.CertifyingTradeParty.DefinedTradeContact.Person Name	string	П.І.Б.		mandatory	ПІБ відповідальної особи Експедитора	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    175
        3.16.8.4		DeliveryTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП відповідальної особи Експедитора	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    176
        3.17		PickUpTransportEvent		Навантажувальні роботи		optional		Supply Chain_ Consignment. Pick-Up. Transport_ Event
    177
        3.17.1		PickUpTransportEvent.ApplicableNote (з кодом GROSSWEIGHT)	decimal	Маса брутто, кг	0,1	optional	маса зданого/отриманого для перевезення вантажу в кілограмах з точністю до 0,1	Transport_ Event. Applicable. Note
    178
        3.17.2		PickUpTransportEvent.ActualOccurrenceDateTime	datetime	Дата і час прибуття	yyyy:mm:dd hh:mm:ss	optional	дата і час прибуття автомобіля під навантаження	Transport_ Event. Actual_ Occurrence. Date Time
    179
        3.17.3		PickUpTransportEvent.ScheduledOccurrenceDateTime	datetime	Дата і час відправлення	yyyy:mm:dd hh:mm:ss	optional	дата і час відправлення автомобіля з-під навантаження	Transport_ Event. Scheduled_ Occurrence. Date Time
    180
        3.17.4		PickUpTransportEvent.ApplicableNote (з кодом DOWNTIME)	unsignedByte	Час простою	hh:mm:ss	optional	час простою під навантаженням	Transport_ Event. Applicable. Note
    181
        3.17.5		PickUpTransportEvent.CertifyingTradeParty (RoleCode=CZ)		
    Інформація про відповідальних осіб Вантажовідправника
            mandatory		Transport_ Event. Certifying. Trade_ Party
    182
        3.17.5.1		PickUpTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	посада матеріально відповідальної особи, яка відпускає вантаж	Trade_ Party. Name. Text
    183
        3.17.5.2		PickUpTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	вантажовідправник CZ	mandatory	роль - вантажовідправник	Trade_ Party. Role. Code
    184
        3.17.5.3		PickUpTransportEvent.CertifyingTradeParty.DefinedTradeContact.PersonName	string	П.І.Б.		mandatory	ПІБ матеріально відповідальної особи, яка відпускає вантаж	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    185
        3.17.5.4		PickUpTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП матеріально відповідальної особи, яка відпускає вантаж	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    186
        3.17.6		PickUpTransportEvent.CertifyingTradeParty (RoleCode=DR)		Інформація про водія Перевізника		mandatory		Transport_ Event. Certifying. Trade_ Party
    187
        3.17.6.1		PickUpTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	посада водія, що прийняв вантаж	Trade_ Party. Name. Text
    188
        3.17.6.2		PickUpTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	водій DR	mandatory	роль - водій	Trade_ Party. Role. Code
    189
        3.17.6.3		PickUpTransportEvent.CertifyingTradeParty.DefinedTradeContact.PersonName	string	П.І.Б.		mandatory	ПІБ водія, що прийняв вантаж 	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    190
        3.17.6.4		PickUpTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП водія	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    191
        3.17.7		PickUpTransportEvent.CertifyingTradeParty (RoleCode=CA)		
    Інформація про відповідальних осіб Перевізника
            optional		Transport_ Event. Certifying. Trade_ Party
    192
        3.17.7.1		PickUpTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	Посада відповідальної особи Перевізника	Trade_ Party. Name. Text
    193
        3.17.7.2		PickUpTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	перевізник СА	mandatory	роль - перевізник	Trade_ Party. Role. Code
    194
        3.17.7.3		PickUpTransportEvent.CertifyingTradeParty.DefinedTradeContact.PersonName	string	П.І.Б.		mandatory	П.І.Б. відповідальної особи Перевізника	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    195
        3.17.7.4		PickUpTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП відповідальної особи Перевізника	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    196
        3.17.8		PickUpTransportEvent.CertifyingTradeParty (RoleCode=FW)		
    Інформація про відповідальних осіб Експедитора
            optional		Transport_ Event. Certifying. Trade_ Party
    197
        3.17.8.1		PickUpTransportEvent.CertifyingTradeParty.Name	string	Посада		mandatory	посада відповідальної особи Експедитора	Trade_ Party. Name. Text
    198
        3.17.8.2		PickUpTransportEvent.CertifyingTradeParty.RoleCode	string	Роль	експедитор FW	mandatory	роль - експедитор	Trade_ Party. Role. Code
    199
        3.17.8.3		PickUpTransportEvent.CertifyingTradeParty.DefinedTradeContact.PersonName	string	П.І.Б.		mandatory	ПІБ відповідальної особи Експедитора	Trade_ Party. Defined. Trade_ Contact (Trade_ Contact. Person Name. Text)
    200
        3.17.8.4		PickUpTransportEvent.CertifyingTradeParty.ID (schemeAgencyID="РНОКПП")	string	Ідентифікаційний код		optional	РНОКПП відповідальної особи Експедитора	Trade_ Party. Identification. Identifier (Identification Scheme Agency. Identifier)
    201
        3.18		IncludedSupplyChainConsignmentItem		Відомості про вантаж		mandatory		Supply Chain_ Consignment. Included. Supply Chain_ Consignment Item
    202
        3.18.1		IncludedSupplyChainConsignmentItem.SequenceNumeric	int	Порядковий номер		mandatory	порядковий номер рядка в таблиці	Supply Chain_ Consignment Item. Sequence. Numeric
    203
        3.18.2		IncludedSupplyChainConsignmentItem.InvoiceAmount	decimal	Загальна сума з ПДВ, грн	0,01	mandatory	загальна сума товару з ПДВ	Supply Chain_ Consignment Item. Invoice. Amount
    204
        3.18.3		IncludedSupplyChainConsignmentItem.GrossWeightMeasure	decimal	Маса брутто, кг	0,1	mandatory	маса вантажу по кожному рядку з точністю до 0,1	Supply Chain_ Consignment Item. Gross Weight. Measure
    205
        3.18.4		IncludedSupplyChainConsignmentItem.TariffQuantity	decimal	Ціна без ПДВ за одиницю, грн	0,01	optional	ціна товару без ПДВ (це можуть бути як гривні на кілограм (грн./кг), так і гривні на ящик (грн./ящик)) - залежить від зазначеної одиниці виміру	Supply Chain_ Consignment Item. Tariff. Quantity
    206
        3.18.5		IncludedSupplyChainConsignmentItem.GlobalID (schemeAgencyID="УКТЗЕД")	string	Код УКТЗЕД продукції	валідація за кодифікатором	optional	Код УКТЗЕД продукції	Supply Chain_ Consignment Item. Global_ Identification. Identifier
    207
        3.18.6		IncludedSupplyChainConsignmentItem.NatureIdentificationTransportCargo. Identification	string	Найменування вантажу		mandatory	Найменування вантажу	Supply Chain_ Consignment Item. Nature Identification. Transport_ Cargo
    208
        3.18.7		IncludedSupplyChainConsignmentItem.ApplicableTransportDangerousGoods.UNDGIdentificationCode	decimal	Клас небезпечних речовин		optional	у разі перевезення небезпечних вантажів: клас небезпечних речовин, до якого віднесено вантаж	Supply Chain_ Consignment Item. Applicable. Transport_ Dangerous Goods (Transport_ Dangerous Goods. UNDG Identification. Code)
    209
        3.18.8		IncludedSupplyChainConsignmentItem.AssociatedReferencedLogisticsTransportEquipment. ID	string	Номер контейнера		optional	Відсилка до номеру контейнера, в якому завантажено цей вантаж.
    Використовуєься опційно для контейнерих перевезень і має відповідати даним тегу UtilizedLogisticsTransportEquipment 	Supply Chain_ Consignment Item. Associated. Referenced_ Logistics_ Transport Equipment (Referenced_ Logistics_ Transport Equipment. Identification. Identifier)
    210
        3.18.9		IncludedSupplyChainConsignmentItem.AssociatedReferencedDocument.ID
    + IncludedSupplyChainConsignmentItem.AssociatedReferencedDocument.Remarks	string	Документи з вантажем		optional	реквізити документів, які водій отримує від вантажовідправника і передає вантажоодержувачеві разом з вантажем (товарні, залізничні накладні, сертифікати, свідоцтва тощо)	Supply Chain_ Consignment Item. Associated. Referenced_ Document (Referenced_ Document. Identification. Identifier + Referenced_ Document. Remarks. Text)
    211
        3.18.10		IncludedSupplyChainConsignmentItem.TransportLogisticsPackage		Транспортна упаковка		optional		Supply Chain_ Consignment Item. Transport. Logistics_ Package
    212
        3.18.10.1		IncludedSupplyChainConsignmentItem.TransportLogisticsPackage.ItemQuantity	decimal	Кількість місць		optional	кількість місць, які визначаються за кожним найменуванням вантажу (це можуть бути ящики, кошики, мішки тощо; якщо вантаж упаковано на піддонах - вказують кількість піддонів)	Logistics_ Package. Item. Quantity
    213
        3.18.10.2		IncludedSupplyChainConsignmentItem.TransportLogisticsPackage.TypeCode	string	Вид пакування	значення з довідника	optional	довідник видів упаковок	Logistics_ Package. Type. Code
    214
        3.18.10.3		IncludedSupplyChainConsignmentItem.TransportLogisticsPackage.Type	string	Одиниця виміру		optional	одиниця виміру для ItemQuantity	Logistics_ Package. Type. Text
    215
        3.18.10.4		IncludedSupplyChainConsignmentItem.TransportLogisticsPackage.PhysicalLogisticsShippingMarks.Marking	string	Назва транспортної упаковки		optional	вільна назва транспортної упаковки, в якій перевозиться вантаж (див.приклад)	Logistics_ Package. Physical. Logistics_ Shipping Marks
    216
        3.18.10.5		IncludedSupplyChainConsignmentItem.TransportLogisticsPackage.PhysicalLogisticsShippingMarks.BarcodeLogisticsLabel.ID	string	Штрихкод товару		optional	Штрихкод товару	Logistics_ Shipping Marks. Barcode. Logistics_ Label
    217
        3.18.11		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом VENDOR_CODE)	string	Артикул товару		optional	Артикул товару	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    218
        3.18.12		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом QUANTITY)	string	Кількість товару		optional		Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    219
        3.18.13		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом URL)	string	Посилання на документ		optional		Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    220
        3.18.14		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом BASE_UOM)	string	Одиниця виміру кількості товару		optional	одиниця виміру для QUANTITY	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    221
        3.18.15		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом BUYER_CODE)	string	Артикул покупця		optional	Артикул покупця (використовується для ідентифікації товарної позиції при прийманні)	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    222
        3.18.16		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом PRICE_WITH_VAT)	string	Ціна за одиницю з ПДВ		optional	Ціна за одиницю з ПДВ	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    223
        3.18.17		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом SUM_WITHOUT_VAT)	string	Загальна сума без ПДВ		optional	Загальна сума без ПДВ	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    224
        3.18.18		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом RETURN_TARE)	string	Ознака "зворотня тара"		optional		Logistics_ Package. Returnable. Indicator
    225
        3.18.19		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом NET_WEIGHT)	string	Маса нетто		optional	Маса нетто	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    226
        3.18.20		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом RTP_TYPE)	string	Тип транспортної упаковки		optional	Тип транспортної упаковки, наприклад, контейнер	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    227
        3.18.21		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом RTP_NAME)	string	Назва транспортної упаковки		optional	Назва транспортної упаковки, наприклад, контейнер для перевезення сипучих речовин	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    228
        3.18.22		IncludedSupplyChainConsignmentItem.ApplicableNote.Content (з кодом RTP_QUANTITY)	string	Кількість транспортної упаковки		optional	Кількість транспортної упаковки (використовується для обліку оборотної тари)	Supply Chain_ Consignment Item. Applicable. Note (Note. Content. Text)
    229
        3.19		
    UtilizedLogisticsTransportEquipment (CategoryCode=TRUCK)
            Автомобіль		mandatory		Supply Chain_ Consignment. Utilized. Logistics_ Transport Equipment
    230
        3.19.1		UtilizedLogisticsTransportEquipment.CategoryCode (якщо відсутній - то вантажний)	string	Тип автомобіля	Вантажний TRUCK 	mandatory	тип автомобіля: вантажний	Logistics_ Transport Equipment. Category. Code
    231
        3.19.2		UtilizedLogisticsTransportEquipment. ID	string	Реєстраційний номер автомобіля	1. укр.номери: має відповідати одному з патернів для автомобільних номерних знаків
    2. єврономери: без валідації	mandatory	реєстраційний номер автомобіля згідно з техпаспортом	Logistics_ Transport Equipment. Identification. Identifier
    232
        3.19.3		UtilizedLogisticsTransportEquipment.AffixedLogisticsSeal. ID	string	Номер пломби (автомобіль)		optional	відбиток пломби, якою проводилося пломбування автомобіля	Logistics_ Transport Equipment. Affixed. Logistics_ Seal (Logistics_ Seal. Identification. Identifier)
    233
        3.19.4		HandlingInstructions.ApplicableTransportSettingTemperature.MinimumValueMeasure + HandlingInstructions.ApplicableTransportSettingTemperature.MaximumValueMeasure	string	Температурний режим		optional	опис температурного режиму, необхідного для перевезення вантажу.
    діапазон температур	Transport Setting_ Temperature. Minimum_ Value. Measure +
    Transport Setting_ Temperature. Maximum_ Value. Measure
    234
        3.19.5		UtilizedLogisticsTransportEquipment.ApplicableNote (BRAND)	string	Марка автомобіля		mandatory	марка автомобіля згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    235
        3.19.6		UtilizedLogisticsTransportEquipment.ApplicableNote (MODEL)	string	Модель автомобіля		mandatory	модель автомобіля згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    236
        3.19.7		UtilizedLogisticsTransportEquipment.ApplicableNote (COLOR)	string	Колір автомобіля		optional	колір автомобіля згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    237
        3.19.8		UtilizedLogisticsTransportEquipment.ApplicableNote (TYPE)	string	Тип (назва) автомобіля		optional	тип автомобіля згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    238
        3.20		
    UtilizedLogisticsTransportEquipment (CategoryCode=TE)
            Причіп/напівпричіп		optional		Supply Chain_ Consignment. Utilized. Logistics_ Transport Equipment
    239
        3.20.1		UtilizedLogisticsTransportEquipment.CategoryCode	string	Вид транспортного засобу	TE	mandatory	причіп/напівпричіп	Logistics_ Transport Equipment. Category. Code
    240
        3.20.2		UtilizedLogisticsTransportEquipment.CharacteristicCode	string	Тип причіп/напівпричіп	Причіп 14
    Напівпричіп 17 	mandatory	тип: причіп або напівпричіп	Logistics_ Transport Equipment. Characteristic. Code
    241
        3.20.3		UtilizedLogisticsTransportEquipment. ID	string	Реєстраційний номер причіп/напівпричіп		mandatory	реєстраційний номер причіпа/напівпричіпа 1 згідно з техпаспортом	Logistics_ Transport Equipment. Identification. Identifier
    242
        3.20.4		UtilizedLogisticsTransportEquipment.AffixedLogisticsSeal. ID	string	Номер пломби (причіп/напівпричіп)		optional	відбиток пломби, якою проводилося пломбування причіпа/напівпричіпа	Logistics_ Transport Equipment. Affixed. Logistics_ Seal (Logistics_ Seal. Identification. Identifier)
    243
        3.20.5		HandlingInstructions.ApplicableTransportSettingTemperature.MinimumValueMeasure + HandlingInstructions.ApplicableTransportSettingTemperature.MaximumValueMeasure	string	Температурний режим		optional	опис температурного режиму, необхідного для перевезення вантажу.
    діапазон температур	Transport Setting_ Temperature. Minimum_ Value. Measure +
    Transport Setting_ Temperature. Maximum_ Value. Measure
    244
        3.20.6		UtilizedLogisticsTransportEquipment.ApplicableNote (BRAND)	string	Марка причіп/напівпричіп		mandatory	марка причіпа/напівпричіпа 1 згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    245
        3.20.7		UtilizedLogisticsTransportEquipment.ApplicableNote (MODEL)	string	Модель причіп/напівпричіп		mandatory	модель причіпа/напівпричіпа 1 згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    246
        3.20.8		UtilizedLogisticsTransportEquipment.ApplicableNote (TYPE)	string	Тип (назва) причіп/напівпричіп		optional	тип причіпа/напівпричіпа згідно з техпаспортом	Logistics_ Transport Equipment. Applicable. Note
    247
        3.21		
    UtilizedLogisticsTransportEquipment (CategoryCode=CN)
            Контейнер		optional		Supply Chain_ Consignment. Utilized. Logistics_ Transport Equipment
    248
        3.21.1		UtilizedLogisticsTransportEquipment.CategoryCode	string	Вид транспортного засобу	CN	mandatory	контейнер	Logistics_ Transport Equipment. Category. Code
    249
        3.21.2		UtilizedLogisticsTransportEquipment.CharacteristicCode	string	Тип контейнера	20-футовий 21
    40-футовий 23	mandatory	тип: 20-футовий або 40-футовий контейнер 	Logistics_ Transport Equipment. Characteristic. Code
    250
        3.21.3		UtilizedLogisticsTransportEquipment. ID	string	Ідентифікаційний номер контейнера		mandatory	Ідентифікаційний номер контейнера	Logistics_ Transport Equipment. Identification. Identifier
    251
        3.21.4		UtilizedLogisticsTransportEquipment.AffixedLogisticsSeal. ID	string	Номер пломби контейнера		optional	відбиток пломби, якою проводилося пломбування контейнера	Logistics_ Transport Equipment. Affixed. Logistics_ Seal (Logistics_ Seal. Identification. Identifier)
    252
        3.21.5		HandlingInstructions.ApplicableTransportSettingTemperature.MinimumValueMeasure + HandlingInstructions.ApplicableTransportSettingTemperature.MaximumValueMeasure	string	Температурний режим		optional	опис температурного режиму, необхідного для перевезення вантажу.
    діапазон температур	Transport Setting_ Temperature. Minimum_ Value. Measure +
    Transport Setting_ Temperature. Maximum_ Value. Measure
    253
        3.22		MainCarriageLogisticsTransportMovement		
    Маршрутизація (проміжні пункти перевантаження)
            optional	Заповнюється Перевізником	Supply Chain_ Consignment. Main Carriage. Logistics_ Transport Movement
    254
        3.22.1		MainCarriageLogisticsTransportMovement.ModeCode	string	Код	3	mandatory	завжди одне значення (3), оскільки використовується лише для дорожніх перевезень	Logistics_ Transport Movement. Mode. Code
    255
        3.22.2		MainCarriageLogisticsTransportMovement.SpecifiedTransportEvent		Проміжне розвантаження		mandatory		Logistics_ Transport Movement. Specified. Transport_ Event
    256
        3.22.2.1		SpecifiedTransportEvent.ID	string	Порядковий номер події		mandatory	Події завжди нумеруються в порядку поступового зростання за принципом N+1	Transport_ Event. Identification. Identifier
    257
        3.22.2.2		SpecifiedTransportEvent.TypeCode	string	Тип операції	розвантаження 5	mandatory	завжди одне значення (5), оскільки використовується як планові пункти розвантаження	Transport_ Event. Type. Code
    258
        3.22.2.3		SpecifiedTransportEvent.Description	string	Опис		optional		Transport_ Event. Description. Text
    259
        3.22.2.4		SpecifiedTransportEvent.OccurrenceLogisticsLocation		Місцезнаходження		mandatory		Transport_ Event. Occurrence. Logistics_ Location
    260
        3.22.2.4.1		SpecifiedTransportEvent.OccurrenceLogisticsLocation.ID (schemeAgencyID="КАТОТТГ")	string	Код КАТОТТГ складу		mandatory	код складу тимчасового зберігання відповідно до Кодифікатора адміністративно-територіальних одиниць та територій територіальних громад 	Logistics_ Location. Identification. Identifier (Identification Scheme Agency. Identifier)
    261
        3.22.2.4.2		SpecifiedTransportEvent.OccurrenceLogisticsLocation.TypeCode	string	Тип операції	розвантаження 5	mandatory	завжди одне значення (5), оскільки використовується як планові пункти розвантаження	Logistics_ Location. Type. Code
    262
        3.22.2.4.3		SpecifiedTransportEvent.OccurrenceLogisticsLocation.Name + SpecifiedTransportEvent.OccurrenceLogisticsLocation.Description	string	Місцезнаходження складу 		optional	найменування та адреса, додаткова інформація складу тимчасового зберігання	Logistics_ Location. Name. Text + Logistics_ Location. Description. Text
    263
        3.22.2.5		SpecifiedTransportEvent.CertifyingTradeParty (роль - WD)		Юридична особа Проміжний склад		mandatory		Transport_ Event. Certifying. Trade_ Party
    264
        3.22.2.5.1		SpecifiedTransportEvent.CertifyingTradeParty.ID	string	Ідентифікаційний код Проміжний склад	валідація за кількістю символів та згідно з алгоритмом перевірки контрольної суми	mandatory	ЄДРПОУ підприємства (Вантажовідправник/Перевізник/Експедитор/Вантажоодержувач/Товарний склад), що приймає від Перевізника на тимчасове зберігання вантаж 	Trade_ Party. Identification. Identifier
    265
        3.22.2.5.2		SpecifiedTransportEvent.CertifyingTradeParty.Name	string	Повне найменування Проміжний склад		mandatory	Повне найменування підприємства (Вантажовідправник/Перевізник/Експедитор/Вантажоодержувач/Товарний склад), що приймає від Перевізника на тимчасове зберігання вантаж 	Trade_ Party. Name. Text
    266
        3.22.2.5.3		SpecifiedTransportEvent.CertifyingTradeParty.RoleCode	string	Роль учасника	проміжний склад WD	mandatory	довідник ролей	Trade_ Party. Role. Code
    267
        3.22.2.5.4		CertifyingTradeParty.PostalTradeAddress		Юридична адреса Проміжний склад		mandatory	Юридична адреса підприємства (Вантажовідправник/Перевізник/Експедитор/Вантажоодержувач/Товарний склад), що приймає від Перевізника на тимчасове зберігання вантаж 	Trade_ Party. Postal. Trade_ Address
    268
        3.22.2.5.4.1		CertifyingTradeParty.PostalTradeAddress.PostcodeCode	string	Індекс		optional	Індекс	Trade_ Address. Postcode. Code
    269
        3.22.2.5.4.2		CertifyingTradeParty.PostalTradeAddress.StreetName	string	Адреса		mandatory	Назва вулиці + номер будівлі	Trade_ Address. Street Name. Text
    270
        3.22.2.5.4.3		CertifyingTradeParty.PostalTradeAddress.CityName	string	Місто		mandatory	Назва населеного пункту	Trade_ Address. City Name. Text
    271
        3.22.2.5.4.4		CertifyingTradeParty.PostalTradeAddress.CountryID	string	Країна	Україна UA	mandatory	Країна	Trade_ Address. Country. Identifier
    272
        3.22.2.5.4.5		CertifyingTradeParty.PostalTradeAddress.CountrySubDivisionName	string	Область + район		optional	Область та район (за наявності)	Trade_ Address. Country Sub-Division Name. Text
    273
        3.22.2.5.5		CertifyingTradeParty.DefinedTradeContact		Контактні/відповідальні особи Проміжний склад		optional		Trade_ Party. Defined. Trade_ Contact
    274
        3.22.2.5.5.1		CertifyingTradeParty.DefinedTradeContact.PersonName	string	ПІБ		optional		Trade_ Contact. Person Name. Text
    275
        3.22.2.5.5.2		CertifyingTradeParty.DefinedTradeContact.TelephoneUniversalCommunication.CompleteNumber	string	Основний телефон		optional		Trade_ Contact. Telephone. Universal_ Communication
    276
        3.22.2.5.5.3		CertifyingTradeParty.DefinedTradeContact.MobileTelephoneUniversalCommunication.CompleteNumber	string	Мобільний телефон		optional		Trade_ Contact. Mobile_ Telephone. Universal_ Communication
    277
        3.22.2.5.5.4		CertifyingTradeParty.DefinedTradeContact.EmailURIUniversalCommunication.CompleteNumber	string	Електронна адреса		optional		Trade_ Contact. Email_ URI. Universal_ Communication
    278
        3.22.2.5.5.5		CertifyingTradeParty.SpecifiedTaxRegistration	string	Ідентифікаційний код в.о.		optional	РНОКПП відповідальної особи за необхідності	Trade_ Party. Specified. Tax_ Registration
    279
        II		UaSignatureStorage		Підписи				
    280
        1		UaSignatureStorage.VisualReferencedDocument				optional		
    281
        1.1		UaSignatureStorage.VisualReferencedDocument.TypeCode	string	Тип	ТТН 730	mandatory	довідник кодів документів	
    282
        1.2		UaSignatureStorage.VisualReferencedDocument.Remarks	string	Графічне зображення е-ТТН		optional	base64 графічного відображення документа	
    283
        2		UaSignatureStorage.Signature (SigningPartyRoleCode=CZ)		ЕП в.о. Вантажовідправника		mandatory		
    284
        2.1		UaSignatureStorage.Signature.SigningPartyRoleCode	string	Роль підписувача	вантажовідправник CZ	mandatory	вантажовідправник	
    285
        2.2		UaSignatureStorage.Signature.PartySignature	string	Підпис		mandatory	base64 підпису p7s	
    286
        2.3		UaSignatureStorage.Signature.Name	string	ПІБ		mandatory	ПІБ підписувача (відповідальної особи вантажовідправника)	
    287
        2.4		UaSignatureStorage.Signature.Position	string	Посада		optional	Посада підписувача (відповідальної особи вантажовідправника)	
    288
        2.5		UaSignatureStorage.Signature.SpecifiedTaxRegistration.ID	string	Ідентифікаційний код		mandatory	РНОКПП підписувача (відповідальної особи вантажовідправника)	
    289
        3		UaSignatureStorage.Signature (SigningPartyRoleCode=DR)		ЕП водія Перевізника		mandatory		
    290
        3.1		UaSignatureStorage.Signature.SigningPartyRoleCode	string	Роль підписувача	водій DR	mandatory	водій	
    291
        3.2		UaSignatureStorage.Signature.PartySignature	string	Підпис		mandatory	base64 підпису p7s	
    292
        3.3		UaSignatureStorage.Signature.Name	string	ПІБ		mandatory	ПІБ підписувача (водія)	
    293
        3.4		UaSignatureStorage.Signature.Position	string	Посада		optional	Посада підписувача (водія)	
    294
        3.5		UaSignatureStorage.Signature.SpecifiedTaxRegistration.ID	string	Ідентифікаційний код		mandatory	РНОКПП підписувача (водія)	
    295
        4		UaSignatureStorage.Signature (SigningPartyRoleCode=CA)		ЕП в.о. Перевізника		optional		
    296
        4.1		UaSignatureStorage.Signature.SigningPartyRoleCode	string	Роль підписувача	перевізник СА	mandatory	перевізник	
    297
        4.2		UaSignatureStorage.Signature.PartySignature	string	Підпис		mandatory	base64 підпису p7s	
    298
        4.3		UaSignatureStorage.Signature.Name	string	ПІБ		mandatory	ПІБ підписувача (відповідальної особи перевізника)	
    299
        4.4		UaSignatureStorage.Signature.Position	string	Посада		optional	Посада підписувача (відповідальної особи перевізника)	
    300
        4.5		UaSignatureStorage.Signature.SpecifiedTaxRegistration.ID	string	Ідентифікаційний код		mandatory	РНОКПП підписувача (відповідальної особи перевізника)	
    301
        5		UaSignatureStorage.Signature (SigningPartyRoleCode=CN)		ЕП в.о. Вантажоодержувача		mandatory		
    302
        5.1		UaSignatureStorage.Signature.SigningPartyRoleCode	string	Роль підписувача	вантажоодержувач CN	mandatory	вантажоодержувач	
    303
        5.2		UaSignatureStorage.Signature.PartySignature	string	Підпис		mandatory	base64 підпису p7s	
    304
        5.3		UaSignatureStorage.Signature.Name	string	ПІБ		mandatory	ПІБ підписувача (відповідальної особи вантажоодержувача)	
    305
        5.4		UaSignatureStorage.Signature.Position	string	Посада		optional	Посада підписувача (відповідальної особи вантажоодержувача)	
    306
        5.5		UaSignatureStorage.Signature.SpecifiedTaxRegistration.ID	string	Ідентифікаційний код		mandatory	РНОКПП підписувача (відповідальної особи вантажоодержувача)	
    307
                                        
    308
                                        
    309
        III		Extensions				
    310
        №		Назва тегу Uncefact	тип даних	значення тегу	обмеження	обов'язковість	зміст тегу (як заповнювати)	
    311
        1		Logistics_ Location. Identification (schemeAgencyID="КАТОТТГ")	string	Код КАТОТТГ		optional		Logistics_ Location. Identification. Identifier (Identification Scheme Agency. Identifier)
    312
        2		Logistics_ Location. Physical. Geographical Coordinate	string	GLN		optional		Logistics_ Location. Physical. Geographical Coordinate
    313
        3		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (TypeCode=315)	string	Номер договору	315	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    314
        4		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (Referenced_ Document. Effective. Specified_ Period)	datetime	Дата договору	315	optional		Supply Chain_ Consignment. Associated. Referenced_ Document (Referenced_ Document. Effective. Specified_ Period)
    315
        5		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (TypeCode=303)	string	Номер заявки на перевезення	303	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    316
        6		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (Referenced_ Document. Effective. Specified_ Period)	datetime	Дата заявки на перевезення	303	optional		Supply Chain_ Consignment. Associated. Referenced_ Document (Referenced_ Document. Effective. Specified_ Period)
    317
        7		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (TypeCode=220)	string	номер замовлення	220	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    318
        8		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (Referenced_ Document. Effective. Specified_ Period)	datetime	дата замовлення	220	optional		Supply Chain_ Consignment. Associated. Referenced_ Document (Referenced_ Document. Effective. Specified_ Period)
    319
        9		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (TypeCode=171)	string	номер повідомлення про відвантаження	171	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    320
        10		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (Referenced_ Document. Effective. Specified_ Period)	datetime	дата повідомлення про відвантаження	171	optional		Supply Chain_ Consignment. Associated. Referenced_ Document (Referenced_ Document. Effective. Specified_ Period)
    321
        11		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument	string	номер сертифіката	значення згідно з довідником	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    322
        12		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (TypeCode=395)	string	номер товарної накладної	395	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    323
        13		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (Referenced_ Document. Effective. Specified_ Period)	datetime	дата товарної накладної	395	optional		Supply Chain_ Consignment. Associated. Referenced_ Document (Referenced_ Document. Effective. Specified_ Period)
    324
        14		SpecifiedSupplyChainConsignment.AssociatedReferencedDocument (TypeCode=441)	string	Номер рейсу	441	optional	довідник кодів документів	Supply Chain_ Consignment. Associated. Referenced_ Document
    325
        15		Exchanged_ Document. Included. Note	string	Текстове поле	other	optional		Exchanged_ Document. Included. Note
    Published by Google Sheets–Report Abuse–Updated automatically every 5 minutes
