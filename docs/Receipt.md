# Receipt

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **int** | The total amount, in cents | [optional] 
**amount_change** | **int** | The change amount, in cents | [optional] 
**amountexvat** | **int** | The total amount without vat, in cents | [optional] 
**barcodes** | [**list[Barcode]**](Barcode.md) | Barcodes that are found on the document | [optional] 
**currency** | **str** | The three-letter currency code, as defined in ISO 4217, e.g. &#x60;EUR&#x60; | [optional] 
**customer_address** | **str** | The address line of the customer, as written on the document | [optional] 
**customer_bank_account_number** | **str** | The IBAN number of the customer. | [optional] 
**customer_bank_account_number_bic** | **str** | The BIC associated with the IBAN number of the customer | [optional] 
**customer_city** | **str** |  | [optional] 
**customer_coc_number** | **str** | The chamber of commerce number of the customer | [optional] 
**customer_country** | **str** | The name of the country, as written on the document | [optional] 
**customer_email** | **str** |  | [optional] 
**customer_house_number** | **str** | The house number of the customer. It will only be set if the customer address could be split into a street name and house number | [optional] 
**customer_municipality** | **str** |  | [optional] 
**customer_name** | **str** | The name of the customer | [optional] 
**customer_number** | **str** | A number used by the merchant to identify the customer | [optional] 
**customer_phone** | **str** |  | [optional] 
**customer_province** | **str** |  | [optional] 
**customer_reference** | **str** | A reference to this document, given by the customer | [optional] 
**customer_street_name** | **str** | The street name of the customer. It will only be set if the customer address could be split into a street name and house number | [optional] 
**customer_vat_number** | **str** | The VAT number of the customer. It contains the two-letter country code, followed by a country-specific implementation of the VAT number. | [optional] 
**customer_website** | **str** |  | [optional] 
**customer_zipcode** | **str** | The zipcode of the customer. Dutch postcodes are formatted as 1234 AB | [optional] 
**date** | **str** | The purchase datetime as ISO string, E.g. &#x60;2019-07-01T16:46:00&#x60; | [optional] 
**document_language** | **str** | The language of the document as a two-letter country code | [optional] 
**document_subject** | **str** | The subject of the document | [optional] 
**document_type** | **str** |  | [optional] 
**hash** | **str** | Unique hash of the receipt. | [optional] 
**hash_duplicate** | **bool** | Whether we have seen the hash before for the current key. | [optional] 
**invoice_number** | **str** | The number of the invoice | [optional] 
**invoice_type** | **str** |  | [optional] 
**lines** | [**list[ReceiptLineItem]**](ReceiptLineItem.md) |  | [optional] 
**matched_keywords** | [**list[MatchedKeyword]**](MatchedKeyword.md) | If keywords have been given in the userdata, matched_keywords will contain the id&#39;s of the keywords that matched, and their number of occurrences. | [optional] 
**matched_lineitems** | [**list[MatchedLineItemsReceipt]**](MatchedLineItemsReceipt.md) | If keywords have been given for lineitems in the userdata, matched_lineitems will contain the id&#39;s of the keywords that matched, and the lineitems on which the matches were made. | [optional] 
**matched_purchase_order_id** | **str** | The id of the purchase order from the user data | [optional] 
**merchant_address** | **str** | The address line of the merchant, as written on the document | [optional] 
**merchant_bank_account_number** | **str** | The IBAN bank account number of the merchant. | [optional] 
**merchant_bank_account_number_bic** | **str** | The BIC associated with the IBAN bank account number of the merchant | [optional] 
**merchant_bank_domestic_account_number** | **str** | The domestic bank account number of the merchant | [optional] 
**merchant_bank_domestic_bank_code** | **str** | The domestic bank code of the bank account of the merchant | [optional] 
**merchant_chain_liability_bank_account_number** | **str** | The IBAN bank account number of the merchant used for Chain Liability G-Account (Wet Ketenaansprakelijkheid G-rekening) | [optional] 
**merchant_city** | **str** |  | [optional] 
**merchant_coc_number** | **str** | The chamber of commerce number of the merchant | [optional] 
**merchant_country** | **str** | The name of the country, as written on the document | [optional] 
**merchant_country_code** | **str** | The name of the country as two-letter country code | [optional] 
**merchant_email** | **str** |  | [optional] 
**merchant_house_number** | **str** | The house number of the merchant. It will only be set if the merchant address could be split into a street name and house number | [optional] 
**merchant_id** | **str** | The identifier of the merchant. It is only present if the merchant is found using a relation that was provided in the user_data object, or was provided in a user_data_set. | [optional] 
**merchant_main_activity_code** | **str** | The main activity code of the merchant | [optional] 
**merchant_municipality** | **str** |  | [optional] 
**merchant_name** | **str** | The name of the merchant | [optional] 
**merchant_phone** | **str** |  | [optional] 
**merchant_province** | **str** |  | [optional] 
**merchant_street_name** | **str** | The street name of the merchant. It will only be set if the merchant address could be split into a street name and house number | [optional] 
**merchant_vat_number** | **str** | The VAT number of the merchant. It contains the two-letter country code, followed by a country-specific implementation of the VAT number. | [optional] 
**merchant_website** | **str** |  | [optional] 
**merchant_zipcode** | **str** | The zipcode of the merchant. Dutch postcodes are formatted as 1234 AB | [optional] 
**order_number** | **str** | The order number | [optional] 
**package_number** | **str** | Package number, usually found on packaging slips | [optional] 
**payment_auth_code** | **str** | The transaction authorization code | [optional] 
**payment_card_account_number** | **str** | The account number of the card that was used to complete the payment | [optional] 
**payment_card_bank** | **str** |  | [optional] 
**payment_card_issuer** | **str** | Name of the party that issued the credit- or debit card | [optional] 
**payment_card_number** | **str** |  | [optional] 
**payment_due_date** | **str** | Date on which the payment is due as ISO string, E.g. &#x60;2019-07-01T00:00:00&#x60; | [optional] 
**payment_slip_code** | **str** | The full code of the payment slip | [optional] 
**payment_slip_customer_number** | **str** | The customer number of the payment slip | [optional] 
**payment_slip_reference_number** | **str** | The reference number of the payment slip | [optional] 
**paymentmethod** | **str** |  | [optional] 
**purchasedate** | **str** | The purchase date as &#x60;yyyy-mm-dd&#x60; string, e.g. &#x60;2019-07-01&#x60; | [optional] 
**purchasetime** | **str** | The purchase time as hh:mm:ss string, e.g. &#x60;16:46:00&#x60; | [optional] 
**raw_text** | **str** | Original plain text of receipt. | [optional] 
**receipt_number** | **str** | The receipt ticket number | [optional] 
**server** | **str** |  | [optional] 
**shop_number** | **str** | A number that identifies the store in which the payment was processed. Usually found on EFT receipts. | [optional] 
**table_group** | **str** |  | [optional] 
**table_number** | **str** |  | [optional] 
**terminal_number** | **str** | A number that identifies the terminal on which the payment was processed. Usually found on EFT receipts. | [optional] 
**transaction_number** | **str** | The transaction number provided by the payment processor. Usually found on EFT receipts. | [optional] 
**transaction_reference** | **str** | A transaction reference provided by the merchant | [optional] 
**vat_context** | **str** | enum ,purchase_none,vat_relayed In case no vat was found, the vat context field may indicate a reason why no vat was found | [optional] 
**vatamount** | **int** | The total VAT amount, in cents | [optional] 
**vatitems** | [**list[ReceiptVAT]**](ReceiptVAT.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


