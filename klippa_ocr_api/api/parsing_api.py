# coding: utf-8

"""
    Klippa Custom OCR API

    # Introduction The Klippa Custom OCR Webservice API is a REST webservice for custom OCR implementations by Klippa.  The service replies are JSON only.  The service base URL is https://custom-ocr.klippa.com/api/v1. The service base URL for the test environment is https://test.custom-ocr.klippa.com/api/v1, we test experimental templates and features there. It also hosts the demo interface.  # Authentication ## APIKeyHeader The API requires the following header to be set:  Header | Description | --- |--- |   X-Auth-Key  |  The auth key provided by Klippa. |  The Key is provided per customer by Klippa.  ## APIKeyQueryParam The key can also be provided in the request query as ```?X-Auth-Key=key```  ## APIPublicKeyHeader The Public API requires the following header to be set:  Header | Description | --- |--- |   X-Auth-Public-Key  |  The public auth key provided by Klippa. |  ## APIPublicKeyQueryParam The key can also be provided in the request query as ```?X-Auth-Public-Key=public-key```   # Calling the API from public applications If you want to call the API from a public application, like a mobile app, you should **NOT** embed your API key in the app, this key could be extracted and abused.  The way to do this is using our API to [generate a public key](#operation/createPublicKey) from your backend, and send that public key to your application. That way only users that are authenticated are allowed to call the API. That way you can also better monitor which users are using the API and prevent abuse. You can also configure the public key to be valid for a certain time and give a maximum amount of scans.  The public key API is not available for every API key, we have to enable this for you.  We also have a [complete scanner SDK for Android and iOS](https://www.klippa.com/en/ocr/ocr-sdk/) available that has this API integrated.  The Public API requires the following header to be set:  Header | Description | --- |--- |   X-Auth-Public-Key  |  The public auth key provided by Klippa. |  The key can also be provided in the request query as ```?X-Auth-Public-Key=public-key```   # API Client libraries  Language | Client | --- |--- |   Go  |   [go.tar.gz](/docs/static/clients/go.tar.gz) |   Java  |   [java.tar.gz](/docs/static/clients/java.tar.gz) |   PHP  |   [php.tar.gz](/docs/static/clients/php.tar.gz) |   Python  |   [python.tar.gz](/docs/static/clients/python.tar.gz) |   Typescript (Axios)  |   [typescript.tar.gz](/docs/static/clients/typescript.tar.gz) |   Swift 4  |   [swift4.tar.gz](/docs/static/clients/swift4.tar.gz) |   Swift 5  |   [swift5.tar.gz](/docs/static/clients/swift5.tar.gz) |   # Error codes ## Authentication errors  Code | Name | --- |--- |   100001  |   ErrorCodeAuthMissingKey |   100002  |   ErrorCodeAuthInvalidKey |   100003  |   ErrorCodeAuthError |   100004  |   ErrorCodeAuthNoCreditsLeft |   100005  |   ErrorCodeAuthInvalidPublicKey |   100006  |   ErrorCodeAuthPublicKeyNoScansLeft |   100007  |   ErrorCodeAuthPublicKeyExpired |   ## PDF Parser errors  Code | Name | --- |--- |   200001  |   ErrorCodePDFParserDocumentError |   200002  |   Obsolete |   200003  |   Obsolete |   200004  |   ErrorCodePDFParserNoAccessToTemplate |   200005  |   ErrorCodePDFParserConvertError |   200006  |   ErrorCodePDFParserParseError |   ## Document Parser errors  Code | Name | --- |--- |   300001  |   ErrorCodeDocumentParserDocumentError |   300002  |   Obsolete |   300003  |   Obsolete |   300004  |   ErrorCodeDocumentParserNoAccessToTemplate |   300005  |   ErrorCodeDocumentParserConvertError |   300006  |   ErrorCodeDocumentParserParseError |   300007  |   ErrorCodeDocumentParserTooBigFileError |   ## Public Key errors  Code | Name | --- |--- |   400001  |   ErrorCodePublicKeyNotAllowed |   400002  |   ErrorCodePublicKeyCreationFailed |   400003  |   ErrorCodePublicKeyInvalidScanLimit |   400004  |   ErrorCodePublicKeyInvalidValidTime |   400005  |   ErrorCodePublicKeyLoadError |   400006  |   ErrorCodePublicKeyNotFoundError |  # Userdata  The user_data field allows for sending additional data into the parser and can be used to enable extra features, improve the recognition of certain fields and improve the processing speed. The user_data must be given as a JSON-encoded string. All fields are optional, a documents may be submitted without this field.  The following fields are accepted in the user_data object:  Key | Value type  | Description | --|--|--| `client`| `Relation` object | A relation object containing information about the client that submits the document. It should contain information either the merchant of the customer of the invoice. This is indicated by the `transaction_type` key. If the `transaction_type` is set to `purchase`, the client is considered to be the customer. If the `transaction_type` is set to `sale`, the client is considered to be the merchant. `transaction_type`  | string  | The transaction type of the document for the client. If the invoices contains a sale that the client made, this field can be set to `sale`. If the invoice contains a purchase that the client made, this field can be set to `purchase`.| `relations`  | array of `Relation` objects  | An optional list of relations which have previously been used by the client. The list does not have to be complete, the OCR may suggest merchants and customers which are not in this list. | `transactions`  | array of `Transaction` objects  | An optional list of open transactions for the client. We use this list to validate and improve our OCR detections. | `purchase_orders`  | array of `PurchaseOrder` objects  | An optional list of purchase orders. It's identifier will be present in the output if the purchase order was found on the document | `locale`| `Locale` object | If the language or originating country of the document is known, these values may be set.   ## Relation object  The relation object may contain the following fields. All fields are optional and may be omitted if a field is not available. This user data can also be managed by [User Data Sets](#tag/UserDataSets) when allowed for your key.  Key | Value type  | Description | --|--|--| id|string|The ID of the relation in your own system, we will return this id in the `merchant_id` field if there is a match. In the User Data Set this is the ExternalID. name|string|The company name of the client street_name|string|The street name of the client address street_number|string|The street number of the client address zipcode|string|The zipcode of the client address city|string|The city of the client address country|string|The country of the client address. It must be provided as a 2-letter country code as specified by ISO 3166-1. For example `FR` for France and `NL` for The Netherlands vat_number|string|The vat number, formatted according to the EU VAT directive. It must start with the country code prefix, such as `FR` or `NL` coc_number|string|A chamber of commerce number. E.g. the Dutch KVK number, or the French SIRET/SIREN number phone|string|The phone number of the client. International calling codes, such as `+33` may be provided but are not required website|string|The full URL to the website email|string|The email address bank_account_number|string|The IBAN number   ## Transaction object  The transaction object may contain the following fields. All fields are optional and may be omitted if a field is not available. This user data can also be managed by [User Data Sets](#tag/UserDataSets) when allowed for your key.  Key | Value type  | Description | --|--|--| identifier|string|The identifier of the transaction as given by the bank date|string|The date of the transaction, in the format 2019-06-24 11:16:33 currency|string|The currency of the transaction, eg. EUR amount|float|The amount of the transaction, eg 23.56 description|string|The description of the transaction as given by the bank iban|string|The IBAN number that made the transaction name|string|The name of the bank account  ## PurchaseOrder object  The PurchaseOrder object may contain the following fields. The `date` and `amount` fields are optional. If given, the purchase order will only be searched for on the document if those fields match the document date and document total amount, respectively.  Key | Value type  | Description | --|--|--| identifier|string|The identifier of the purchase order purchase_order_number|string|The purchase order number which should be searched for on the document, e.g 'PO-12345' date|string|The expected document date, in the format 2019-06-24 11:16:33 amount|float|The expected total amount on the document, eg 23.56   ## Locale object In case the language and/or originating country of the document are known, these may be set in the locale object. The locale object may contain the following fields. Both fields are optional.  Key | Value type  | Description | --|--|--| language|string|A 2-letter language code according to ISO 3166-1. country|string|A 2-letter country code according to ISO 639.  ## Keyword and lineitem matching Keyword rules can be use to find strings in the text of the document using either a list of keywords or a regex.  Multiple rules may be given, each rule will provide a separate object in the output. All keywords and regexes are treated case-insensitive.  For example, by passing the following `keywords_rules` object, the regex will match all \"new product\" strings which are followed by a number. The matches are provided in the output in an object with \"id\" set to \"products\". The \"coupon\" rule can be used to count the number of occurrences of a list of words:  ``` { \"keyword_rules\": [ { \"id\": \"products\", \"regex\": \"(new product [0-9]+)\" }, { \"id\": \"coupon\", \"keywords\": [ \"coupon\" ] } ] } ```  If for example the keywords of \"products\" are matched 3 times in the text of the document, and the keywords of \"coupons\" 2 times, the output will be: ``` { \"matched_keywords\": [ { \"id\": \"products\", \"count\": 3 \"matches\": [\"new product 6\", \"new product 1\", \"new product 14\"] }, { \"id\": \"coupons\", \"count\": 2 \"matches\": [\"COUPON\", \"coupon\"] } ] } ```  ### Lineitem matching Similar to keyword rules, lineitems rules can be used to list products which contain a certain keyword. ``` { \"lineitem_rules\": [ { \"id\": \"fruit\", \"regex\": \"apple|banana\" }, { \"id\": \"vegetables\", \"keywords\": [ \"carrots\", \"broccoli\" ] } ] } ``` For example, if some of the lineitems on the document contain a word that is in the \"vegetables\" keyword list, they are of the present in the output under the \"vegetables\" key: ``` { \"matched_lineitems\": [ { \"id\": \"vegetables\", \"lineitems\": [ { \"title\": \"1kg carrots\", \"amount\": 164, \"amount_each\": 82, \"quantity\": 2 }, { \"title\": \"Set of 2 broccoli\", \"amount\": 164, \"amount_each\": 592, \"quantity\": 4 } ] } ] } ```  ## Userdata Example ``` { \"client\": { \"name\": \"\", \"street_name\": \"\", \"street_number\": \"\", \"zipcode\": \"\", \"city\": \"\", \"country\": \"\", \"vat_number\": \"\", \"coc_number\": \"\", \"phone\": \"\", \"website\": \"\", \"email\": \"\", \"bank_account_number\": \"\" }, \"transaction_type\": \"\", \"relations\": [ { \"name\": \"\", \"street_name\": \"\", \"street_number\": \"\", \"zipcode\": \"\", \"city\": \"\", \"country\": \"\", \"vat_number\": \"\", \"coc_number\": \"\", \"phone\": \"\", \"website\": \"\", \"email\": \"\", \"bank_account_number\": \"\" }, { \"name\": \"\", \"street_name\": \"\", \"street_number\": \"\", \"zipcode\": \"\", \"city\": \"\", \"country\": \"\", \"vat_number\": \"\", \"coc_number\": \"\", \"phone\": \"\", \"website\": \"\", \"email\": \"\", \"bank_account_number\": \"\" } ], \"locale\": { \"language\": \"\", \"country\": \"\" } } ```  # noqa: E501

    The version of the OpenAPI document: v0-15-56 - 1079148c9f913abee8defb181f6df7277de45506
    Contact: jeroen@klippa.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from klippa_ocr_api.api_client import ApiClient
from klippa_ocr_api.exceptions import (  # noqa: F401
    ApiTypeError,
    ApiValueError
)


class ParsingApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def parse_document(self, **kwargs):  # noqa: E501
        """Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.  # noqa: E501

        Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_document(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan.
        :param str url: The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan.
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str pdf_text_extraction: PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str user_data_set_external_id: The external ID of the user data set.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReceiptBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.parse_document_with_http_info(**kwargs)  # noqa: E501

    def parse_document_with_http_info(self, **kwargs):  # noqa: E501
        """Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.  # noqa: E501

        Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_document_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan.
        :param str url: The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan.
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str pdf_text_extraction: PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str user_data_set_external_id: The external ID of the user data set.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReceiptBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'document',
            'url',
            'template',
            'pdf_text_extraction',
            'user_data',
            'user_data_set_external_id',
            'hash_duplicate_group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method parse_document" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'document' in local_var_params:
            local_var_files['document'] = local_var_params['document']  # noqa: E501
        if 'url' in local_var_params:
            form_params.append(('url', local_var_params['url']))  # noqa: E501
        if 'template' in local_var_params:
            form_params.append(('template', local_var_params['template']))  # noqa: E501
        if 'pdf_text_extraction' in local_var_params:
            form_params.append(('pdf_text_extraction', local_var_params['pdf_text_extraction']))  # noqa: E501
        if 'user_data' in local_var_params:
            form_params.append(('user_data', local_var_params['user_data']))  # noqa: E501
        if 'user_data_set_external_id' in local_var_params:
            form_params.append(('user_data_set_external_id', local_var_params['user_data_set_external_id']))  # noqa: E501
        if 'hash_duplicate_group_id' in local_var_params:
            form_params.append(('hash_duplicate_group_id', local_var_params['hash_duplicate_group_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam', 'APIPublicKeyHeader', 'APIPublicKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/parseDocument', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReceiptBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def parse_document_eu_passport(self, **kwargs):  # noqa: E501
        """Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.  # noqa: E501

        Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_document_eu_passport(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan.
        :param str url: The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan.
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str pdf_text_extraction: PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str user_data_set_external_id: The external ID of the user data set.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: EuropeanPassportBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.parse_document_eu_passport_with_http_info(**kwargs)  # noqa: E501

    def parse_document_eu_passport_with_http_info(self, **kwargs):  # noqa: E501
        """Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.  # noqa: E501

        Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_document_eu_passport_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan.
        :param str url: The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan.
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str pdf_text_extraction: PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str user_data_set_external_id: The external ID of the user data set.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(EuropeanPassportBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'document',
            'url',
            'template',
            'pdf_text_extraction',
            'user_data',
            'user_data_set_external_id',
            'hash_duplicate_group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method parse_document_eu_passport" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'document' in local_var_params:
            local_var_files['document'] = local_var_params['document']  # noqa: E501
        if 'url' in local_var_params:
            form_params.append(('url', local_var_params['url']))  # noqa: E501
        if 'template' in local_var_params:
            form_params.append(('template', local_var_params['template']))  # noqa: E501
        if 'pdf_text_extraction' in local_var_params:
            form_params.append(('pdf_text_extraction', local_var_params['pdf_text_extraction']))  # noqa: E501
        if 'user_data' in local_var_params:
            form_params.append(('user_data', local_var_params['user_data']))  # noqa: E501
        if 'user_data_set_external_id' in local_var_params:
            form_params.append(('user_data_set_external_id', local_var_params['user_data_set_external_id']))  # noqa: E501
        if 'hash_duplicate_group_id' in local_var_params:
            form_params.append(('hash_duplicate_group_id', local_var_params['hash_duplicate_group_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam', 'APIPublicKeyHeader', 'APIPublicKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/parseDocument/eu-passport', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='EuropeanPassportBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def parse_document_identity_document(self, **kwargs):  # noqa: E501
        """Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.  # noqa: E501

        Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_document_identity_document(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan.
        :param str url: The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan.
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str pdf_text_extraction: PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str user_data_set_external_id: The external ID of the user data set.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: IdentityDocumentBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.parse_document_identity_document_with_http_info(**kwargs)  # noqa: E501

    def parse_document_identity_document_with_http_info(self, **kwargs):  # noqa: E501
        """Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.  # noqa: E501

        Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_document_identity_document_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan.
        :param str url: The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan.
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str pdf_text_extraction: PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str user_data_set_external_id: The external ID of the user data set.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(IdentityDocumentBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'document',
            'url',
            'template',
            'pdf_text_extraction',
            'user_data',
            'user_data_set_external_id',
            'hash_duplicate_group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method parse_document_identity_document" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'document' in local_var_params:
            local_var_files['document'] = local_var_params['document']  # noqa: E501
        if 'url' in local_var_params:
            form_params.append(('url', local_var_params['url']))  # noqa: E501
        if 'template' in local_var_params:
            form_params.append(('template', local_var_params['template']))  # noqa: E501
        if 'pdf_text_extraction' in local_var_params:
            form_params.append(('pdf_text_extraction', local_var_params['pdf_text_extraction']))  # noqa: E501
        if 'user_data' in local_var_params:
            form_params.append(('user_data', local_var_params['user_data']))  # noqa: E501
        if 'user_data_set_external_id' in local_var_params:
            form_params.append(('user_data_set_external_id', local_var_params['user_data_set_external_id']))  # noqa: E501
        if 'hash_duplicate_group_id' in local_var_params:
            form_params.append(('hash_duplicate_group_id', local_var_params['hash_duplicate_group_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam', 'APIPublicKeyHeader', 'APIPublicKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/parseDocument/identity', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='IdentityDocumentBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def parse_structured_pdf(self, document, **kwargs):  # noqa: E501
        """Parse a structured PDF file.  # noqa: E501

        Only use this when you are sure your PDF is plain text and not an image of a document.  Results in quicker / better parses in cases where the PDF only consists of plain text.  Body is the raw document file in the document field.  The template (when available) has to be given in the template value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_structured_pdf(document, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The passport document to scan as a multipart/form-data file. (required)
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReceiptBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.parse_structured_pdf_with_http_info(document, **kwargs)  # noqa: E501

    def parse_structured_pdf_with_http_info(self, document, **kwargs):  # noqa: E501
        """Parse a structured PDF file.  # noqa: E501

        Only use this when you are sure your PDF is plain text and not an image of a document.  Results in quicker / better parses in cases where the PDF only consists of plain text.  Body is the raw document file in the document field.  The template (when available) has to be given in the template value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_structured_pdf_with_http_info(document, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param file document: The passport document to scan as a multipart/form-data file. (required)
        :param str template: The template to use for parsing. Empty for default parsing.
        :param str user_data: Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data.
        :param str hash_duplicate_group_id: An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReceiptBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'document',
            'template',
            'user_data',
            'hash_duplicate_group_id'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method parse_structured_pdf" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'document' is set
        if self.api_client.client_side_validation and ('document' not in local_var_params or  # noqa: E501
                                                        local_var_params['document'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `document` when calling `parse_structured_pdf`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'document' in local_var_params:
            local_var_files['document'] = local_var_params['document']  # noqa: E501
        if 'template' in local_var_params:
            form_params.append(('template', local_var_params['template']))  # noqa: E501
        if 'user_data' in local_var_params:
            form_params.append(('user_data', local_var_params['user_data']))  # noqa: E501
        if 'hash_duplicate_group_id' in local_var_params:
            form_params.append(('hash_duplicate_group_id', local_var_params['hash_duplicate_group_id']))  # noqa: E501

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['multipart/form-data'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/parseStructuredPDF', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReceiptBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def parse_text(self, **kwargs):  # noqa: E501
        """Parse plain text.  # noqa: E501

        The template (when available) has to be given in the template property.  The output is not the same for every template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_text(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TextUploadForm body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: ReceiptBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.parse_text_with_http_info(**kwargs)  # noqa: E501

    def parse_text_with_http_info(self, **kwargs):  # noqa: E501
        """Parse plain text.  # noqa: E501

        The template (when available) has to be given in the template property.  The output is not the same for every template.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.parse_text_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param TextUploadForm body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(ReceiptBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'body'
        ]
        all_params.extend(
            [
                'async_req',
                '_return_http_data_only',
                '_preload_content',
                '_request_timeout'
            ]
        )

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method parse_text" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in local_var_params:
            body_params = local_var_params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/parseText', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ReceiptBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
