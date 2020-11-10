# BulkUserDataSetRecordResult

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str** | The action that was performed. | [optional] 
**external_id** | **str** | The ID on the external user record this data set belongs to. | [optional] 
**failure_code** | **int** | The code when Result is failure. 1: internal error 2: item exists (when doing a create) 3: item does not exist (when doing update or delete) | [optional] 
**failure_message** | **str** | The message when Result is failure. | [optional] 
**item** | [**UserDataSetRecord**](UserDataSetRecord.md) |  | [optional] 
**result** | **str** | The result of the action. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


