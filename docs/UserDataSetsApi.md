# klippa_ocr_api.UserDataSetsApi

All URIs are relative to *https://custom-ocr.klippa.com/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bulk_user_data_set_record**](UserDataSetsApi.md#bulk_user_data_set_record) | **POST** /userDataSet/{ID}/records/bulk | Bulk create/update/delete user data set record.
[**create_user_data_set**](UserDataSetsApi.md#create_user_data_set) | **POST** /userDataSet | Create a new user data set.
[**create_user_data_set_record**](UserDataSetsApi.md#create_user_data_set_record) | **POST** /userDataSet/{ID}/records | Create a new user data set record.
[**delete_user_data_set**](UserDataSetsApi.md#delete_user_data_set) | **DELETE** /userDataSet/{ID} | Delete user data set.
[**delete_user_data_set_record**](UserDataSetsApi.md#delete_user_data_set_record) | **DELETE** /userDataSet/{ID}/records/{RecordID} | Delete user data set record.
[**get_user_data_set**](UserDataSetsApi.md#get_user_data_set) | **GET** /userDataSet/{ID} | Get user data set.
[**get_user_data_set_record**](UserDataSetsApi.md#get_user_data_set_record) | **GET** /userDataSet/{ID}/records/{RecordID} | Get user data set record.
[**get_user_data_set_records**](UserDataSetsApi.md#get_user_data_set_records) | **GET** /userDataSet/{ID}/records | List user data set records.
[**get_user_data_sets**](UserDataSetsApi.md#get_user_data_sets) | **GET** /userDataSet | List user data sets.
[**update_user_data_set**](UserDataSetsApi.md#update_user_data_set) | **PATCH** /userDataSet/{ID} | Update user data set.
[**update_user_data_set_record**](UserDataSetsApi.md#update_user_data_set_record) | **PATCH** /userDataSet/{ID}/records/{RecordID} | Update user data set record.


# **bulk_user_data_set_record**
> BulkUserDataSetRecordBody bulk_user_data_set_record(id, body=body)

Bulk create/update/delete user data set record.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
body = klippa_ocr_api.BulkUserDataSetRecordForm() # BulkUserDataSetRecordForm |  (optional)

    try:
        # Bulk create/update/delete user data set record.
        api_response = api_instance.bulk_user_data_set_record(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->bulk_user_data_set_record: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
body = klippa_ocr_api.BulkUserDataSetRecordForm() # BulkUserDataSetRecordForm |  (optional)

    try:
        # Bulk create/update/delete user data set record.
        api_response = api_instance.bulk_user_data_set_record(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->bulk_user_data_set_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **body** | [**BulkUserDataSetRecordForm**](BulkUserDataSetRecordForm.md)|  | [optional] 

### Return type

[**BulkUserDataSetRecordBody**](BulkUserDataSetRecordBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data set. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_data_set**
> CreateUserDataSetResponseBody create_user_data_set(body=body)

Create a new user data set.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    body = klippa_ocr_api.CreateUserDataSetForm() # CreateUserDataSetForm |  (optional)

    try:
        # Create a new user data set.
        api_response = api_instance.create_user_data_set(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->create_user_data_set: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    body = klippa_ocr_api.CreateUserDataSetForm() # CreateUserDataSetForm |  (optional)

    try:
        # Create a new user data set.
        api_response = api_instance.create_user_data_set(body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->create_user_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateUserDataSetForm**](CreateUserDataSetForm.md)|  | [optional] 

### Return type

[**CreateUserDataSetResponseBody**](CreateUserDataSetResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data set. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_data_set_record**
> CreateUserDataSetRecordResponseBody create_user_data_set_record(id, body=body)

Create a new user data set record.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
body = klippa_ocr_api.CreateUserDataSetRecordForm() # CreateUserDataSetRecordForm |  (optional)

    try:
        # Create a new user data set record.
        api_response = api_instance.create_user_data_set_record(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->create_user_data_set_record: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
body = klippa_ocr_api.CreateUserDataSetRecordForm() # CreateUserDataSetRecordForm |  (optional)

    try:
        # Create a new user data set record.
        api_response = api_instance.create_user_data_set_record(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->create_user_data_set_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **body** | [**CreateUserDataSetRecordForm**](CreateUserDataSetRecordForm.md)|  | [optional] 

### Return type

[**CreateUserDataSetRecordResponseBody**](CreateUserDataSetRecordResponseBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data record. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_data_set**
> DeleteUserDataSetBody delete_user_data_set(id)

Delete user data set.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.

    try:
        # Delete user data set.
        api_response = api_instance.delete_user_data_set(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->delete_user_data_set: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.

    try:
        # Delete user data set.
        api_response = api_instance.delete_user_data_set(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->delete_user_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 

### Return type

[**DeleteUserDataSetBody**](DeleteUserDataSetBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with an empty body. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user_data_set_record**
> DeleteUserDataSetRecordBody delete_user_data_set_record(id, record_id)

Delete user data set record.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
record_id = 56 # int | The ID of the user data set record. To use the external ID, prefix the ID with E.

    try:
        # Delete user data set record.
        api_response = api_instance.delete_user_data_set_record(id, record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->delete_user_data_set_record: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
record_id = 56 # int | The ID of the user data set record. To use the external ID, prefix the ID with E.

    try:
        # Delete user data set record.
        api_response = api_instance.delete_user_data_set_record(id, record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->delete_user_data_set_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **record_id** | **int**| The ID of the user data set record. To use the external ID, prefix the ID with E. | 

### Return type

[**DeleteUserDataSetRecordBody**](DeleteUserDataSetRecordBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with an empty body. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_set**
> GetUserDataSetBody get_user_data_set(id)

Get user data set.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.

    try:
        # Get user data set.
        api_response = api_instance.get_user_data_set(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_set: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.

    try:
        # Get user data set.
        api_response = api_instance.get_user_data_set(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 

### Return type

[**GetUserDataSetBody**](GetUserDataSetBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data set. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_set_record**
> GetUserDataSetRecordBody get_user_data_set_record(id, record_id)

Get user data set record.

Note: we do not output the values of the record for privacy reasons.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
record_id = 56 # int | The ID of the user data set record. To use the external ID, prefix the ID with E.

    try:
        # Get user data set record.
        api_response = api_instance.get_user_data_set_record(id, record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_set_record: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
record_id = 56 # int | The ID of the user data set record. To use the external ID, prefix the ID with E.

    try:
        # Get user data set record.
        api_response = api_instance.get_user_data_set_record(id, record_id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_set_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **record_id** | **int**| The ID of the user data set record. To use the external ID, prefix the ID with E. | 

### Return type

[**GetUserDataSetRecordBody**](GetUserDataSetRecordBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data set. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_set_records**
> GetUserDataSetRecordsBody get_user_data_set_records(id, per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field, type=type, external_id=external_id, filter=filter)

List user data set records.

Note: we do not output the values of the record for privacy reasons.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
per_page = 10 # int | The amount of results per page. (optional) (default to 10)
page = 1 # int | The page to load. (optional) (default to 1)
sort_order = 'ASC' # str | The order to sort. (optional) (default to 'ASC')
sort_field = 'CreatedAt' # str | The field to sort on. (optional) (default to 'CreatedAt')
type = 'type_example' # str | The types to filter on. Separated by a comma. When no types are given, all types are returned. (optional)
external_id = 'external_id_example' # str | The external IDs to filter on. Separated by a comma. When no external IDs are given, items of all external ids are returned. (optional)
filter = 'filter_example' # str | A filter to use for the list. This query can be used multiple times.  Format is:  CreatedAt:{value}:{operator}  UpdatedAt:{value}:{operator}  ID:{value}:{operator}  ExternalID:{value}:{operator}  LastSyncDate:{value}:{operator}  {operator} is one of:  EQ (Equal)  NEQ (Not equal)  GT (Greater than)  GTE (Greater than or equal)  LT (Lower than)  LTE (Lower than or equal)  LIKE  NULL (value can be empty)  NOTNULL (value can be empty) (optional)

    try:
        # List user data set records.
        api_response = api_instance.get_user_data_set_records(id, per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field, type=type, external_id=external_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_set_records: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
per_page = 10 # int | The amount of results per page. (optional) (default to 10)
page = 1 # int | The page to load. (optional) (default to 1)
sort_order = 'ASC' # str | The order to sort. (optional) (default to 'ASC')
sort_field = 'CreatedAt' # str | The field to sort on. (optional) (default to 'CreatedAt')
type = 'type_example' # str | The types to filter on. Separated by a comma. When no types are given, all types are returned. (optional)
external_id = 'external_id_example' # str | The external IDs to filter on. Separated by a comma. When no external IDs are given, items of all external ids are returned. (optional)
filter = 'filter_example' # str | A filter to use for the list. This query can be used multiple times.  Format is:  CreatedAt:{value}:{operator}  UpdatedAt:{value}:{operator}  ID:{value}:{operator}  ExternalID:{value}:{operator}  LastSyncDate:{value}:{operator}  {operator} is one of:  EQ (Equal)  NEQ (Not equal)  GT (Greater than)  GTE (Greater than or equal)  LT (Lower than)  LTE (Lower than or equal)  LIKE  NULL (value can be empty)  NOTNULL (value can be empty) (optional)

    try:
        # List user data set records.
        api_response = api_instance.get_user_data_set_records(id, per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field, type=type, external_id=external_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_set_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **per_page** | **int**| The amount of results per page. | [optional] [default to 10]
 **page** | **int**| The page to load. | [optional] [default to 1]
 **sort_order** | **str**| The order to sort. | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| The field to sort on. | [optional] [default to &#39;CreatedAt&#39;]
 **type** | **str**| The types to filter on. Separated by a comma. When no types are given, all types are returned. | [optional] 
 **external_id** | **str**| The external IDs to filter on. Separated by a comma. When no external IDs are given, items of all external ids are returned. | [optional] 
 **filter** | **str**| A filter to use for the list. This query can be used multiple times.  Format is:  CreatedAt:{value}:{operator}  UpdatedAt:{value}:{operator}  ID:{value}:{operator}  ExternalID:{value}:{operator}  LastSyncDate:{value}:{operator}  {operator} is one of:  EQ (Equal)  NEQ (Not equal)  GT (Greater than)  GTE (Greater than or equal)  LT (Lower than)  LTE (Lower than or equal)  LIKE  NULL (value can be empty)  NOTNULL (value can be empty) | [optional] 

### Return type

[**GetUserDataSetRecordsBody**](GetUserDataSetRecordsBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data sets. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_data_sets**
> GetUserDataSetsBody get_user_data_sets(per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field, type=type, external_id=external_id, filter=filter)

List user data sets.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    per_page = 10 # int | The amount of results per page. (optional) (default to 10)
page = 1 # int | The page to load. (optional) (default to 1)
sort_order = 'ASC' # str | The order to sort. (optional) (default to 'ASC')
sort_field = 'CreatedAt' # str | The field to sort on. (optional) (default to 'CreatedAt')
type = 'type_example' # str | The types to filter on. Separated by a comma. When no types are given, all types are returned. (optional)
external_id = 'external_id_example' # str | The external IDs to filter on. Separated by a comma. When no external IDs are given, items of all external ids are returned. (optional)
filter = 'filter_example' # str | A filter to use for the list. This query can be used multiple times.  Format is:  CreatedAt:{value}:{operator}  UpdatedAt:{value}:{operator}  ID:{value}:{operator}  Type:{value}:{operator}  ExternalID:{value}:{operator}  LastSyncDate:{value}:{operator}  {operator} is one of:  EQ (Equal)  NEQ (Not equal)  GT (Greater than)  GTE (Greater than or equal)  LT (Lower than)  LTE (Lower than or equal)  LIKE  NULL (value can be empty)  NOTNULL (value can be empty) (optional)

    try:
        # List user data sets.
        api_response = api_instance.get_user_data_sets(per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field, type=type, external_id=external_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_sets: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    per_page = 10 # int | The amount of results per page. (optional) (default to 10)
page = 1 # int | The page to load. (optional) (default to 1)
sort_order = 'ASC' # str | The order to sort. (optional) (default to 'ASC')
sort_field = 'CreatedAt' # str | The field to sort on. (optional) (default to 'CreatedAt')
type = 'type_example' # str | The types to filter on. Separated by a comma. When no types are given, all types are returned. (optional)
external_id = 'external_id_example' # str | The external IDs to filter on. Separated by a comma. When no external IDs are given, items of all external ids are returned. (optional)
filter = 'filter_example' # str | A filter to use for the list. This query can be used multiple times.  Format is:  CreatedAt:{value}:{operator}  UpdatedAt:{value}:{operator}  ID:{value}:{operator}  Type:{value}:{operator}  ExternalID:{value}:{operator}  LastSyncDate:{value}:{operator}  {operator} is one of:  EQ (Equal)  NEQ (Not equal)  GT (Greater than)  GTE (Greater than or equal)  LT (Lower than)  LTE (Lower than or equal)  LIKE  NULL (value can be empty)  NOTNULL (value can be empty) (optional)

    try:
        # List user data sets.
        api_response = api_instance.get_user_data_sets(per_page=per_page, page=page, sort_order=sort_order, sort_field=sort_field, type=type, external_id=external_id, filter=filter)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->get_user_data_sets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **per_page** | **int**| The amount of results per page. | [optional] [default to 10]
 **page** | **int**| The page to load. | [optional] [default to 1]
 **sort_order** | **str**| The order to sort. | [optional] [default to &#39;ASC&#39;]
 **sort_field** | **str**| The field to sort on. | [optional] [default to &#39;CreatedAt&#39;]
 **type** | **str**| The types to filter on. Separated by a comma. When no types are given, all types are returned. | [optional] 
 **external_id** | **str**| The external IDs to filter on. Separated by a comma. When no external IDs are given, items of all external ids are returned. | [optional] 
 **filter** | **str**| A filter to use for the list. This query can be used multiple times.  Format is:  CreatedAt:{value}:{operator}  UpdatedAt:{value}:{operator}  ID:{value}:{operator}  Type:{value}:{operator}  ExternalID:{value}:{operator}  LastSyncDate:{value}:{operator}  {operator} is one of:  EQ (Equal)  NEQ (Not equal)  GT (Greater than)  GTE (Greater than or equal)  LT (Lower than)  LTE (Lower than or equal)  LIKE  NULL (value can be empty)  NOTNULL (value can be empty) | [optional] 

### Return type

[**GetUserDataSetsBody**](GetUserDataSetsBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data sets. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_data_set**
> UpdateUserDataSetBody update_user_data_set(id, body=body)

Update user data set.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
body = klippa_ocr_api.UpdateUserDataSetForm() # UpdateUserDataSetForm |  (optional)

    try:
        # Update user data set.
        api_response = api_instance.update_user_data_set(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->update_user_data_set: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
body = klippa_ocr_api.UpdateUserDataSetForm() # UpdateUserDataSetForm |  (optional)

    try:
        # Update user data set.
        api_response = api_instance.update_user_data_set(id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->update_user_data_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **body** | [**UpdateUserDataSetForm**](UpdateUserDataSetForm.md)|  | [optional] 

### Return type

[**UpdateUserDataSetBody**](UpdateUserDataSetBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data set. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user_data_set_record**
> UpdateUserDataSetRecordBody update_user_data_set_record(id, record_id, body=body)

Update user data set record.

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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
record_id = 56 # int | The ID of the user data set record. To use the external ID, prefix the ID with E.
body = klippa_ocr_api.UpdateUserDataSetRecordForm() # UpdateUserDataSetRecordForm |  (optional)

    try:
        # Update user data set record.
        api_response = api_instance.update_user_data_set_record(id, record_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->update_user_data_set_record: %s\n" % e)
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
    api_instance = klippa_ocr_api.UserDataSetsApi(api_client)
    id = 56 # int | The ID of the user data set. To use the external ID, prefix the ID with E-{type}-.
record_id = 56 # int | The ID of the user data set record. To use the external ID, prefix the ID with E.
body = klippa_ocr_api.UpdateUserDataSetRecordForm() # UpdateUserDataSetRecordForm |  (optional)

    try:
        # Update user data set record.
        api_response = api_instance.update_user_data_set_record(id, record_id, body=body)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling UserDataSetsApi->update_user_data_set_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The ID of the user data set. To use the external ID, prefix the ID with E-{type}-. | 
 **record_id** | **int**| The ID of the user data set record. To use the external ID, prefix the ID with E. | 
 **body** | [**UpdateUserDataSetRecordForm**](UpdateUserDataSetRecordForm.md)|  | [optional] 

### Return type

[**UpdateUserDataSetRecordBody**](UpdateUserDataSetRecordBody.md)

### Authorization

[APIKeyHeader](../README.md#APIKeyHeader), [APIKeyQueryParam](../README.md#APIKeyQueryParam)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Response with the user data set record. |  -  |
**500** | The serializable Error structure.  Used for any common errors. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

