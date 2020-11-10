# TextUploadForm

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hash_duplicate_group_id** | **str** | An identifier to use when saving/detecting hash duplicates. This way you can allow to have the same document scanned more than once for multiple groups. When doing a scan, the combination of the Hash Group ID and the document Hash will be used to detect duplicates. This value is saved hashed on our side. Common use cases: Company ID, Campaign ID, User ID. In: formData | [optional] 
**template** | **str** |  | [optional] 
**text** | **str** |  | [optional] 
**user_data** | **str** | Extra metadata to give to the parser. Only works with templates that are configured to accept user data. | [optional] 
**user_data_set_external_id** | **str** | The external ID of the user data set. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


