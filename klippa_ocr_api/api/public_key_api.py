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


class PublicKeyApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def create_public_key(self, **kwargs):  # noqa: E501
        """Create a public key.  # noqa: E501

        The public key API is not available for every API key, we have to enable this for you.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_public_key(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePublicKeyForm body:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: CreatePublicKeyBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.create_public_key_with_http_info(**kwargs)  # noqa: E501

    def create_public_key_with_http_info(self, **kwargs):  # noqa: E501
        """Create a public key.  # noqa: E501

        The public key API is not available for every API key, we have to enable this for you.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_public_key_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param CreatePublicKeyForm body:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(CreatePublicKeyBody, status_code(int), headers(HTTPHeaderDict))
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
                    " to method create_public_key" % key
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
            '/publicKey', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreatePublicKeyBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def public_key_info(self, **kwargs):  # noqa: E501
        """Get information about the public key.  # noqa: E501

        This call can only be made with public key authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_key_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetPublicKeyInfoBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.public_key_info_with_http_info(**kwargs)  # noqa: E501

    def public_key_info_with_http_info(self, **kwargs):  # noqa: E501
        """Get information about the public key.  # noqa: E501

        This call can only be made with public key authentication.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_key_info_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetPublicKeyInfoBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
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
                    " to method public_key_info" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIPublicKeyHeader', 'APIPublicKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/publicKey', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPublicKeyInfoBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def public_key_info_by_id(self, public_key_id, **kwargs):  # noqa: E501
        """Get information about the public key by a public key ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_key_info_by_id(public_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str public_key_id: The ID of the public key. (required)
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: GetPublicKeyInfoBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.public_key_info_by_id_with_http_info(public_key_id, **kwargs)  # noqa: E501

    def public_key_info_by_id_with_http_info(self, public_key_id, **kwargs):  # noqa: E501
        """Get information about the public key by a public key ID.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_key_info_by_id_with_http_info(public_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str public_key_id: The ID of the public key. (required)
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(GetPublicKeyInfoBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'public_key_id'
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
                    " to method public_key_info_by_id" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'public_key_id' is set
        if self.api_client.client_side_validation and ('public_key_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['public_key_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `public_key_id` when calling `public_key_info_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'public_key_id' in local_var_params:
            path_params['PublicKeyID'] = local_var_params['public_key_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/publicKey/{PublicKeyID}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GetPublicKeyInfoBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def public_key_statistics(self, public_key_id, **kwargs):  # noqa: E501
        """Get API usage statistics for the public key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_key_statistics(public_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str public_key_id: The ID of the public key. (required)
        :param datetime date_min: The minimum date of the receipts.
        :param datetime date_max: The maximum date of the receipts.
        :param str granularity: The granularity of the stat.
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: PublicKeyStatisticsBody
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.public_key_statistics_with_http_info(public_key_id, **kwargs)  # noqa: E501

    def public_key_statistics_with_http_info(self, public_key_id, **kwargs):  # noqa: E501
        """Get API usage statistics for the public key.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.public_key_statistics_with_http_info(public_key_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param str public_key_id: The ID of the public key. (required)
        :param datetime date_min: The minimum date of the receipts.
        :param datetime date_max: The maximum date of the receipts.
        :param str granularity: The granularity of the stat.
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(PublicKeyStatisticsBody, status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = [
            'public_key_id',
            'date_min',
            'date_max',
            'granularity'
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
                    " to method public_key_statistics" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'public_key_id' is set
        if self.api_client.client_side_validation and ('public_key_id' not in local_var_params or  # noqa: E501
                                                        local_var_params['public_key_id'] is None):  # noqa: E501
            raise ApiValueError("Missing the required parameter `public_key_id` when calling `public_key_statistics`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'public_key_id' in local_var_params:
            path_params['PublicKeyID'] = local_var_params['public_key_id']  # noqa: E501

        query_params = []
        if 'date_min' in local_var_params and local_var_params['date_min'] is not None:  # noqa: E501
            query_params.append(('date_min', local_var_params['date_min']))  # noqa: E501
        if 'date_max' in local_var_params and local_var_params['date_max'] is not None:  # noqa: E501
            query_params.append(('date_max', local_var_params['date_max']))  # noqa: E501
        if 'granularity' in local_var_params and local_var_params['granularity'] is not None:  # noqa: E501
            query_params.append(('granularity', local_var_params['granularity']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['APIKeyHeader', 'APIKeyQueryParam']  # noqa: E501

        return self.api_client.call_api(
            '/publicKey/{PublicKeyID}/statistics', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PublicKeyStatisticsBody',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
