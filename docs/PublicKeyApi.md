# klippa_ocr_api.PublicKeyApi

All URIs are relative to *https://custom-ocr.klippa.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_public_key**](PublicKeyApi.md#create_public_key) | **POST** /publicKey | Create a public key.
[**public_key_info**](PublicKeyApi.md#public_key_info) | **GET** /publicKey | Get information about the public key.
[**public_key_info_by_id**](PublicKeyApi.md#public_key_info_by_id) | **GET** /publicKey/{PublicKeyID} | Get information about the public key by a public key ID.
[**public_key_statistics**](PublicKeyApi.md#public_key_statistics) | **GET** /publicKey/{PublicKeyID}/statistics | Get API usage statistics for the public key.


# **create_public_key**
> CreatePublicKeyBody create_public_key(body=body)

Create a public key.

The public key API is not available for every API key, we have to enable this for you.

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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    body = klippa_ocr_api.CreatePublicKeyForm() # CreatePublicKeyForm |  (optional)

    try:
        # Create a public key.
        api_response = api_instance.create_public_key(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->create_public_key: %s\n" % e)
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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    body = klippa_ocr_api.CreatePublicKeyForm() # CreatePublicKeyForm |  (optional)

    try:
        # Create a public key.
        api_response = api_instance.create_public_key(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->create_public_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreatePublicKeyForm**](CreatePublicKeyForm.md)|  | [optional] 

### Return type

[**CreatePublicKeyBody**](CreatePublicKeyBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the new public key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_key_info**
> GetPublicKeyInfoBody public_key_info()

Get information about the public key.

This call can only be made with public key authentication.

### Example

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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    
    try:
        # Get information about the public key.
        api_response = api_instance.public_key_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->public_key_info: %s\n" % e)
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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    
    try:
        # Get information about the public key.
        api_response = api_instance.public_key_info()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->public_key_info: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GetPublicKeyInfoBody**](GetPublicKeyInfoBody.md)

### Authorization

[APIPublicKeyHeader](../README.md#APIPublicKeyHeader), [APIPublicKeyQueryParam](../README.md#APIPublicKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with public key details. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_key_info_by_id**
> GetPublicKeyInfoBody public_key_info_by_id(public_key_id)

Get information about the public key by a public key ID.

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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    public_key_id = 'public_key_id_example' # str | The ID of the public key.

    try:
        # Get information about the public key by a public key ID.
        api_response = api_instance.public_key_info_by_id(public_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->public_key_info_by_id: %s\n" % e)
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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    public_key_id = 'public_key_id_example' # str | The ID of the public key.

    try:
        # Get information about the public key by a public key ID.
        api_response = api_instance.public_key_info_by_id(public_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->public_key_info_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_key_id** | **str**| The ID of the public key. | 

### Return type

[**GetPublicKeyInfoBody**](GetPublicKeyInfoBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with public key details. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **public_key_statistics**
> PublicKeyStatisticsBody public_key_statistics(public_key_id, date_min=date_min, date_max=date_max, granularity=granularity)

Get API usage statistics for the public key.

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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    public_key_id = 'public_key_id_example' # str | The ID of the public key.
date_min = '2013-10-20T19:20:30+01:00' # datetime | The minimum date of the receipts. (optional)
date_max = '2013-10-20T19:20:30+01:00' # datetime | The maximum date of the receipts. (optional)
granularity = 'day' # str | The granularity of the stat. (optional) (default to 'day')

    try:
        # Get API usage statistics for the public key.
        api_response = api_instance.public_key_statistics(public_key_id, date_min=date_min, date_max=date_max, granularity=granularity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->public_key_statistics: %s\n" % e)
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
    api_instance = klippa_ocr_api.PublicKeyApi(api_client)
    public_key_id = 'public_key_id_example' # str | The ID of the public key.
date_min = '2013-10-20T19:20:30+01:00' # datetime | The minimum date of the receipts. (optional)
date_max = '2013-10-20T19:20:30+01:00' # datetime | The maximum date of the receipts. (optional)
granularity = 'day' # str | The granularity of the stat. (optional) (default to 'day')

    try:
        # Get API usage statistics for the public key.
        api_response = api_instance.public_key_statistics(public_key_id, date_min=date_min, date_max=date_max, granularity=granularity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PublicKeyApi->public_key_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **public_key_id** | **str**| The ID of the public key. | 
 **date_min** | **datetime**| The minimum date of the receipts. | [optional] 
 **date_max** | **datetime**| The maximum date of the receipts. | [optional] 
 **granularity** | **str**| The granularity of the stat. | [optional] [default to &#39;day&#39;]

### Return type

[**PublicKeyStatisticsBody**](PublicKeyStatisticsBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with statistics of the credit usage for a public key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

