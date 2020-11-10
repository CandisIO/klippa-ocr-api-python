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


class ReceiptLineItemItem(object):
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
        'amount_each': 'int',
        'amount_ex_vat': 'int',
        'description': 'str',
        'quantity': 'float',
        'sku': 'str',
        'title': 'str',
        'vat_amount': 'int',
        'vat_code': 'str',
        'vat_percentage': 'int'
    }

    attribute_map = {
        'amount': 'amount',
        'amount_each': 'amount_each',
        'amount_ex_vat': 'amount_ex_vat',
        'description': 'description',
        'quantity': 'quantity',
        'sku': 'sku',
        'title': 'title',
        'vat_amount': 'vat_amount',
        'vat_code': 'vat_code',
        'vat_percentage': 'vat_percentage'
    }

    def __init__(self, amount=None, amount_each=None, amount_ex_vat=None, description=None, quantity=None, sku=None, title=None, vat_amount=None, vat_code=None, vat_percentage=None, local_vars_configuration=None):  # noqa: E501
        """ReceiptLineItemItem - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._amount = None
        self._amount_each = None
        self._amount_ex_vat = None
        self._description = None
        self._quantity = None
        self._sku = None
        self._title = None
        self._vat_amount = None
        self._vat_code = None
        self._vat_percentage = None
        self.discriminator = None

        if amount is not None:
            self.amount = amount
        if amount_each is not None:
            self.amount_each = amount_each
        if amount_ex_vat is not None:
            self.amount_ex_vat = amount_ex_vat
        if description is not None:
            self.description = description
        if quantity is not None:
            self.quantity = quantity
        if sku is not None:
            self.sku = sku
        if title is not None:
            self.title = title
        if vat_amount is not None:
            self.vat_amount = vat_amount
        if vat_code is not None:
            self.vat_code = vat_code
        if vat_percentage is not None:
            self.vat_percentage = vat_percentage

    @property
    def amount(self):
        """Gets the amount of this ReceiptLineItemItem.  # noqa: E501

        The total amount of this lineitem, in cents.  # noqa: E501

        :return: The amount of this ReceiptLineItemItem.  # noqa: E501
        :rtype: int
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this ReceiptLineItemItem.

        The total amount of this lineitem, in cents.  # noqa: E501

        :param amount: The amount of this ReceiptLineItemItem.  # noqa: E501
        :type: int
        """

        self._amount = amount

    @property
    def amount_each(self):
        """Gets the amount_each of this ReceiptLineItemItem.  # noqa: E501

        The amount per product of this lineitem, in cents. If quantity is 1, this amount is equal to the 'amount' field.  # noqa: E501

        :return: The amount_each of this ReceiptLineItemItem.  # noqa: E501
        :rtype: int
        """
        return self._amount_each

    @amount_each.setter
    def amount_each(self, amount_each):
        """Sets the amount_each of this ReceiptLineItemItem.

        The amount per product of this lineitem, in cents. If quantity is 1, this amount is equal to the 'amount' field.  # noqa: E501

        :param amount_each: The amount_each of this ReceiptLineItemItem.  # noqa: E501
        :type: int
        """

        self._amount_each = amount_each

    @property
    def amount_ex_vat(self):
        """Gets the amount_ex_vat of this ReceiptLineItemItem.  # noqa: E501

        THe total amount of this lineitem in cents, excluding VAT.  # noqa: E501

        :return: The amount_ex_vat of this ReceiptLineItemItem.  # noqa: E501
        :rtype: int
        """
        return self._amount_ex_vat

    @amount_ex_vat.setter
    def amount_ex_vat(self, amount_ex_vat):
        """Sets the amount_ex_vat of this ReceiptLineItemItem.

        THe total amount of this lineitem in cents, excluding VAT.  # noqa: E501

        :param amount_ex_vat: The amount_ex_vat of this ReceiptLineItemItem.  # noqa: E501
        :type: int
        """

        self._amount_ex_vat = amount_ex_vat

    @property
    def description(self):
        """Gets the description of this ReceiptLineItemItem.  # noqa: E501

        An additional description of the lineitem  # noqa: E501

        :return: The description of this ReceiptLineItemItem.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReceiptLineItemItem.

        An additional description of the lineitem  # noqa: E501

        :param description: The description of this ReceiptLineItemItem.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def quantity(self):
        """Gets the quantity of this ReceiptLineItemItem.  # noqa: E501

        The quantity of the products of the lineitem.  # noqa: E501

        :return: The quantity of this ReceiptLineItemItem.  # noqa: E501
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ReceiptLineItemItem.

        The quantity of the products of the lineitem.  # noqa: E501

        :param quantity: The quantity of this ReceiptLineItemItem.  # noqa: E501
        :type: float
        """

        self._quantity = quantity

    @property
    def sku(self):
        """Gets the sku of this ReceiptLineItemItem.  # noqa: E501


        :return: The sku of this ReceiptLineItemItem.  # noqa: E501
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this ReceiptLineItemItem.


        :param sku: The sku of this ReceiptLineItemItem.  # noqa: E501
        :type: str
        """

        self._sku = sku

    @property
    def title(self):
        """Gets the title of this ReceiptLineItemItem.  # noqa: E501

        The title of the lineitem  # noqa: E501

        :return: The title of this ReceiptLineItemItem.  # noqa: E501
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ReceiptLineItemItem.

        The title of the lineitem  # noqa: E501

        :param title: The title of this ReceiptLineItemItem.  # noqa: E501
        :type: str
        """

        self._title = title

    @property
    def vat_amount(self):
        """Gets the vat_amount of this ReceiptLineItemItem.  # noqa: E501

        The VAT amount, in cents  # noqa: E501

        :return: The vat_amount of this ReceiptLineItemItem.  # noqa: E501
        :rtype: int
        """
        return self._vat_amount

    @vat_amount.setter
    def vat_amount(self, vat_amount):
        """Sets the vat_amount of this ReceiptLineItemItem.

        The VAT amount, in cents  # noqa: E501

        :param vat_amount: The vat_amount of this ReceiptLineItemItem.  # noqa: E501
        :type: int
        """

        self._vat_amount = vat_amount

    @property
    def vat_code(self):
        """Gets the vat_code of this ReceiptLineItemItem.  # noqa: E501


        :return: The vat_code of this ReceiptLineItemItem.  # noqa: E501
        :rtype: str
        """
        return self._vat_code

    @vat_code.setter
    def vat_code(self, vat_code):
        """Sets the vat_code of this ReceiptLineItemItem.


        :param vat_code: The vat_code of this ReceiptLineItemItem.  # noqa: E501
        :type: str
        """

        self._vat_code = vat_code

    @property
    def vat_percentage(self):
        """Gets the vat_percentage of this ReceiptLineItemItem.  # noqa: E501

        The VAT percentage of this lineitem, in hundreds. For example, a percentage of \"21%\" is represented as 2100.  # noqa: E501

        :return: The vat_percentage of this ReceiptLineItemItem.  # noqa: E501
        :rtype: int
        """
        return self._vat_percentage

    @vat_percentage.setter
    def vat_percentage(self, vat_percentage):
        """Sets the vat_percentage of this ReceiptLineItemItem.

        The VAT percentage of this lineitem, in hundreds. For example, a percentage of \"21%\" is represented as 2100.  # noqa: E501

        :param vat_percentage: The vat_percentage of this ReceiptLineItemItem.  # noqa: E501
        :type: int
        """

        self._vat_percentage = vat_percentage

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
        if not isinstance(other, ReceiptLineItemItem):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReceiptLineItemItem):
            return True

        return self.to_dict() != other.to_dict()
