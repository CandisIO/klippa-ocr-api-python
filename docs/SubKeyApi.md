# klippa_ocr_api.SubKeyApi

All URIs are relative to *https://custom-ocr.klippa.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sub_key**](SubKeyApi.md#create_sub_key) | **POST** /subKey | Create a sub key.
[**delete_sub_key**](SubKeyApi.md#delete_sub_key) | **DELETE** /subKey/{SubKeyID} | Delete the sub key.
[**get_sub_key**](SubKeyApi.md#get_sub_key) | **GET** /subKey/{SubKeyID} | Get the sub key.
[**sub_key_list**](SubKeyApi.md#sub_key_list) | **GET** /subKey | Get a list of sub keys.
[**sub_key_statistics**](SubKeyApi.md#sub_key_statistics) | **GET** /subKey/{SubKeyID}/statistics | Get API usage statistics for the sub key.
[**update_sub_key**](SubKeyApi.md#update_sub_key) | **PATCH** /subKey/{SubKeyID} | Update the sub key.


# **create_sub_key**
> CreateSubKeyBody create_sub_key(body=body)

Create a sub key.

The sub key API is not available for every API key, we have to enable this for you.

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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    body = klippa_ocr_api.SubKeyForm() # SubKeyForm |  (optional)

    try:
        # Create a sub key.
        api_response = api_instance.create_sub_key(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->create_sub_key: %s\n" % e)
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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    body = klippa_ocr_api.SubKeyForm() # SubKeyForm |  (optional)

    try:
        # Create a sub key.
        api_response = api_instance.create_sub_key(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->create_sub_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SubKeyForm**](SubKeyForm.md)|  | [optional] 

### Return type

[**CreateSubKeyBody**](CreateSubKeyBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the new key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sub_key**
> DeleteSubKeyBody delete_sub_key(sub_key_id)

Delete the sub key.

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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.

    try:
        # Delete the sub key.
        api_response = api_instance.delete_sub_key(sub_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->delete_sub_key: %s\n" % e)
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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.

    try:
        # Delete the sub key.
        api_response = api_instance.delete_sub_key(sub_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->delete_sub_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_key_id** | **str**| The ID of the sub key. | 

### Return type

[**DeleteSubKeyBody**](DeleteSubKeyBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response about the deleted sub key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sub_key**
> GetSubKeyBody get_sub_key(sub_key_id)

Get the sub key.

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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.

    try:
        # Get the sub key.
        api_response = api_instance.get_sub_key(sub_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->get_sub_key: %s\n" % e)
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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.

    try:
        # Get the sub key.
        api_response = api_instance.get_sub_key(sub_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->get_sub_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_key_id** | **str**| The ID of the sub key. | 

### Return type

[**GetSubKeyBody**](GetSubKeyBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the sub key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_key_list**
> SubKeyListBody sub_key_list(per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field)

Get a list of sub keys.

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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    per_page = 10 # int | The amount of results per page. (optional) (default to 10)
page = 1 # int | The page to load. (optional) (default to 1)
sort_order = 'ASC' # str | The order to sort. (optional) (default to 'ASC')
sort_field = 'CreatedAt' # str | The field to sort on. (optional) (default to 'CreatedAt')

    try:
        # Get a list of sub keys.
        api_response = api_instance.sub_key_list(per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->sub_key_list: %s\n" % e)
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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    per_page = 10 # int | The amount of results per page. (optional) (default to 10)
page = 1 # int | The page to load. (optional) (default to 1)
sort_order = 'ASC' # str | The order to sort. (optional) (default to 'ASC')
sort_field = 'CreatedAt' # str | The field to sort on. (optional) (default to 'CreatedAt')

    try:
        # Get a list of sub keys.
        api_response = api_instance.sub_key_list(per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->sub_key_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The amount of results per page. | [optional] [default to 10]
 **page** | **int**| The page to load. | [optional] [default to 1]
 **sort_order** | **str**| The order to sort. | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| The field to sort on. | [optional] [default to &#39;CreatedAt&#39;]

### Return type

[**SubKeyListBody**](SubKeyListBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with sub key details. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_key_statistics**
> SubKeyStatisticsBody sub_key_statistics(sub_key_id, date_min=date_min, date_max=date_max, granularity=granularity)

Get API usage statistics for the sub key.

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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.
date_min = '2013-10-20T19:20:30+01:00' # datetime | The minimum date of the receipts. (optional)
date_max = '2013-10-20T19:20:30+01:00' # datetime | The maximum date of the receipts. (optional)
granularity = 'day' # str | The granularity of the stat. (optional) (default to 'day')

    try:
        # Get API usage statistics for the sub key.
        api_response = api_instance.sub_key_statistics(sub_key_id, date_min=date_min, date_max=date_max, granularity=granularity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->sub_key_statistics: %s\n" % e)
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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.
date_min = '2013-10-20T19:20:30+01:00' # datetime | The minimum date of the receipts. (optional)
date_max = '2013-10-20T19:20:30+01:00' # datetime | The maximum date of the receipts. (optional)
granularity = 'day' # str | The granularity of the stat. (optional) (default to 'day')

    try:
        # Get API usage statistics for the sub key.
        api_response = api_instance.sub_key_statistics(sub_key_id, date_min=date_min, date_max=date_max, granularity=granularity)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->sub_key_statistics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_key_id** | **str**| The ID of the sub key. | 
 **date_min** | **datetime**| The minimum date of the receipts. | [optional] 
 **date_max** | **datetime**| The maximum date of the receipts. | [optional] 
 **granularity** | **str**| The granularity of the stat. | [optional] [default to &#39;day&#39;]

### Return type

[**SubKeyStatisticsBody**](SubKeyStatisticsBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with statistics of the credit usage for a sub key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sub_key**
> UpdateSubKeyBody update_sub_key(sub_key_id)

Update the sub key.

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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.

    try:
        # Update the sub key.
        api_response = api_instance.update_sub_key(sub_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->update_sub_key: %s\n" % e)
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
    api_instance = klippa_ocr_api.SubKeyApi(api_client)
    sub_key_id = 'sub_key_id_example' # str | The ID of the sub key.

    try:
        # Update the sub key.
        api_response = api_instance.update_sub_key(sub_key_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SubKeyApi->update_sub_key: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sub_key_id** | **str**| The ID of the sub key. | 

### Return type

[**UpdateSubKeyBody**](UpdateSubKeyBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the updated sub key. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

