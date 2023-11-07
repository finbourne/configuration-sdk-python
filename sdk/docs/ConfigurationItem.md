# ConfigurationItem

The full version of the configuration item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date referring to the creation date of the configuration item | 
**created_by** | **str** | Who created the configuration item | 
**last_modified_at** | **datetime** | The date referring to the date when the configuration item was last modified | 
**last_modified_by** | **str** | Who modified the configuration item most recently | 
**description** | **str** | Describes the configuration item | [optional] 
**key** | **str** | The key which identifies the configuration item | 
**value** | **str** | The value of the configuration item | 
**value_type** | **str** | The type of the configuration item&#39;s value | 
**is_secret** | **bool** | Defines whether or not the value is a secret. | 
**ref** | **str** | The reference to the configuration item | [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_configuration.models.configuration_item import ConfigurationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationItem from a JSON string
configuration_item_instance = ConfigurationItem.from_json(json)
# print the JSON string representation of the object
print ConfigurationItem.to_json()

# convert the object into a dict
configuration_item_dict = configuration_item_instance.to_dict()
# create an instance of ConfigurationItem from a dict
configuration_item_form_dict = configuration_item.from_dict(configuration_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


