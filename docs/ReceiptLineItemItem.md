# ReceiptLineItemItem

A single lineitem. The amounts are in cents
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The total amount of this lineitem, in cents. | [optional] 
**amount_each** | **int** | The amount per product of this lineitem, in cents. If quantity is 1, this amount is equal to the &#39;amount&#39; field. | [optional] 
**amount_ex_vat** | **int** | THe total amount of this lineitem in cents, excluding VAT. | [optional] 
**description** | **str** | An additional description of the lineitem | [optional] 
**quantity** | **float** | The quantity of the products of the lineitem. | [optional] 
**sku** | **str** |  | [optional] 
**title** | **str** | The title of the lineitem | [optional] 
**vat_amount** | **int** | The VAT amount, in cents | [optional] 
**vat_code** | **str** |  | [optional] 
**vat_percentage** | **int** | The VAT percentage of this lineitem, in hundreds. For example, a percentage of \&quot;21%\&quot; is represented as 2100. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


