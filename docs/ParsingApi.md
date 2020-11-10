# klippa_ocr_api.ParsingApi

All URIs are relative to *https://custom-ocr.klippa.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**parse_document**](ParsingApi.md#parse_document) | **POST** /parseDocument | Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
[**parse_document_eu_passport**](ParsingApi.md#parse_document_eu_passport) | **POST** /parseDocument/eu-passport | Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
[**parse_document_identity_document**](ParsingApi.md#parse_document_identity_document) | **POST** /parseDocument/identity | Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
[**parse_structured_pdf**](ParsingApi.md#parse_structured_pdf) | **POST** /parseStructuredPDF | Parse a structured PDF file.
[**parse_text**](ParsingApi.md#parse_text) | **POST** /parseText | Parse plain text.


# **parse_document**
> ReceiptBody parse_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)

Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.

Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan. (optional)
template = 'template_example' # str | The template to use for parsing. Empty for default parsing. (optional)
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document: %s\n" % e)
```

* Api Key Authentication (APIKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan. (optional)
template = 'template_example' # str | The template to use for parsing. Empty for default parsing. (optional)
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document: %s\n" % e)
```

* Api Key Authentication (APIPublicKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan. (optional)
template = 'template_example' # str | The template to use for parsing. Empty for default parsing. (optional)
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document: %s\n" % e)
```

* Api Key Authentication (APIPublicKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan. (optional)
template = 'template_example' # str | The template to use for parsing. Empty for default parsing. (optional)
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Financial (default): Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **file**| The document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. | [optional] 
 **url** | **str**| The document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a document at once. Every url is seen as 1 scan. | [optional] 
 **template** | **str**| The template to use for parsing. Empty for default parsing. | [optional] 
 **pdf_text_extraction** | **str**| PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. | [optional] [default to &#39;fast&#39;]
 **user_data** | **str**| Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. | [optional] 
 **user_data_set_external_id** | **str**| The external ID of the user data set. | [optional] 
 **hash_duplicate_group_id** | **str**| An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. | [optional] 

### Return type

[**ReceiptBody**](ReceiptBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam), [APIPublicKeyHeader](../README.md#APIPublicKeyHeader), [APIPublicKeyQueryParam](../README.md#APIPublicKeyQueryParam)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The parsed document with the default template. |  -  |
**400** | The serializable Error with extra data structure.  Used for any common for form validation errors. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_document_eu_passport**
> EuropeanPassportBody parse_document_eu_passport(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)

Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.

Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan. (optional)
template = 'eu-passport' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'eu-passport')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_eu_passport(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_eu_passport: %s\n" % e)
```

* Api Key Authentication (APIKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan. (optional)
template = 'eu-passport' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'eu-passport')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_eu_passport(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_eu_passport: %s\n" % e)
```

* Api Key Authentication (APIPublicKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan. (optional)
template = 'eu-passport' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'eu-passport')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_eu_passport(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_eu_passport: %s\n" % e)
```

* Api Key Authentication (APIPublicKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan. (optional)
template = 'eu-passport' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'eu-passport')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template EU Passport: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_eu_passport(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_eu_passport: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **file**| The passport document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a passport document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. | [optional] 
 **url** | **str**| The passport document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a passport document at once. Every url is seen as 1 scan. | [optional] 
 **template** | **str**| The template to use for parsing. Empty for default parsing. | [optional] [default to &#39;eu-passport&#39;]
 **pdf_text_extraction** | **str**| PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. | [optional] [default to &#39;fast&#39;]
 **user_data** | **str**| Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. | [optional] 
 **user_data_set_external_id** | **str**| The external ID of the user data set. | [optional] 
 **hash_duplicate_group_id** | **str**| An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. | [optional] 

### Return type

[**EuropeanPassportBody**](EuropeanPassportBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam), [APIPublicKeyHeader](../README.md#APIPublicKeyHeader), [APIPublicKeyQueryParam](../README.md#APIPublicKeyQueryParam)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The parsed document with the eu-passport template. |  -  |
**400** | The serializable Error with extra data structure.  Used for any common for form validation errors. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_document_identity_document**
> IdentityDocumentBody parse_document_identity_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)

Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.

Body is the raw document file in the ```document``` field. You can also give a URL in the ```url``` field to let the API download the file. Note: you need to either pass a document or a URL. The service accepts image (jpg/png/gif/heic/heif) and PDF files.  The template (when available) has to be given in the ```template``` value or in the query argument ```template```. The query overwrites the form value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan. (optional)
template = 'identity' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'identity')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_identity_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_identity_document: %s\n" % e)
```

* Api Key Authentication (APIKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan. (optional)
template = 'identity' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'identity')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_identity_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_identity_document: %s\n" % e)
```

* Api Key Authentication (APIPublicKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan. (optional)
template = 'identity' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'identity')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_identity_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_identity_document: %s\n" % e)
```

* Api Key Authentication (APIPublicKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Configure API key authorization: APIPublicKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Public-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Public-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. (optional)
url = 'url_example' # str | The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan. (optional)
template = 'identity' # str | The template to use for parsing. Empty for default parsing. (optional) (default to 'identity')
pdf_text_extraction = 'fast' # str | PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. (optional) (default to 'fast')
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
user_data_set_external_id = 'user_data_set_external_id_example' # str | The external ID of the user data set. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Template Identity Document: Parse GIF, PNG, JPG, HEIC/HEIF or PDF file.
        api_response = api_instance.parse_document_identity_document(document=document, url=url, template=template, pdf_text_extraction=pdf_text_extraction, user_data=user_data, user_data_set_external_id=user_data_set_external_id, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_document_identity_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **file**| The identity document to scan as a multipart/form-data file. You can add this key multiple times to scan multiple parts of a identity document at once. If you are calling this method using JSON, the document field allows you to send a base64 string or an array of base64 strings for multiple files. Every file is seen as 1 scan. | [optional] 
 **url** | **str**| The identity document to scan as a file available at this URL. The request should be completed within 30 seconds. You can add this key multiple times to scan multiple parts of a identity document at once. Every url is seen as 1 scan. | [optional] 
 **template** | **str**| The template to use for parsing. Empty for default parsing. | [optional] [default to &#39;identity&#39;]
 **pdf_text_extraction** | **str**| PDF Text extraction. Use full when you want the best quality scan, use fast when you want fast scan results. Fast will try to extract the text from the PDF. Full will actually scan the full PDF, which is slower. Speed difference: full: ~5s, fast: ~2.5. When a PDF does not contain text, e.g., scans of documents and pictures, we will automatically use full for that request. This value is ignored for non-PDF requests. | [optional] [default to &#39;fast&#39;]
 **user_data** | **str**| Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. | [optional] 
 **user_data_set_external_id** | **str**| The external ID of the user data set. | [optional] 
 **hash_duplicate_group_id** | **str**| An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. | [optional] 

### Return type

[**IdentityDocumentBody**](IdentityDocumentBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam), [APIPublicKeyHeader](../README.md#APIPublicKeyHeader), [APIPublicKeyQueryParam](../README.md#APIPublicKeyQueryParam)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The parsed document with the identity_document template. |  -  |
**400** | The serializable Error with extra data structure.  Used for any common for form validation errors. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_structured_pdf**
> ReceiptBody parse_structured_pdf(document, template=template, user_data=user_data, hash_duplicate_group_id=hash_duplicate_group_id)

Parse a structured PDF file.

Only use this when you are sure your PDF is plain text and not an image of a document.  Results in quicker / better parses in cases where the PDF only consists of plain text.  Body is the raw document file in the document field.  The template (when available) has to be given in the template value.  The output is not the same for every template.  Note: ***this request is in multipart/form-data***.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The passport document to scan as a multipart/form-data file.
template = 'template_example' # str | The template to use for parsing. Empty for default parsing. (optional)
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Parse a structured PDF file.
        api_response = api_instance.parse_structured_pdf(document, template=template, user_data=user_data, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_structured_pdf: %s\n" % e)
```

* Api Key Authentication (APIKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    document = '/path/to/file' # file | The passport document to scan as a multipart/form-data file.
template = 'template_example' # str | The template to use for parsing. Empty for default parsing. (optional)
user_data = 'user_data_example' # str | Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. (optional)
hash_duplicate_group_id = 'hash_duplicate_group_id_example' # str | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. (optional)

    try:
        # Parse a structured PDF file.
        api_response = api_instance.parse_structured_pdf(document, template=template, user_data=user_data, hash_duplicate_group_id=hash_duplicate_group_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_structured_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document** | **file**| The passport document to scan as a multipart/form-data file. | 
 **template** | **str**| The template to use for parsing. Empty for default parsing. | [optional] 
 **user_data** | **str**| Extra metadata in JSON format to give to the parser. Only works with templates that are configured to accept user data. | [optional] 
 **hash_duplicate_group_id** | **str**| An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. | [optional] 

### Return type

[**ReceiptBody**](ReceiptBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The parsed PDF. |  -  |
**400** | The serializable Error with extra data structure.  Used for any common for form validation errors. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_text**
> ReceiptBody parse_text(body=body)

Parse plain text.

The template (when available) has to be given in the template property.  The output is not the same for every template.

### Example

* Api Key Authentication (APIKeyHeader):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    body = klippa_ocr_api.TextUploadForm() # TextUploadForm |  (optional)

    try:
        # Parse plain text.
        api_response = api_instance.parse_text(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_text: %s\n" % e)
```

* Api Key Authentication (APIKeyQueryParam):
```python
from __future__ import print_function
import time
import klippa_ocr_api
from klippa_ocr_api.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to https://custom-ocr.klippa.com/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: APIKeyHeader
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Configure API key authorization: APIKeyQueryParam
configuration = klippa_ocr_api.Configuration(
    host = "https://custom-ocr.klippa.com/api/v1",
    api_key = {
        'X-Auth-Key': 'YOUR_API_KEY'
    }
)
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Auth-Key'] = 'Bearer'

# Enter a context with an instance of the API client
with klippa_ocr_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = klippa_ocr_api.ParsingApi(api_client)
    body = klippa_ocr_api.TextUploadForm() # TextUploadForm |  (optional)

    try:
        # Parse plain text.
        api_response = api_instance.parse_text(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ParsingApi->parse_text: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TextUploadForm**](TextUploadForm.md)|  | [optional] 

### Return type

[**ReceiptBody**](ReceiptBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The parsed text. |  -  |
**400** | The serializable Error with extra data structure.  Used for any common for form validation errors. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

