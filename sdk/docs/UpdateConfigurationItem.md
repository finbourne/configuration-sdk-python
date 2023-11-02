# UpdateConfigurationItem

The information required to update a configuration item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The new value of the configuration item | 
**description** | **str** | The new description of the configuration item | [optional] 

## Example

```python
from finbourne_configuration.models.update_configuration_item import UpdateConfigurationItem

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigurationItem from a JSON string
update_configuration_item_instance = UpdateConfigurationItem.from_json(json)
# print the JSON string representation of the object
print UpdateConfigurationItem.to_json()

# convert the object into a dict
update_configuration_item_dict = update_configuration_item_instance.to_dict()
# create an instance of UpdateConfigurationItem from a dict
update_configuration_item_form_dict = update_configuration_item.from_dict(update_configuration_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


