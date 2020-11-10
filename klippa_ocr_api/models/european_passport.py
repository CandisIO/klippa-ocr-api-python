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


class EuropeanPassport(object):
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
        'authority': 'str',
        'date_of_birth': 'str',
        'date_of_expiry': 'str',
        'date_of_issue': 'str',
        'document_code': 'str',
        'document_number': 'str',
        'document_type': 'str',
        'gender': 'str',
        'given_names': 'str',
        'height': 'str',
        'issuing_country': 'str',
        'nationality': 'str',
        'personal_number': 'str',
        'place_of_birth': 'str',
        'raw_text': 'str',
        'surname': 'str'
    }

    attribute_map = {
        'authority': 'authority',
        'date_of_birth': 'date_of_birth',
        'date_of_expiry': 'date_of_expiry',
        'date_of_issue': 'date_of_issue',
        'document_code': 'document_code',
        'document_number': 'document_number',
        'document_type': 'document_type',
        'gender': 'gender',
        'given_names': 'given_names',
        'height': 'height',
        'issuing_country': 'issuing_country',
        'nationality': 'nationality',
        'personal_number': 'personal_number',
        'place_of_birth': 'place_of_birth',
        'raw_text': 'raw_text',
        'surname': 'surname'
    }

    def __init__(self, authority=None, date_of_birth=None, date_of_expiry=None, date_of_issue=None, document_code=None, document_number=None, document_type=None, gender=None, given_names=None, height=None, issuing_country=None, nationality=None, personal_number=None, place_of_birth=None, raw_text=None, surname=None, local_vars_configuration=None):  # noqa: E501
        """EuropeanPassport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._authority = None
        self._date_of_birth = None
        self._date_of_expiry = None
        self._date_of_issue = None
        self._document_code = None
        self._document_number = None
        self._document_type = None
        self._gender = None
        self._given_names = None
        self._height = None
        self._issuing_country = None
        self._nationality = None
        self._personal_number = None
        self._place_of_birth = None
        self._raw_text = None
        self._surname = None
        self.discriminator = None

        if authority is not None:
            self.authority = authority
        if date_of_birth is not None:
            self.date_of_birth = date_of_birth
        if date_of_expiry is not None:
            self.date_of_expiry = date_of_expiry
        if date_of_issue is not None:
            self.date_of_issue = date_of_issue
        if document_code is not None:
            self.document_code = document_code
        if document_number is not None:
            self.document_number = document_number
        if document_type is not None:
            self.document_type = document_type
        if gender is not None:
            self.gender = gender
        if given_names is not None:
            self.given_names = given_names
        if height is not None:
            self.height = height
        if issuing_country is not None:
            self.issuing_country = issuing_country
        if nationality is not None:
            self.nationality = nationality
        if personal_number is not None:
            self.personal_number = personal_number
        if place_of_birth is not None:
            self.place_of_birth = place_of_birth
        if raw_text is not None:
            self.raw_text = raw_text
        if surname is not None:
            self.surname = surname

    @property
    def authority(self):
        """Gets the authority of this EuropeanPassport.  # noqa: E501


        :return: The authority of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._authority

    @authority.setter
    def authority(self, authority):
        """Sets the authority of this EuropeanPassport.


        :param authority: The authority of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._authority = authority

    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this EuropeanPassport.  # noqa: E501


        :return: The date_of_birth of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this EuropeanPassport.


        :param date_of_birth: The date_of_birth of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._date_of_birth = date_of_birth

    @property
    def date_of_expiry(self):
        """Gets the date_of_expiry of this EuropeanPassport.  # noqa: E501


        :return: The date_of_expiry of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._date_of_expiry

    @date_of_expiry.setter
    def date_of_expiry(self, date_of_expiry):
        """Sets the date_of_expiry of this EuropeanPassport.


        :param date_of_expiry: The date_of_expiry of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._date_of_expiry = date_of_expiry

    @property
    def date_of_issue(self):
        """Gets the date_of_issue of this EuropeanPassport.  # noqa: E501


        :return: The date_of_issue of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._date_of_issue

    @date_of_issue.setter
    def date_of_issue(self, date_of_issue):
        """Sets the date_of_issue of this EuropeanPassport.


        :param date_of_issue: The date_of_issue of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._date_of_issue = date_of_issue

    @property
    def document_code(self):
        """Gets the document_code of this EuropeanPassport.  # noqa: E501


        :return: The document_code of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._document_code

    @document_code.setter
    def document_code(self, document_code):
        """Sets the document_code of this EuropeanPassport.


        :param document_code: The document_code of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._document_code = document_code

    @property
    def document_number(self):
        """Gets the document_number of this EuropeanPassport.  # noqa: E501


        :return: The document_number of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._document_number

    @document_number.setter
    def document_number(self, document_number):
        """Sets the document_number of this EuropeanPassport.


        :param document_number: The document_number of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._document_number = document_number

    @property
    def document_type(self):
        """Gets the document_type of this EuropeanPassport.  # noqa: E501

        European Passport.  # noqa: E501

        :return: The document_type of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._document_type

    @document_type.setter
    def document_type(self, document_type):
        """Sets the document_type of this EuropeanPassport.

        European Passport.  # noqa: E501

        :param document_type: The document_type of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._document_type = document_type

    @property
    def gender(self):
        """Gets the gender of this EuropeanPassport.  # noqa: E501


        :return: The gender of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this EuropeanPassport.


        :param gender: The gender of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._gender = gender

    @property
    def given_names(self):
        """Gets the given_names of this EuropeanPassport.  # noqa: E501


        :return: The given_names of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._given_names

    @given_names.setter
    def given_names(self, given_names):
        """Sets the given_names of this EuropeanPassport.


        :param given_names: The given_names of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._given_names = given_names

    @property
    def height(self):
        """Gets the height of this EuropeanPassport.  # noqa: E501


        :return: The height of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this EuropeanPassport.


        :param height: The height of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._height = height

    @property
    def issuing_country(self):
        """Gets the issuing_country of this EuropeanPassport.  # noqa: E501


        :return: The issuing_country of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._issuing_country

    @issuing_country.setter
    def issuing_country(self, issuing_country):
        """Sets the issuing_country of this EuropeanPassport.


        :param issuing_country: The issuing_country of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._issuing_country = issuing_country

    @property
    def nationality(self):
        """Gets the nationality of this EuropeanPassport.  # noqa: E501


        :return: The nationality of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._nationality

    @nationality.setter
    def nationality(self, nationality):
        """Sets the nationality of this EuropeanPassport.


        :param nationality: The nationality of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._nationality = nationality

    @property
    def personal_number(self):
        """Gets the personal_number of this EuropeanPassport.  # noqa: E501


        :return: The personal_number of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._personal_number

    @personal_number.setter
    def personal_number(self, personal_number):
        """Sets the personal_number of this EuropeanPassport.


        :param personal_number: The personal_number of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._personal_number = personal_number

    @property
    def place_of_birth(self):
        """Gets the place_of_birth of this EuropeanPassport.  # noqa: E501


        :return: The place_of_birth of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._place_of_birth

    @place_of_birth.setter
    def place_of_birth(self, place_of_birth):
        """Sets the place_of_birth of this EuropeanPassport.


        :param place_of_birth: The place_of_birth of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._place_of_birth = place_of_birth

    @property
    def raw_text(self):
        """Gets the raw_text of this EuropeanPassport.  # noqa: E501


        :return: The raw_text of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._raw_text

    @raw_text.setter
    def raw_text(self, raw_text):
        """Sets the raw_text of this EuropeanPassport.


        :param raw_text: The raw_text of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._raw_text = raw_text

    @property
    def surname(self):
        """Gets the surname of this EuropeanPassport.  # noqa: E501


        :return: The surname of this EuropeanPassport.  # noqa: E501
        :rtype: str
        """
        return self._surname

    @surname.setter
    def surname(self, surname):
        """Sets the surname of this EuropeanPassport.


        :param surname: The surname of this EuropeanPassport.  # noqa: E501
        :type: str
        """

        self._surname = surname

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
        if not isinstance(other, EuropeanPassport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, EuropeanPassport):
            return True

        return self.to_dict() != other.to_dict()
