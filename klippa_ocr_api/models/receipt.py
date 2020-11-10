# coding: utf-8

"""
    Klippa Custom OCR API

    # Introduction The Klippa Custom OCR Webservice API is a REST webservice for custom OCR implementations by Klippa.  The service replies are JSON only.  The service base URL is https://custom-ocr.klippa.com/api/v1. The service base URL for the test environment is https://test.custom-ocr.klippa.com/api/v1, we test experimental templates and features there. It also hosts the demo interface.  # Authentication ## APIKeyHeader The API requires the following header to be set:  Header | Description | --- |--- |   X-Auth-Key  |  The auth key provided by Klippa. |  The Key is provided per customer by Klippa.  ## APIKeyQueryParam The key can also be provided in the request query as ```?X-Auth-Key=key```  ## APIPublicKeyHeader The Public API requires the following header to be set:  Header | Description | --- |--- |   X-Auth-Public-Key  |  The public auth key provided by Klippa. |  ## APIPublicKeyQueryParam The key can also be provided in the request query as ```?X-Auth-Public-Key=public-key```   # Calling the API from public applications If you want to call the API from a public application, like a mobile app, you should **NOT** embed your API key in the app, this key could be extracted and abused.  The way to do this is using our API to [generate a public key](#operation/createPublicKey) from your backend, and send that public key to your application. That way only users that are authenticated are allowed to call the API. That way you can also better monitor which users are using the API and prevent abuse. You can also configure the public key to be valid for a certain time and give a maximum amount of scans.  The public key API is not available for every API key, we have to enable this for you.  We also have a [complete scanner SDK for Android and iOS](https://www.klippa.com/en/ocr/ocr-sdk/) available that has this API integrated.  The Public API requires the following header to be set:  Header | Description | --- |--- |   X-Auth-Public-Key  |  The public auth key provided by Klippa. |  The key can also be provided in the request query as ```?X-Auth-Public-Key=public-key```   # API Client libraries  Language | Client | --- |--- |   Go  |   [go.tar.gz](/docs/static/clients/go.tar.gz) |   Java  |   [java.tar.gz](/docs/static/clients/java.tar.gz) |   PHP  |   [php.tar.gz](/docs/static/clients/php.tar.gz) |   Python  |   [python.tar.gz](/docs/static/clients/python.tar.gz) |   Typescript (Axios)  |   [typescript.tar.gz](/docs/static/clients/typescript.tar.gz) |   Swift 4  |   [swift4.tar.gz](/docs/static/clients/swift4.tar.gz) |   Swift 5  |   [swift5.tar.gz](/docs/static/clients/swift5.tar.gz) |   # Error codes ## Authentication errors  Code | Name | --- |--- |   100001  |   ErrorCodeAuthMissingKey |   100002  |   ErrorCodeAuthInvalidKey |   100003  |   ErrorCodeAuthError |   100004  |   ErrorCodeAuthNoCreditsLeft |   100005  |   ErrorCodeAuthInvalidPublicKey |   100006  |   ErrorCodeAuthPublicKeyNoScansLeft |   100007  |   ErrorCodeAuthPublicKeyExpired |   ## PDF Parser errors  Code | Name | --- |--- |   200001  |   ErrorCodePDFParserDocumentError |   200002  |   Obsolete |   200003  |   Obsolete |   200004  |   ErrorCodePDFParserNoAccessToTemplate |   200005  |   ErrorCodePDFParserConvertError |   200006  |   ErrorCodePDFParserParseError |   ## Document Parser errors  Code | Name | --- |--- |   300001  |   ErrorCodeDocumentParserDocumentError |   300002  |   Obsolete |   300003  |   Obsolete |   300004  |   ErrorCodeDocumentParserNoAccessToTemplate |   300005  |   ErrorCodeDocumentParserConvertError |   300006  |   ErrorCodeDocumentParserParseError |   300007  |   ErrorCodeDocumentParserTooBigFileError |   ## Public Key errors  Code | Name | --- |--- |   400001  |   ErrorCodePublicKeyNotAllowed |   400002  |   ErrorCodePublicKeyCreationFailed |   400003  |   ErrorCodePublicKeyInvalidScanLimit |   400004  |   ErrorCodePublicKeyInvalidValidTime |   400005  |   ErrorCodePublicKeyLoadError |   400006  |   ErrorCodePublicKeyNotFoundError |  # Userdata  The user_data field allows for sending additional data into the parser and can be used to enable extra features, improve the recognition of certain fields and improve the processing speed. The user_data must be given as a JSON-encoded string. All fields are optional, a documents may be submitted without this field.  The following fields are accepted in the user_data object:  Key | Value type  | Description | --|--|--| `client`| `Relation` object | A relation object containing information about the client that submits the document. It should contain information either the merchant of the customer of the invoice. This is indicated by the `transaction_type` key. If the `transaction_type` is set to `purchase`, the client is considered to be the customer. If the `transaction_type` is set to `sale`, the client is considered to be the merchant. `transaction_type`  | string  | The transaction type of the document for the client. If the invoices contains a sale that the client made, this field can be set to `sale`. If the invoice contains a purchase that the client made, this field can be set to `purchase`.| `relations`  | array of `Relation` objects  | An optional list of relations which have previously been used by the client. The list does not have to be complete, the OCR may suggest merchants and customers which are not in this list. | `transactions`  | array of `Transaction` objects  | An optional list of open transactions for the client. We use this list to validate and improve our OCR detections. | `purchase_orders`  | array of `PurchaseOrder` objects  | An optional list of purchase orders. It's identifier will be present in the output if the purchase order was found on the document | `locale`| `Locale` object | If the language or originating country of the document is known, these values may be set.   ## Relation object  The relation object may contain the following fields. All fields are optional and may be omitted if a field is not available. This user data can also be managed by [User Data Sets](#tag/UserDataSets) when allowed for your key.  Key | Value type  | Description | --|--|--| id|string|The ID of the relation in your own system, we will return this id in the `merchant_id` field if there is a match. In the User Data Set this is the ExternalID. name|string|The company name of the client street_name|string|The street name of the client address street_number|string|The street number of the client address zipcode|string|The zipcode of the client address city|string|The city of the client address country|string|The country of the client address. It must be provided as a 2-letter country code as specified by ISO 3166-1. For example `FR` for France and `NL` for The Netherlands vat_number|string|The vat number, formatted according to the EU VAT directive. It must start with the country code prefix, such as `FR` or `NL` coc_number|string|A chamber of commerce number. E.g. the Dutch KVK number, or the French SIRET/SIREN number phone|string|The phone number of the client. International calling codes, such as `+33` may be provided but are not required website|string|The full URL to the website email|string|The email address bank_account_number|string|The IBAN number   ## Transaction object  The transaction object may contain the following fields. All fields are optional and may be omitted if a field is not available. This user data can also be managed by [User Data Sets](#tag/UserDataSets) when allowed for your key.  Key | Value type  | Description | --|--|--| identifier|string|The identifier of the transaction as given by the bank date|string|The date of the transaction, in the format 2019-06-24 11:16:33 currency|string|The currency of the transaction, eg. EUR amount|float|The amount of the transaction, eg 23.56 description|string|The description of the transaction as given by the bank iban|string|The IBAN number that made the transaction name|string|The name of the bank account  ## PurchaseOrder object  The PurchaseOrder object may contain the following fields. The `date` and `amount` fields are optional. If given, the purchase order will only be searched for on the document if those fields match the document date and document total amount, respectively.  Key | Value type  | Description | --|--|--| identifier|string|The identifier of the purchase order purchase_order_number|string|The purchase order number which should be searched for on the document, e.g 'PO-12345' date|string|The expected document date, in the format 2019-06-24 11:16:33 amount|float|The expected total amount on the document, eg 23.56   ## Locale object In case the language and/or originating country of the document are known, these may be set in the locale object. The locale object may contain the following fields. Both fields are optional.  Key | Value type  | Description | --|--|--| language|string|A 2-letter language code according to ISO 3166-1. country|string|A 2-letter country code according to ISO 639.  ## Keyword and lineitem matching Keyword rules can be use to find strings in the text of the document using either a list of keywords or a regex.  Multiple rules may be given, each rule will provide a separate object in the output. All keywords and regexes are treated case-insensitive.  For example, by passing the following `keywords_rules` object, the regex will match all \"new product\" strings which are followed by a number. The matches are provided in the output in an object with \"id\" set to \"products\". The \"coupon\" rule can be used to count the number of occurrences of a list of words:  ``` { \"keyword_rules\": [ { \"id\": \"products\", \"regex\": \"(new product [0-9]+)\" }, { \"id\": \"coupon\", \"keywords\": [ \"coupon\" ] } ] } ```  If for example the keywords of \"products\" are matched 3 times in the text of the document, and the keywords of \"coupons\" 2 times, the output will be: ``` { \"matched_keywords\": [ { \"id\": \"products\", \"count\": 3 \"matches\": [\"new product 6\", \"new product 1\", \"new product 14\"] }, { \"id\": \"coupons\", \"count\": 2 \"matches\": [\"COUPON\", \"coupon\"] } ] } ```  ### Lineitem matching Similar to keyword rules, lineitems rules can be used to list products which contain a certain keyword. ``` { \"lineitem_rules\": [ { \"id\": \"fruit\", \"regex\": \"apple|banana\" }, { \"id\": \"vegetables\", \"keywords\": [ \"carrots\", \"broccoli\" ] } ] } ``` For example, if some of the lineitems on the document contain a word that is in the \"vegetables\" keyword list, they are of the present in the output under the \"vegetables\" key: ``` { \"matched_lineitems\": [ { \"id\": \"vegetables\", \"lineitems\": [ { \"title\": \"1kg carrots\", \"amount\": 164, \"amount_each\": 82, \"quantity\": 2 }, { \"title\": \"Set of 2 broccoli\", \"amount\": 164, \"amount_each\": 592, \"quantity\": 4 } ] } ] } ```  ## Userdata Example ``` { \"client\": { \"name\": \"\", \"street_name\": \"\", \"street_number\": \"\", \"zipcode\": \"\", \"city\": \"\", \"country\": \"\", \"vat_number\": \"\", \"coc_number\": \"\", \"phone\": \"\", \"website\": \"\", \"email\": \"\", \"bank_account_number\": \"\" }, \"transaction_type\": \"\", \"relations\": [ { \"name\": \"\", \"street_name\": \"\", \"street_number\": \"\", \"zipcode\": \"\", \"city\": \"\", \"country\": \"\", \"vat_number\": \"\", \"coc_number\": \"\", \"phone\": \"\", \"website\": \"\", \"email\": \"\", \"bank_account_number\": \"\" }, { \"name\": \"\", \"street_name\": \"\", \"street_number\": \"\", \"zipcode\": \"\", \"city\": \"\", \"country\": \"\", \"vat_number\": \"\", \"coc_number\": \"\", \"phone\": \"\", \"website\": \"\", \"email\": \"\", \"bank_account_number\": \"\" } ], \"locale\": { \"language\": \"\", \"country\": \"\" } } ```  # noqa: E501

    The version of the OpenAPI document: v0-15-56 - 1079148c9f913abee8defb181f6df7277de45506
    Contact: jeroen@klippa.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from klippa_ocr_api.configuration import Configuration


class Receipt(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'amount': 'int',
        'amount_change': 'int',
        'amountexvat': 'int',
        'barcodes': 'list[Barcode]',
        'currency': 'str',
        'customer_address': 'str',
        'customer_bank_account_number': 'str',
        'customer_bank_account_number_bic': 'str',
        'customer_city': 'str',
        'customer_coc_number': 'str',
        'customer_country': 'str',
        'customer_email': 'str',
        'customer_house_number': 'str',
        'customer_municipality': 'str',
        'customer_name': 'str',
        'customer_number': 'str',
        'customer_phone': 'str',
        'customer_province': 'str',
        'customer_reference': 'str',
        'customer_street_name': 'str',
        'customer_vat_number': 'str',
        'customer_website': 'str',
        'customer_zipcode': 'str',
        'date': 'str',
        'document_language': 'str',
        'document_subject': 'str',
        'document_type': 'str',
        'hash': 'str',
        'hash_duplicate': 'bool',
        'invoice_number': 'str',
        'invoice_type': 'str',
        'lines': 'list[ReceiptLineItem]',
        'matched_keywords': 'list[MatchedKeyword]',
        'matched_lineitems': 'list[MatchedLineItemsReceipt]',
        'matched_purchase_order_id': 'str',
        'merchant_address': 'str',
        'merchant_bank_account_number': 'str',
        'merchant_bank_account_number_bic': 'str',
        'merchant_bank_domestic_account_number': 'str',
        'merchant_bank_domestic_bank_code': 'str',
        'merchant_chain_liability_bank_account_number': 'str',
        'merchant_city': 'str',
        'merchant_coc_number': 'str',
        'merchant_country': 'str',
        'merchant_country_code': 'str',
        'merchant_email': 'str',
        'merchant_house_number': 'str',
        'merchant_id': 'str',
        'merchant_main_activity_code': 'str',
        'merchant_municipality': 'str',
        'merchant_name': 'str',
        'merchant_phone': 'str',
        'merchant_province': 'str',
        'merchant_street_name': 'str',
        'merchant_vat_number': 'str',
        'merchant_website': 'str',
        'merchant_zipcode': 'str',
        'order_number': 'str',
        'package_number': 'str',
        'payment_auth_code': 'str',
        'payment_card_account_number': 'str',
        'payment_card_bank': 'str',
        'payment_card_issuer': 'str',
        'payment_card_number': 'str',
        'payment_due_date': 'str',
        'payment_slip_code': 'str',
        'payment_slip_customer_number': 'str',
        'payment_slip_reference_number': 'str',
        'paymentmethod': 'str',
        'purchasedate': 'str',
        'purchasetime': 'str',
        'raw_text': 'str',
        'receipt_number': 'str',
        'server': 'str',
        'shop_number': 'str',
        'table_group': 'str',
        'table_number': 'str',
        'terminal_number': 'str',
        'transaction_number': 'str',
        'transaction_reference': 'str',
        'vat_context': 'str',
        'vatamount': 'int',
        'vatitems': 'list[ReceiptVAT]'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_change': 'amount_change',
        'amountexvat': 'amountexvat',
        'barcodes': 'barcodes',
        'currency': 'currency',
        'customer_address': 'customer_address',
        'customer_bank_account_number': 'customer_bank_account_number',
        'customer_bank_account_number_bic': 'customer_bank_account_number_bic',
        'customer_city': 'customer_city',
        'customer_coc_number': 'customer_coc_number',
        'customer_country': 'customer_country',
        'customer_email': 'customer_email',
        'customer_house_number': 'customer_house_number',
        'customer_municipality': 'customer_municipality',
        'customer_name': 'customer_name',
        'customer_number': 'customer_number',
        'customer_phone': 'customer_phone',
        'customer_province': 'customer_province',
        'customer_reference': 'customer_reference',
        'customer_street_name': 'customer_street_name',
        'customer_vat_number': 'customer_vat_number',
        'customer_website': 'customer_website',
        'customer_zipcode': 'customer_zipcode',
        'date': 'date',
        'document_language': 'document_language',
        'document_subject': 'document_subject',
        'document_type': 'document_type',
        'hash': 'hash',
        'hash_duplicate': 'hash_duplicate',
        'invoice_number': 'invoice_number',
        'invoice_type': 'invoice_type',
        'lines': 'lines',
        'matched_keywords': 'matched_keywords',
        'matched_lineitems': 'matched_lineitems',
        'matched_purchase_order_id': 'matched_purchase_order_id',
        'merchant_address': 'merchant_address',
        'merchant_bank_account_number': 'merchant_bank_account_number',
        'merchant_bank_account_number_bic': 'merchant_bank_account_number_bic',
        'merchant_bank_domestic_account_number': 'merchant_bank_domestic_account_number',
        'merchant_bank_domestic_bank_code': 'merchant_bank_domestic_bank_code',
        'merchant_chain_liability_bank_account_number': 'merchant_chain_liability_bank_account_number',
        'merchant_city': 'merchant_city',
        'merchant_coc_number': 'merchant_coc_number',
        'merchant_country': 'merchant_country',
        'merchant_country_code': 'merchant_country_code',
        'merchant_email': 'merchant_email',
        'merchant_house_number': 'merchant_house_number',
        'merchant_id': 'merchant_id',
        'merchant_main_activity_code': 'merchant_main_activity_code',
        'merchant_municipality': 'merchant_municipality',
        'merchant_name': 'merchant_name',
        'merchant_phone': 'merchant_phone',
        'merchant_province': 'merchant_province',
        'merchant_street_name': 'merchant_street_name',
        'merchant_vat_number': 'merchant_vat_number',
        'merchant_website': 'merchant_website',
        'merchant_zipcode': 'merchant_zipcode',
        'order_number': 'order_number',
        'package_number': 'package_number',
        'payment_auth_code': 'payment_auth_code',
        'payment_card_account_number': 'payment_card_account_number',
        'payment_card_bank': 'payment_card_bank',
        'payment_card_issuer': 'payment_card_issuer',
        'payment_card_number': 'payment_card_number',
        'payment_due_date': 'payment_due_date',
        'payment_slip_code': 'payment_slip_code',
        'payment_slip_customer_number': 'payment_slip_customer_number',
        'payment_slip_reference_number': 'payment_slip_reference_number',
        'paymentmethod': 'paymentmethod',
        'purchasedate': 'purchasedate',
        'purchasetime': 'purchasetime',
        'raw_text': 'raw_text',
        'receipt_number': 'receipt_number',
        'server': 'server',
        'shop_number': 'shop_number',
        'table_group': 'table_group',
        'table_number': 'table_number',
        'terminal_number': 'terminal_number',
        'transaction_number': 'transaction_number',
        'transaction_reference': 'transaction_reference',
        'vat_context': 'vat_context',
        'vatamount': 'vatamount',
        'vatitems': 'vatitems'
    }

    def __init__(self, amount=None, amount_change=None, amountexvat=None, barcodes=None, currency=None, customer_address=None, customer_bank_account_number=None, customer_bank_account_number_bic=None, customer_city=None, customer_coc_number=None, customer_country=None, customer_email=None, customer_house_number=None, customer_municipality=None, customer_name=None, customer_number=None, customer_phone=None, customer_province=None, customer_reference=None, customer_street_name=None, customer_vat_number=None, customer_website=None, customer_zipcode=None, date=None, document_language=None, document_subject=None, document_type=None, hash=None, hash_duplicate=None, invoice_number=None, invoice_type=None, lines=None, matched_keywords=None, matched_lineitems=None, matched_purchase_order_id=None, merchant_address=None, merchant_bank_account_number=None, merchant_bank_account_number_bic=None, merchant_bank_domestic_account_number=None, merchant_bank_domestic_bank_code=None, merchant_chain_liability_bank_account_number=None, merchant_city=None, merchant_coc_number=None, merchant_country=None, merchant_country_code=None, merchant_email=None, merchant_house_number=None, merchant_id=None, merchant_main_activity_code=None, merchant_municipality=None, merchant_name=None, merchant_phone=None, merchant_province=None, merchant_street_name=None, merchant_vat_number=None, merchant_website=None, merchant_zipcode=None, order_number=None, package_number=None, payment_auth_code=None, payment_card_account_number=None, payment_card_bank=None, payment_card_issuer=None, payment_card_number=None, payment_due_date=None, payment_slip_code=None, payment_slip_customer_number=None, payment_slip_reference_number=None, paymentmethod=None, purchasedate=None, purchasetime=None, raw_text=None, receipt_number=None, server=None, shop_number=None, table_group=None, table_number=None, terminal_number=None, transaction_number=None, transaction_reference=None, vat_context=None, vatamount=None, vatitems=None, local_vars_configuration=None):  # noqa: E501
        """Receipt - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._amount_change = None
        self._amountexvat = None
        self._barcodes = None
        self._currency = None
        self._customer_address = None
        self._customer_bank_account_number = None
        self._customer_bank_account_number_bic = None
        self._customer_city = None
        self._customer_coc_number = None
        self._customer_country = None
        self._customer_email = None
        self._customer_house_number = None
        self._customer_municipality = None
        self._customer_name = None
        self._customer_number = None
        self._customer_phone = None
        self._customer_province = None
        self._customer_reference = None
        self._customer_street_name = None
        self._customer_vat_number = None
        self._customer_website = None
        self._customer_zipcode = None
        self._date = None
        self._document_language = None
        self._document_subject = None
        self._document_type = None
        self._hash = None
        self._hash_duplicate = None
        self._invoice_number = None
        self._invoice_type = None
        self._lines = None
        self._matched_keywords = None
        self._matched_lineitems = None
        self._matched_purchase_order_id = None
        self._merchant_address = None
        self._merchant_bank_account_number = None
        self._merchant_bank_account_number_bic = None
        self._merchant_bank_domestic_account_number = None
        self._merchant_bank_domestic_bank_code = None
        self._merchant_chain_liability_bank_account_number = None
        self._merchant_city = None
        self._merchant_coc_number = None
        self._merchant_country = None
        self._merchant_country_code = None
        self._merchant_email = None
        self._merchant_house_number = None
        self._merchant_id = None
        self._merchant_main_activity_code = None
        self._merchant_municipality = None
        self._merchant_name = None
        self._merchant_phone = None
        self._merchant_province = None
        self._merchant_street_name = None
        self._merchant_vat_number = None
        self._merchant_website = None
        self._merchant_zipcode = None
        self._order_number = None
        self._package_number = None
        self._payment_auth_code = None
        self._payment_card_account_number = None
        self._payment_card_bank = None
        self._payment_card_issuer = None
        self._payment_card_number = None
        self._payment_due_date = None
        self._payment_slip_code = None
        self._payment_slip_customer_number = None
        self._payment_slip_reference_number = None
        self._paymentmethod = None
        self._purchasedate = None
        self._purchasetime = None
        self._raw_text = None
        self._receipt_number = None
        self._server = None
        self._shop_number = None
        self._table_group = None
        self._table_number = None
        self._terminal_number = None
        self._transaction_number = None
        self._transaction_reference = None
        self._vat_context = None
        self._vatamount = None
        self._vatitems = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if amount_change is not None:
            self.amount_change = amount_change
        if amountexvat is not None:
            self.amountexvat = amountexvat
        if barcodes is not None:
            self.barcodes = barcodes
        if currency is not None:
            self.currency = currency
        if customer_address is not None:
            self.customer_address = customer_address
        if customer_bank_account_number is not None:
            self.customer_bank_account_number = customer_bank_account_number
        if customer_bank_account_number_bic is not None:
            self.customer_bank_account_number_bic = customer_bank_account_number_bic
        if customer_city is not None:
            self.customer_city = customer_city
        if customer_coc_number is not None:
            self.customer_coc_number = customer_coc_number
        if customer_country is not None:
            self.customer_country = customer_country
        if customer_email is not None:
            self.customer_email = customer_email
        if customer_house_number is not None:
            self.customer_house_number = customer_house_number
        if customer_municipality is not None:
            self.customer_municipality = customer_municipality
        if customer_name is not None:
            self.customer_name = customer_name
        if customer_number is not None:
            self.customer_number = customer_number
        if customer_phone is not None:
            self.customer_phone = customer_phone
        if customer_province is not None:
            self.customer_province = customer_province
        if customer_reference is not None:
            self.customer_reference = customer_reference
        if customer_street_name is not None:
            self.customer_street_name = customer_street_name
        if customer_vat_number is not None:
            self.customer_vat_number = customer_vat_number
        if customer_website is not None:
            self.customer_website = customer_website
        if customer_zipcode is not None:
            self.customer_zipcode = customer_zipcode
        if date is not None:
            self.date = date
        if document_language is not None:
            self.document_language = document_language
        if document_subject is not None:
            self.document_subject = document_subject
        if document_type is not None:
            self.document_type = document_type
        if hash is not None:
            self.hash = hash
        if hash_duplicate is not None:
            self.hash_duplicate = hash_duplicate
        if invoice_number is not None:
            self.invoice_number = invoice_number
        if invoice_type is not None:
            self.invoice_type = invoice_type
        if lines is not None:
            self.lines = lines
        if matched_keywords is not None:
            self.matched_keywords = matched_keywords
        if matched_lineitems is not None:
            self.matched_lineitems = matched_lineitems
        if matched_purchase_order_id is not None:
            self.matched_purchase_order_id = matched_purchase_order_id
        if merchant_address is not None:
            self.merchant_address = merchant_address
        if merchant_bank_account_number is not None:
            self.merchant_bank_account_number = merchant_bank_account_number
        if merchant_bank_account_number_bic is not None:
            self.merchant_bank_account_number_bic = merchant_bank_account_number_bic
        if merchant_bank_domestic_account_number is not None:
            self.merchant_bank_domestic_account_number = merchant_bank_domestic_account_number
        if merchant_bank_domestic_bank_code is not None:
            self.merchant_bank_domestic_bank_code = merchant_bank_domestic_bank_code
        if merchant_chain_liability_bank_account_number is not None:
            self.merchant_chain_liability_bank_account_number = merchant_chain_liability_bank_account_number
        if merchant_city is not None:
            self.merchant_city = merchant_city
        if merchant_coc_number is not None:
            self.merchant_coc_number = merchant_coc_number
        if merchant_country is not None:
            self.merchant_country = merchant_country
        if merchant_country_code is not None:
            self.merchant_country_code = merchant_country_code
        if merchant_email is not None:
            self.merchant_email = merchant_email
        if merchant_house_number is not None:
            self.merchant_house_number = merchant_house_number
        if merchant_id is not None:
            self.merchant_id = merchant_id
        if merchant_main_activity_code is not None:
            self.merchant_main_activity_code = merchant_main_activity_code
        if merchant_municipality is not None:
            self.merchant_municipality = merchant_municipality
        if merchant_name is not None:
            self.merchant_name = merchant_name
        if merchant_phone is not None:
            self.merchant_phone = merchant_phone
        if merchant_province is not None:
            self.merchant_province = merchant_province
        if merchant_street_name is not None:
            self.merchant_street_name = merchant_street_name
        if merchant_vat_number is not None:
            self.merchant_vat_number = merchant_vat_number
        if merchant_website is not None:
            self.merchant_website = merchant_website
        if merchant_zipcode is not None:
            self.merchant_zipcode = merchant_zipcode
        if order_number is not None:
            self.order_number = order_number
        if package_number is not None:
            self.package_number = package_number
        if payment_auth_code is not None:
            self.payment_auth_code = payment_auth_code
        if payment_card_account_number is not None:
            self.payment_card_account_number = payment_card_account_number
        if payment_card_bank is not None:
            self.payment_card_bank = payment_card_bank
        if payment_card_issuer is not None:
            self.payment_card_issuer = payment_card_issuer
        if payment_card_number is not None:
            self.payment_card_number = payment_card_number
        if payment_due_date is not None:
            self.payment_due_date = payment_due_date
        if payment_slip_code is not None:
            self.payment_slip_code = payment_slip_code
        if payment_slip_customer_number is not None:
            self.payment_slip_customer_number = payment_slip_customer_number
        if payment_slip_reference_number is not None:
            self.payment_slip_reference_number = payment_slip_reference_number
        if paymentmethod is not None:
            self.paymentmethod = paymentmethod
        if purchasedate is not None:
            self.purchasedate = purchasedate
        if purchasetime is not None:
            self.purchasetime = purchasetime
        if raw_text is not None:
            self.raw_text = raw_text
        if receipt_number is not None:
            self.receipt_number = receipt_number
        if server is not None:
            self.server = server
        if shop_number is not None:
            self.shop_number = shop_number
        if table_group is not None:
            self.table_group = table_group
        if table_number is not None:
            self.table_number = table_number
        if terminal_number is not None:
            self.terminal_number = terminal_number
        if transaction_number is not None:
            self.transaction_number = transaction_number
        if transaction_reference is not None:
            self.transaction_reference = transaction_reference
        if vat_context is not None:
            self.vat_context = vat_context
        if vatamount is not None:
            self.vatamount = vatamount
        if vatitems is not None:
            self.vatitems = vatitems

    @property
    def amount(self):
        """Gets the amount of this Receipt.  # noqa: E501

        The total amount, in cents  # noqa: E501

        :return: The amount of this Receipt.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Receipt.

        The total amount, in cents  # noqa: E501

        :param amount: The amount of this Receipt.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def amount_change(self):
        """Gets the amount_change of this Receipt.  # noqa: E501

        The change amount, in cents  # noqa: E501

        :return: The amount_change of this Receipt.  # noqa: E501
        :rtype: int
        """
        return self._amount_change

    @amount_change.setter
    def amount_change(self, amount_change):
        """Sets the amount_change of this Receipt.

        The change amount, in cents  # noqa: E501

        :param amount_change: The amount_change of this Receipt.  # noqa: E501
        :type: int
        """

        self._amount_change = amount_change

    @property
    def amountexvat(self):
        """Gets the amountexvat of this Receipt.  # noqa: E501

        The total amount without vat, in cents  # noqa: E501

        :return: The amountexvat of this Receipt.  # noqa: E501
        :rtype: int
        """
        return self._amountexvat

    @amountexvat.setter
    def amountexvat(self, amountexvat):
        """Sets the amountexvat of this Receipt.

        The total amount without vat, in cents  # noqa: E501

        :param amountexvat: The amountexvat of this Receipt.  # noqa: E501
        :type: int
        """

        self._amountexvat = amountexvat

    @property
    def barcodes(self):
        """Gets the barcodes of this Receipt.  # noqa: E501

        Barcodes that are found on the document  # noqa: E501

        :return: The barcodes of this Receipt.  # noqa: E501
        :rtype: list[Barcode]
        """
        return self._barcodes

    @barcodes.setter
    def barcodes(self, barcodes):
        """Sets the barcodes of this Receipt.

        Barcodes that are found on the document  # noqa: E501

        :param barcodes: The barcodes of this Receipt.  # noqa: E501
        :type: list[Barcode]
        """

        self._barcodes = barcodes

    @property
    def currency(self):
        """Gets the currency of this Receipt.  # noqa: E501

        The three-letter currency code, as defined in ISO 4217, e.g. `EUR`  # noqa: E501

        :return: The currency of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this Receipt.

        The three-letter currency code, as defined in ISO 4217, e.g. `EUR`  # noqa: E501

        :param currency: The currency of this Receipt.  # noqa: E501
        :type: str
        """

        self._currency = currency

    @property
    def customer_address(self):
        """Gets the customer_address of this Receipt.  # noqa: E501

        The address line of the customer, as written on the document  # noqa: E501

        :return: The customer_address of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_address

    @customer_address.setter
    def customer_address(self, customer_address):
        """Sets the customer_address of this Receipt.

        The address line of the customer, as written on the document  # noqa: E501

        :param customer_address: The customer_address of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_address = customer_address

    @property
    def customer_bank_account_number(self):
        """Gets the customer_bank_account_number of this Receipt.  # noqa: E501

        The IBAN number of the customer.  # noqa: E501

        :return: The customer_bank_account_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_bank_account_number

    @customer_bank_account_number.setter
    def customer_bank_account_number(self, customer_bank_account_number):
        """Sets the customer_bank_account_number of this Receipt.

        The IBAN number of the customer.  # noqa: E501

        :param customer_bank_account_number: The customer_bank_account_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_bank_account_number = customer_bank_account_number

    @property
    def customer_bank_account_number_bic(self):
        """Gets the customer_bank_account_number_bic of this Receipt.  # noqa: E501

        The BIC associated with the IBAN number of the customer  # noqa: E501

        :return: The customer_bank_account_number_bic of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_bank_account_number_bic

    @customer_bank_account_number_bic.setter
    def customer_bank_account_number_bic(self, customer_bank_account_number_bic):
        """Sets the customer_bank_account_number_bic of this Receipt.

        The BIC associated with the IBAN number of the customer  # noqa: E501

        :param customer_bank_account_number_bic: The customer_bank_account_number_bic of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_bank_account_number_bic = customer_bank_account_number_bic

    @property
    def customer_city(self):
        """Gets the customer_city of this Receipt.  # noqa: E501


        :return: The customer_city of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_city

    @customer_city.setter
    def customer_city(self, customer_city):
        """Sets the customer_city of this Receipt.


        :param customer_city: The customer_city of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_city = customer_city

    @property
    def customer_coc_number(self):
        """Gets the customer_coc_number of this Receipt.  # noqa: E501

        The chamber of commerce number of the customer  # noqa: E501

        :return: The customer_coc_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_coc_number

    @customer_coc_number.setter
    def customer_coc_number(self, customer_coc_number):
        """Sets the customer_coc_number of this Receipt.

        The chamber of commerce number of the customer  # noqa: E501

        :param customer_coc_number: The customer_coc_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_coc_number = customer_coc_number

    @property
    def customer_country(self):
        """Gets the customer_country of this Receipt.  # noqa: E501

        The name of the country, as written on the document  # noqa: E501

        :return: The customer_country of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_country

    @customer_country.setter
    def customer_country(self, customer_country):
        """Sets the customer_country of this Receipt.

        The name of the country, as written on the document  # noqa: E501

        :param customer_country: The customer_country of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_country = customer_country

    @property
    def customer_email(self):
        """Gets the customer_email of this Receipt.  # noqa: E501


        :return: The customer_email of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_email

    @customer_email.setter
    def customer_email(self, customer_email):
        """Sets the customer_email of this Receipt.


        :param customer_email: The customer_email of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_email = customer_email

    @property
    def customer_house_number(self):
        """Gets the customer_house_number of this Receipt.  # noqa: E501

        The house number of the customer. It will only be set if the customer address could be split into a street name and house number  # noqa: E501

        :return: The customer_house_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_house_number

    @customer_house_number.setter
    def customer_house_number(self, customer_house_number):
        """Sets the customer_house_number of this Receipt.

        The house number of the customer. It will only be set if the customer address could be split into a street name and house number  # noqa: E501

        :param customer_house_number: The customer_house_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_house_number = customer_house_number

    @property
    def customer_municipality(self):
        """Gets the customer_municipality of this Receipt.  # noqa: E501


        :return: The customer_municipality of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_municipality

    @customer_municipality.setter
    def customer_municipality(self, customer_municipality):
        """Sets the customer_municipality of this Receipt.


        :param customer_municipality: The customer_municipality of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_municipality = customer_municipality

    @property
    def customer_name(self):
        """Gets the customer_name of this Receipt.  # noqa: E501

        The name of the customer  # noqa: E501

        :return: The customer_name of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_name

    @customer_name.setter
    def customer_name(self, customer_name):
        """Sets the customer_name of this Receipt.

        The name of the customer  # noqa: E501

        :param customer_name: The customer_name of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_name = customer_name

    @property
    def customer_number(self):
        """Gets the customer_number of this Receipt.  # noqa: E501

        A number used by the merchant to identify the customer  # noqa: E501

        :return: The customer_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_number

    @customer_number.setter
    def customer_number(self, customer_number):
        """Sets the customer_number of this Receipt.

        A number used by the merchant to identify the customer  # noqa: E501

        :param customer_number: The customer_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_number = customer_number

    @property
    def customer_phone(self):
        """Gets the customer_phone of this Receipt.  # noqa: E501


        :return: The customer_phone of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_phone

    @customer_phone.setter
    def customer_phone(self, customer_phone):
        """Sets the customer_phone of this Receipt.


        :param customer_phone: The customer_phone of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_phone = customer_phone

    @property
    def customer_province(self):
        """Gets the customer_province of this Receipt.  # noqa: E501


        :return: The customer_province of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_province

    @customer_province.setter
    def customer_province(self, customer_province):
        """Sets the customer_province of this Receipt.


        :param customer_province: The customer_province of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_province = customer_province

    @property
    def customer_reference(self):
        """Gets the customer_reference of this Receipt.  # noqa: E501

        A reference to this document, given by the customer  # noqa: E501

        :return: The customer_reference of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_reference

    @customer_reference.setter
    def customer_reference(self, customer_reference):
        """Sets the customer_reference of this Receipt.

        A reference to this document, given by the customer  # noqa: E501

        :param customer_reference: The customer_reference of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_reference = customer_reference

    @property
    def customer_street_name(self):
        """Gets the customer_street_name of this Receipt.  # noqa: E501

        The street name of the customer. It will only be set if the customer address could be split into a street name and house number  # noqa: E501

        :return: The customer_street_name of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_street_name

    @customer_street_name.setter
    def customer_street_name(self, customer_street_name):
        """Sets the customer_street_name of this Receipt.

        The street name of the customer. It will only be set if the customer address could be split into a street name and house number  # noqa: E501

        :param customer_street_name: The customer_street_name of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_street_name = customer_street_name

    @property
    def customer_vat_number(self):
        """Gets the customer_vat_number of this Receipt.  # noqa: E501

        The VAT number of the customer. It contains the two-letter country code, followed by a country-specific implementation of the VAT number.  # noqa: E501

        :return: The customer_vat_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_vat_number

    @customer_vat_number.setter
    def customer_vat_number(self, customer_vat_number):
        """Sets the customer_vat_number of this Receipt.

        The VAT number of the customer. It contains the two-letter country code, followed by a country-specific implementation of the VAT number.  # noqa: E501

        :param customer_vat_number: The customer_vat_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_vat_number = customer_vat_number

    @property
    def customer_website(self):
        """Gets the customer_website of this Receipt.  # noqa: E501


        :return: The customer_website of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_website

    @customer_website.setter
    def customer_website(self, customer_website):
        """Sets the customer_website of this Receipt.


        :param customer_website: The customer_website of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_website = customer_website

    @property
    def customer_zipcode(self):
        """Gets the customer_zipcode of this Receipt.  # noqa: E501

        The zipcode of the customer. Dutch postcodes are formatted as 1234 AB  # noqa: E501

        :return: The customer_zipcode of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._customer_zipcode

    @customer_zipcode.setter
    def customer_zipcode(self, customer_zipcode):
        """Sets the customer_zipcode of this Receipt.

        The zipcode of the customer. Dutch postcodes are formatted as 1234 AB  # noqa: E501

        :param customer_zipcode: The customer_zipcode of this Receipt.  # noqa: E501
        :type: str
        """

        self._customer_zipcode = customer_zipcode

    @property
    def date(self):
        """Gets the date of this Receipt.  # noqa: E501

        The purchase datetime as ISO string, E.g. `2019-07-01T16:46:00`  # noqa: E501

        :return: The date of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._date

    @date.setter
    def date(self, date):
        """Sets the date of this Receipt.

        The purchase datetime as ISO string, E.g. `2019-07-01T16:46:00`  # noqa: E501

        :param date: The date of this Receipt.  # noqa: E501
        :type: str
        """

        self._date = date

    @property
    def document_language(self):
        """Gets the document_language of this Receipt.  # noqa: E501

        The language of the document as a two-letter country code  # noqa: E501

        :return: The document_language of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._document_language

    @document_language.setter
    def document_language(self, document_language):
        """Sets the document_language of this Receipt.

        The language of the document as a two-letter country code  # noqa: E501

        :param document_language: The document_language of this Receipt.  # noqa: E501
        :type: str
        """

        self._document_language = document_language

    @property
    def document_subject(self):
        """Gets the document_subject of this Receipt.  # noqa: E501

        The subject of the document  # noqa: E501

        :return: The document_subject of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._document_subject

    @document_subject.setter
    def document_subject(self, document_subject):
        """Sets the document_subject of this Receipt.

        The subject of the document  # noqa: E501

        :param document_subject: The document_subject of this Receipt.  # noqa: E501
        :type: str
        """

        self._document_subject = document_subject

    @property
    def document_type(self):
        """Gets the document_type of this Receipt.  # noqa: E501


        :return: The document_type of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this Receipt.


        :param document_type: The document_type of this Receipt.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "invoice", "receipt", "bank_transaction", "bank_overview", "parking", "petrol", "ticket", "boarding_pass", "other"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and document_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `document_type` ({0}), must be one of {1}"  # noqa: E501
                .format(document_type, allowed_values)
            )

        self._document_type = document_type

    @property
    def hash(self):
        """Gets the hash of this Receipt.  # noqa: E501

        Unique hash of the receipt.  # noqa: E501

        :return: The hash of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._hash

    @hash.setter
    def hash(self, hash):
        """Sets the hash of this Receipt.

        Unique hash of the receipt.  # noqa: E501

        :param hash: The hash of this Receipt.  # noqa: E501
        :type: str
        """

        self._hash = hash

    @property
    def hash_duplicate(self):
        """Gets the hash_duplicate of this Receipt.  # noqa: E501

        Whether we have seen the hash before for the current key.  # noqa: E501

        :return: The hash_duplicate of this Receipt.  # noqa: E501
        :rtype: bool
        """
        return self._hash_duplicate

    @hash_duplicate.setter
    def hash_duplicate(self, hash_duplicate):
        """Sets the hash_duplicate of this Receipt.

        Whether we have seen the hash before for the current key.  # noqa: E501

        :param hash_duplicate: The hash_duplicate of this Receipt.  # noqa: E501
        :type: bool
        """

        self._hash_duplicate = hash_duplicate

    @property
    def invoice_number(self):
        """Gets the invoice_number of this Receipt.  # noqa: E501

        The number of the invoice  # noqa: E501

        :return: The invoice_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._invoice_number

    @invoice_number.setter
    def invoice_number(self, invoice_number):
        """Sets the invoice_number of this Receipt.

        The number of the invoice  # noqa: E501

        :param invoice_number: The invoice_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._invoice_number = invoice_number

    @property
    def invoice_type(self):
        """Gets the invoice_type of this Receipt.  # noqa: E501


        :return: The invoice_type of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._invoice_type

    @invoice_type.setter
    def invoice_type(self, invoice_type):
        """Sets the invoice_type of this Receipt.


        :param invoice_type: The invoice_type of this Receipt.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "invoice", "credit_invoice"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and invoice_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `invoice_type` ({0}), must be one of {1}"  # noqa: E501
                .format(invoice_type, allowed_values)
            )

        self._invoice_type = invoice_type

    @property
    def lines(self):
        """Gets the lines of this Receipt.  # noqa: E501


        :return: The lines of this Receipt.  # noqa: E501
        :rtype: list[ReceiptLineItem]
        """
        return self._lines

    @lines.setter
    def lines(self, lines):
        """Sets the lines of this Receipt.


        :param lines: The lines of this Receipt.  # noqa: E501
        :type: list[ReceiptLineItem]
        """

        self._lines = lines

    @property
    def matched_keywords(self):
        """Gets the matched_keywords of this Receipt.  # noqa: E501

        If keywords have been given in the userdata, matched_keywords will contain the id's of the keywords that matched, and their number of occurrences.  # noqa: E501

        :return: The matched_keywords of this Receipt.  # noqa: E501
        :rtype: list[MatchedKeyword]
        """
        return self._matched_keywords

    @matched_keywords.setter
    def matched_keywords(self, matched_keywords):
        """Sets the matched_keywords of this Receipt.

        If keywords have been given in the userdata, matched_keywords will contain the id's of the keywords that matched, and their number of occurrences.  # noqa: E501

        :param matched_keywords: The matched_keywords of this Receipt.  # noqa: E501
        :type: list[MatchedKeyword]
        """

        self._matched_keywords = matched_keywords

    @property
    def matched_lineitems(self):
        """Gets the matched_lineitems of this Receipt.  # noqa: E501

        If keywords have been given for lineitems in the userdata, matched_lineitems will contain the id's of the keywords that matched, and the lineitems on which the matches were made.  # noqa: E501

        :return: The matched_lineitems of this Receipt.  # noqa: E501
        :rtype: list[MatchedLineItemsReceipt]
        """
        return self._matched_lineitems

    @matched_lineitems.setter
    def matched_lineitems(self, matched_lineitems):
        """Sets the matched_lineitems of this Receipt.

        If keywords have been given for lineitems in the userdata, matched_lineitems will contain the id's of the keywords that matched, and the lineitems on which the matches were made.  # noqa: E501

        :param matched_lineitems: The matched_lineitems of this Receipt.  # noqa: E501
        :type: list[MatchedLineItemsReceipt]
        """

        self._matched_lineitems = matched_lineitems

    @property
    def matched_purchase_order_id(self):
        """Gets the matched_purchase_order_id of this Receipt.  # noqa: E501

        The id of the purchase order from the user data  # noqa: E501

        :return: The matched_purchase_order_id of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._matched_purchase_order_id

    @matched_purchase_order_id.setter
    def matched_purchase_order_id(self, matched_purchase_order_id):
        """Sets the matched_purchase_order_id of this Receipt.

        The id of the purchase order from the user data  # noqa: E501

        :param matched_purchase_order_id: The matched_purchase_order_id of this Receipt.  # noqa: E501
        :type: str
        """

        self._matched_purchase_order_id = matched_purchase_order_id

    @property
    def merchant_address(self):
        """Gets the merchant_address of this Receipt.  # noqa: E501

        The address line of the merchant, as written on the document  # noqa: E501

        :return: The merchant_address of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_address

    @merchant_address.setter
    def merchant_address(self, merchant_address):
        """Sets the merchant_address of this Receipt.

        The address line of the merchant, as written on the document  # noqa: E501

        :param merchant_address: The merchant_address of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_address = merchant_address

    @property
    def merchant_bank_account_number(self):
        """Gets the merchant_bank_account_number of this Receipt.  # noqa: E501

        The IBAN bank account number of the merchant.  # noqa: E501

        :return: The merchant_bank_account_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_bank_account_number

    @merchant_bank_account_number.setter
    def merchant_bank_account_number(self, merchant_bank_account_number):
        """Sets the merchant_bank_account_number of this Receipt.

        The IBAN bank account number of the merchant.  # noqa: E501

        :param merchant_bank_account_number: The merchant_bank_account_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_bank_account_number = merchant_bank_account_number

    @property
    def merchant_bank_account_number_bic(self):
        """Gets the merchant_bank_account_number_bic of this Receipt.  # noqa: E501

        The BIC associated with the IBAN bank account number of the merchant  # noqa: E501

        :return: The merchant_bank_account_number_bic of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_bank_account_number_bic

    @merchant_bank_account_number_bic.setter
    def merchant_bank_account_number_bic(self, merchant_bank_account_number_bic):
        """Sets the merchant_bank_account_number_bic of this Receipt.

        The BIC associated with the IBAN bank account number of the merchant  # noqa: E501

        :param merchant_bank_account_number_bic: The merchant_bank_account_number_bic of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_bank_account_number_bic = merchant_bank_account_number_bic

    @property
    def merchant_bank_domestic_account_number(self):
        """Gets the merchant_bank_domestic_account_number of this Receipt.  # noqa: E501

        The domestic bank account number of the merchant  # noqa: E501

        :return: The merchant_bank_domestic_account_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_bank_domestic_account_number

    @merchant_bank_domestic_account_number.setter
    def merchant_bank_domestic_account_number(self, merchant_bank_domestic_account_number):
        """Sets the merchant_bank_domestic_account_number of this Receipt.

        The domestic bank account number of the merchant  # noqa: E501

        :param merchant_bank_domestic_account_number: The merchant_bank_domestic_account_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_bank_domestic_account_number = merchant_bank_domestic_account_number

    @property
    def merchant_bank_domestic_bank_code(self):
        """Gets the merchant_bank_domestic_bank_code of this Receipt.  # noqa: E501

        The domestic bank code of the bank account of the merchant  # noqa: E501

        :return: The merchant_bank_domestic_bank_code of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_bank_domestic_bank_code

    @merchant_bank_domestic_bank_code.setter
    def merchant_bank_domestic_bank_code(self, merchant_bank_domestic_bank_code):
        """Sets the merchant_bank_domestic_bank_code of this Receipt.

        The domestic bank code of the bank account of the merchant  # noqa: E501

        :param merchant_bank_domestic_bank_code: The merchant_bank_domestic_bank_code of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_bank_domestic_bank_code = merchant_bank_domestic_bank_code

    @property
    def merchant_chain_liability_bank_account_number(self):
        """Gets the merchant_chain_liability_bank_account_number of this Receipt.  # noqa: E501

        The IBAN bank account number of the merchant used for Chain Liability G-Account (Wet Ketenaansprakelijkheid G-rekening)  # noqa: E501

        :return: The merchant_chain_liability_bank_account_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_chain_liability_bank_account_number

    @merchant_chain_liability_bank_account_number.setter
    def merchant_chain_liability_bank_account_number(self, merchant_chain_liability_bank_account_number):
        """Sets the merchant_chain_liability_bank_account_number of this Receipt.

        The IBAN bank account number of the merchant used for Chain Liability G-Account (Wet Ketenaansprakelijkheid G-rekening)  # noqa: E501

        :param merchant_chain_liability_bank_account_number: The merchant_chain_liability_bank_account_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_chain_liability_bank_account_number = merchant_chain_liability_bank_account_number

    @property
    def merchant_city(self):
        """Gets the merchant_city of this Receipt.  # noqa: E501


        :return: The merchant_city of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_city

    @merchant_city.setter
    def merchant_city(self, merchant_city):
        """Sets the merchant_city of this Receipt.


        :param merchant_city: The merchant_city of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_city = merchant_city

    @property
    def merchant_coc_number(self):
        """Gets the merchant_coc_number of this Receipt.  # noqa: E501

        The chamber of commerce number of the merchant  # noqa: E501

        :return: The merchant_coc_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_coc_number

    @merchant_coc_number.setter
    def merchant_coc_number(self, merchant_coc_number):
        """Sets the merchant_coc_number of this Receipt.

        The chamber of commerce number of the merchant  # noqa: E501

        :param merchant_coc_number: The merchant_coc_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_coc_number = merchant_coc_number

    @property
    def merchant_country(self):
        """Gets the merchant_country of this Receipt.  # noqa: E501

        The name of the country, as written on the document  # noqa: E501

        :return: The merchant_country of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_country

    @merchant_country.setter
    def merchant_country(self, merchant_country):
        """Sets the merchant_country of this Receipt.

        The name of the country, as written on the document  # noqa: E501

        :param merchant_country: The merchant_country of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_country = merchant_country

    @property
    def merchant_country_code(self):
        """Gets the merchant_country_code of this Receipt.  # noqa: E501

        The name of the country as two-letter country code  # noqa: E501

        :return: The merchant_country_code of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_country_code

    @merchant_country_code.setter
    def merchant_country_code(self, merchant_country_code):
        """Sets the merchant_country_code of this Receipt.

        The name of the country as two-letter country code  # noqa: E501

        :param merchant_country_code: The merchant_country_code of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_country_code = merchant_country_code

    @property
    def merchant_email(self):
        """Gets the merchant_email of this Receipt.  # noqa: E501


        :return: The merchant_email of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_email

    @merchant_email.setter
    def merchant_email(self, merchant_email):
        """Sets the merchant_email of this Receipt.


        :param merchant_email: The merchant_email of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_email = merchant_email

    @property
    def merchant_house_number(self):
        """Gets the merchant_house_number of this Receipt.  # noqa: E501

        The house number of the merchant. It will only be set if the merchant address could be split into a street name and house number  # noqa: E501

        :return: The merchant_house_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_house_number

    @merchant_house_number.setter
    def merchant_house_number(self, merchant_house_number):
        """Sets the merchant_house_number of this Receipt.

        The house number of the merchant. It will only be set if the merchant address could be split into a street name and house number  # noqa: E501

        :param merchant_house_number: The merchant_house_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_house_number = merchant_house_number

    @property
    def merchant_id(self):
        """Gets the merchant_id of this Receipt.  # noqa: E501

        The identifier of the merchant. It is only present if the merchant is found using a relation that was provided in the user_data object, or was provided in a user_data_set.  # noqa: E501

        :return: The merchant_id of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_id

    @merchant_id.setter
    def merchant_id(self, merchant_id):
        """Sets the merchant_id of this Receipt.

        The identifier of the merchant. It is only present if the merchant is found using a relation that was provided in the user_data object, or was provided in a user_data_set.  # noqa: E501

        :param merchant_id: The merchant_id of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_id = merchant_id

    @property
    def merchant_main_activity_code(self):
        """Gets the merchant_main_activity_code of this Receipt.  # noqa: E501

        The main activity code of the merchant  # noqa: E501

        :return: The merchant_main_activity_code of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_main_activity_code

    @merchant_main_activity_code.setter
    def merchant_main_activity_code(self, merchant_main_activity_code):
        """Sets the merchant_main_activity_code of this Receipt.

        The main activity code of the merchant  # noqa: E501

        :param merchant_main_activity_code: The merchant_main_activity_code of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_main_activity_code = merchant_main_activity_code

    @property
    def merchant_municipality(self):
        """Gets the merchant_municipality of this Receipt.  # noqa: E501


        :return: The merchant_municipality of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_municipality

    @merchant_municipality.setter
    def merchant_municipality(self, merchant_municipality):
        """Sets the merchant_municipality of this Receipt.


        :param merchant_municipality: The merchant_municipality of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_municipality = merchant_municipality

    @property
    def merchant_name(self):
        """Gets the merchant_name of this Receipt.  # noqa: E501

        The name of the merchant  # noqa: E501

        :return: The merchant_name of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_name

    @merchant_name.setter
    def merchant_name(self, merchant_name):
        """Sets the merchant_name of this Receipt.

        The name of the merchant  # noqa: E501

        :param merchant_name: The merchant_name of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_name = merchant_name

    @property
    def merchant_phone(self):
        """Gets the merchant_phone of this Receipt.  # noqa: E501


        :return: The merchant_phone of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_phone

    @merchant_phone.setter
    def merchant_phone(self, merchant_phone):
        """Sets the merchant_phone of this Receipt.


        :param merchant_phone: The merchant_phone of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_phone = merchant_phone

    @property
    def merchant_province(self):
        """Gets the merchant_province of this Receipt.  # noqa: E501


        :return: The merchant_province of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_province

    @merchant_province.setter
    def merchant_province(self, merchant_province):
        """Sets the merchant_province of this Receipt.


        :param merchant_province: The merchant_province of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_province = merchant_province

    @property
    def merchant_street_name(self):
        """Gets the merchant_street_name of this Receipt.  # noqa: E501

        The street name of the merchant. It will only be set if the merchant address could be split into a street name and house number  # noqa: E501

        :return: The merchant_street_name of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_street_name

    @merchant_street_name.setter
    def merchant_street_name(self, merchant_street_name):
        """Sets the merchant_street_name of this Receipt.

        The street name of the merchant. It will only be set if the merchant address could be split into a street name and house number  # noqa: E501

        :param merchant_street_name: The merchant_street_name of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_street_name = merchant_street_name

    @property
    def merchant_vat_number(self):
        """Gets the merchant_vat_number of this Receipt.  # noqa: E501

        The VAT number of the merchant. It contains the two-letter country code, followed by a country-specific implementation of the VAT number.  # noqa: E501

        :return: The merchant_vat_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_vat_number

    @merchant_vat_number.setter
    def merchant_vat_number(self, merchant_vat_number):
        """Sets the merchant_vat_number of this Receipt.

        The VAT number of the merchant. It contains the two-letter country code, followed by a country-specific implementation of the VAT number.  # noqa: E501

        :param merchant_vat_number: The merchant_vat_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_vat_number = merchant_vat_number

    @property
    def merchant_website(self):
        """Gets the merchant_website of this Receipt.  # noqa: E501


        :return: The merchant_website of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_website

    @merchant_website.setter
    def merchant_website(self, merchant_website):
        """Sets the merchant_website of this Receipt.


        :param merchant_website: The merchant_website of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_website = merchant_website

    @property
    def merchant_zipcode(self):
        """Gets the merchant_zipcode of this Receipt.  # noqa: E501

        The zipcode of the merchant. Dutch postcodes are formatted as 1234 AB  # noqa: E501

        :return: The merchant_zipcode of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._merchant_zipcode

    @merchant_zipcode.setter
    def merchant_zipcode(self, merchant_zipcode):
        """Sets the merchant_zipcode of this Receipt.

        The zipcode of the merchant. Dutch postcodes are formatted as 1234 AB  # noqa: E501

        :param merchant_zipcode: The merchant_zipcode of this Receipt.  # noqa: E501
        :type: str
        """

        self._merchant_zipcode = merchant_zipcode

    @property
    def order_number(self):
        """Gets the order_number of this Receipt.  # noqa: E501

        The order number  # noqa: E501

        :return: The order_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._order_number

    @order_number.setter
    def order_number(self, order_number):
        """Sets the order_number of this Receipt.

        The order number  # noqa: E501

        :param order_number: The order_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._order_number = order_number

    @property
    def package_number(self):
        """Gets the package_number of this Receipt.  # noqa: E501

        Package number, usually found on packaging slips  # noqa: E501

        :return: The package_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._package_number

    @package_number.setter
    def package_number(self, package_number):
        """Sets the package_number of this Receipt.

        Package number, usually found on packaging slips  # noqa: E501

        :param package_number: The package_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._package_number = package_number

    @property
    def payment_auth_code(self):
        """Gets the payment_auth_code of this Receipt.  # noqa: E501

        The transaction authorization code  # noqa: E501

        :return: The payment_auth_code of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_auth_code

    @payment_auth_code.setter
    def payment_auth_code(self, payment_auth_code):
        """Sets the payment_auth_code of this Receipt.

        The transaction authorization code  # noqa: E501

        :param payment_auth_code: The payment_auth_code of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_auth_code = payment_auth_code

    @property
    def payment_card_account_number(self):
        """Gets the payment_card_account_number of this Receipt.  # noqa: E501

        The account number of the card that was used to complete the payment  # noqa: E501

        :return: The payment_card_account_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_card_account_number

    @payment_card_account_number.setter
    def payment_card_account_number(self, payment_card_account_number):
        """Sets the payment_card_account_number of this Receipt.

        The account number of the card that was used to complete the payment  # noqa: E501

        :param payment_card_account_number: The payment_card_account_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_card_account_number = payment_card_account_number

    @property
    def payment_card_bank(self):
        """Gets the payment_card_bank of this Receipt.  # noqa: E501


        :return: The payment_card_bank of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_card_bank

    @payment_card_bank.setter
    def payment_card_bank(self, payment_card_bank):
        """Sets the payment_card_bank of this Receipt.


        :param payment_card_bank: The payment_card_bank of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_card_bank = payment_card_bank

    @property
    def payment_card_issuer(self):
        """Gets the payment_card_issuer of this Receipt.  # noqa: E501

        Name of the party that issued the credit- or debit card  # noqa: E501

        :return: The payment_card_issuer of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_card_issuer

    @payment_card_issuer.setter
    def payment_card_issuer(self, payment_card_issuer):
        """Sets the payment_card_issuer of this Receipt.

        Name of the party that issued the credit- or debit card  # noqa: E501

        :param payment_card_issuer: The payment_card_issuer of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_card_issuer = payment_card_issuer

    @property
    def payment_card_number(self):
        """Gets the payment_card_number of this Receipt.  # noqa: E501


        :return: The payment_card_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_card_number

    @payment_card_number.setter
    def payment_card_number(self, payment_card_number):
        """Sets the payment_card_number of this Receipt.


        :param payment_card_number: The payment_card_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_card_number = payment_card_number

    @property
    def payment_due_date(self):
        """Gets the payment_due_date of this Receipt.  # noqa: E501

        Date on which the payment is due as ISO string, E.g. `2019-07-01T00:00:00`  # noqa: E501

        :return: The payment_due_date of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_due_date

    @payment_due_date.setter
    def payment_due_date(self, payment_due_date):
        """Sets the payment_due_date of this Receipt.

        Date on which the payment is due as ISO string, E.g. `2019-07-01T00:00:00`  # noqa: E501

        :param payment_due_date: The payment_due_date of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_due_date = payment_due_date

    @property
    def payment_slip_code(self):
        """Gets the payment_slip_code of this Receipt.  # noqa: E501

        The full code of the payment slip  # noqa: E501

        :return: The payment_slip_code of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_slip_code

    @payment_slip_code.setter
    def payment_slip_code(self, payment_slip_code):
        """Sets the payment_slip_code of this Receipt.

        The full code of the payment slip  # noqa: E501

        :param payment_slip_code: The payment_slip_code of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_slip_code = payment_slip_code

    @property
    def payment_slip_customer_number(self):
        """Gets the payment_slip_customer_number of this Receipt.  # noqa: E501

        The customer number of the payment slip  # noqa: E501

        :return: The payment_slip_customer_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_slip_customer_number

    @payment_slip_customer_number.setter
    def payment_slip_customer_number(self, payment_slip_customer_number):
        """Sets the payment_slip_customer_number of this Receipt.

        The customer number of the payment slip  # noqa: E501

        :param payment_slip_customer_number: The payment_slip_customer_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_slip_customer_number = payment_slip_customer_number

    @property
    def payment_slip_reference_number(self):
        """Gets the payment_slip_reference_number of this Receipt.  # noqa: E501

        The reference number of the payment slip  # noqa: E501

        :return: The payment_slip_reference_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._payment_slip_reference_number

    @payment_slip_reference_number.setter
    def payment_slip_reference_number(self, payment_slip_reference_number):
        """Sets the payment_slip_reference_number of this Receipt.

        The reference number of the payment slip  # noqa: E501

        :param payment_slip_reference_number: The payment_slip_reference_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._payment_slip_reference_number = payment_slip_reference_number

    @property
    def paymentmethod(self):
        """Gets the paymentmethod of this Receipt.  # noqa: E501


        :return: The paymentmethod of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._paymentmethod

    @paymentmethod.setter
    def paymentmethod(self, paymentmethod):
        """Sets the paymentmethod of this Receipt.


        :param paymentmethod: The paymentmethod of this Receipt.  # noqa: E501
        :type: str
        """
        allowed_values = ["", "cash", "creditcard", "pin", "bank"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and paymentmethod not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `paymentmethod` ({0}), must be one of {1}"  # noqa: E501
                .format(paymentmethod, allowed_values)
            )

        self._paymentmethod = paymentmethod

    @property
    def purchasedate(self):
        """Gets the purchasedate of this Receipt.  # noqa: E501

        The purchase date as `yyyy-mm-dd` string, e.g. `2019-07-01`  # noqa: E501

        :return: The purchasedate of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._purchasedate

    @purchasedate.setter
    def purchasedate(self, purchasedate):
        """Sets the purchasedate of this Receipt.

        The purchase date as `yyyy-mm-dd` string, e.g. `2019-07-01`  # noqa: E501

        :param purchasedate: The purchasedate of this Receipt.  # noqa: E501
        :type: str
        """

        self._purchasedate = purchasedate

    @property
    def purchasetime(self):
        """Gets the purchasetime of this Receipt.  # noqa: E501

        The purchase time as hh:mm:ss string, e.g. `16:46:00`  # noqa: E501

        :return: The purchasetime of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._purchasetime

    @purchasetime.setter
    def purchasetime(self, purchasetime):
        """Sets the purchasetime of this Receipt.

        The purchase time as hh:mm:ss string, e.g. `16:46:00`  # noqa: E501

        :param purchasetime: The purchasetime of this Receipt.  # noqa: E501
        :type: str
        """

        self._purchasetime = purchasetime

    @property
    def raw_text(self):
        """Gets the raw_text of this Receipt.  # noqa: E501

        Original plain text of receipt.  # noqa: E501

        :return: The raw_text of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this Receipt.

        Original plain text of receipt.  # noqa: E501

        :param raw_text: The raw_text of this Receipt.  # noqa: E501
        :type: str
        """

        self._raw_text = raw_text

    @property
    def receipt_number(self):
        """Gets the receipt_number of this Receipt.  # noqa: E501

        The receipt ticket number  # noqa: E501

        :return: The receipt_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._receipt_number

    @receipt_number.setter
    def receipt_number(self, receipt_number):
        """Sets the receipt_number of this Receipt.

        The receipt ticket number  # noqa: E501

        :param receipt_number: The receipt_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._receipt_number = receipt_number

    @property
    def server(self):
        """Gets the server of this Receipt.  # noqa: E501


        :return: The server of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._server

    @server.setter
    def server(self, server):
        """Sets the server of this Receipt.


        :param server: The server of this Receipt.  # noqa: E501
        :type: str
        """

        self._server = server

    @property
    def shop_number(self):
        """Gets the shop_number of this Receipt.  # noqa: E501

        A number that identifies the store in which the payment was processed. Usually found on EFT receipts.  # noqa: E501

        :return: The shop_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._shop_number

    @shop_number.setter
    def shop_number(self, shop_number):
        """Sets the shop_number of this Receipt.

        A number that identifies the store in which the payment was processed. Usually found on EFT receipts.  # noqa: E501

        :param shop_number: The shop_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._shop_number = shop_number

    @property
    def table_group(self):
        """Gets the table_group of this Receipt.  # noqa: E501


        :return: The table_group of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._table_group

    @table_group.setter
    def table_group(self, table_group):
        """Sets the table_group of this Receipt.


        :param table_group: The table_group of this Receipt.  # noqa: E501
        :type: str
        """

        self._table_group = table_group

    @property
    def table_number(self):
        """Gets the table_number of this Receipt.  # noqa: E501


        :return: The table_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._table_number

    @table_number.setter
    def table_number(self, table_number):
        """Sets the table_number of this Receipt.


        :param table_number: The table_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._table_number = table_number

    @property
    def terminal_number(self):
        """Gets the terminal_number of this Receipt.  # noqa: E501

        A number that identifies the terminal on which the payment was processed. Usually found on EFT receipts.  # noqa: E501

        :return: The terminal_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._terminal_number

    @terminal_number.setter
    def terminal_number(self, terminal_number):
        """Sets the terminal_number of this Receipt.

        A number that identifies the terminal on which the payment was processed. Usually found on EFT receipts.  # noqa: E501

        :param terminal_number: The terminal_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._terminal_number = terminal_number

    @property
    def transaction_number(self):
        """Gets the transaction_number of this Receipt.  # noqa: E501

        The transaction number provided by the payment processor. Usually found on EFT receipts.  # noqa: E501

        :return: The transaction_number of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._transaction_number

    @transaction_number.setter
    def transaction_number(self, transaction_number):
        """Sets the transaction_number of this Receipt.

        The transaction number provided by the payment processor. Usually found on EFT receipts.  # noqa: E501

        :param transaction_number: The transaction_number of this Receipt.  # noqa: E501
        :type: str
        """

        self._transaction_number = transaction_number

    @property
    def transaction_reference(self):
        """Gets the transaction_reference of this Receipt.  # noqa: E501

        A transaction reference provided by the merchant  # noqa: E501

        :return: The transaction_reference of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._transaction_reference

    @transaction_reference.setter
    def transaction_reference(self, transaction_reference):
        """Sets the transaction_reference of this Receipt.

        A transaction reference provided by the merchant  # noqa: E501

        :param transaction_reference: The transaction_reference of this Receipt.  # noqa: E501
        :type: str
        """

        self._transaction_reference = transaction_reference

    @property
    def vat_context(self):
        """Gets the vat_context of this Receipt.  # noqa: E501

        enum ,purchase_none,vat_relayed In case no vat was found, the vat context field may indicate a reason why no vat was found  # noqa: E501

        :return: The vat_context of this Receipt.  # noqa: E501
        :rtype: str
        """
        return self._vat_context

    @vat_context.setter
    def vat_context(self, vat_context):
        """Sets the vat_context of this Receipt.

        enum ,purchase_none,vat_relayed In case no vat was found, the vat context field may indicate a reason why no vat was found  # noqa: E501

        :param vat_context: The vat_context of this Receipt.  # noqa: E501
        :type: str
        """

        self._vat_context = vat_context

    @property
    def vatamount(self):
        """Gets the vatamount of this Receipt.  # noqa: E501

        The total VAT amount, in cents  # noqa: E501

        :return: The vatamount of this Receipt.  # noqa: E501
        :rtype: int
        """
        return self._vatamount

    @vatamount.setter
    def vatamount(self, vatamount):
        """Sets the vatamount of this Receipt.

        The total VAT amount, in cents  # noqa: E501

        :param vatamount: The vatamount of this Receipt.  # noqa: E501
        :type: int
        """

        self._vatamount = vatamount

    @property
    def vatitems(self):
        """Gets the vatitems of this Receipt.  # noqa: E501


        :return: The vatitems of this Receipt.  # noqa: E501
        :rtype: list[ReceiptVAT]
        """
        return self._vatitems

    @vatitems.setter
    def vatitems(self, vatitems):
        """Sets the vatitems of this Receipt.


        :param vatitems: The vatitems of this Receipt.  # noqa: E501
        :type: list[ReceiptVAT]
        """

        self._vatitems = vatitems

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Receipt):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Receipt):
            return True

        return self.to_dict() != other.to_dict()
