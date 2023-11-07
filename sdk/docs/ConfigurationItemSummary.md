# ConfigurationItemSummary

A single configuration object

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key which identifies the configuration item | 
**value** | **str** | The value of the configuration item | 
**value_type** | **str** | The type of the configuration item&#39;s value | 
**is_secret** | **bool** | Defines whether or not the value is a secret. | 
**ref** | **str** | The reference to the configuration item | [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_configuration.models.configuration_item_summary import ConfigurationItemSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationItemSummary from a JSON string
configuration_item_summary_instance = ConfigurationItemSummary.from_json(json)
# print the JSON string representation of the object
print ConfigurationItemSummary.to_json()

# convert the object into a dict
configuration_item_summary_dict = configuration_item_summary_instance.to_dict()
# create an instance of ConfigurationItemSummary from a dict
configuration_item_summary_form_dict = configuration_item_summary.from_dict(configuration_item_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


