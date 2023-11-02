# ResourceListOfConfigurationItem


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ConfigurationItem]**](ConfigurationItem.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_configuration.models.resource_list_of_configuration_item import ResourceListOfConfigurationItem

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfConfigurationItem from a JSON string
resource_list_of_configuration_item_instance = ResourceListOfConfigurationItem.from_json(json)
# print the JSON string representation of the object
print ResourceListOfConfigurationItem.to_json()

# convert the object into a dict
resource_list_of_configuration_item_dict = resource_list_of_configuration_item_instance.to_dict()
# create an instance of ResourceListOfConfigurationItem from a dict
resource_list_of_configuration_item_form_dict = resource_list_of_configuration_item.from_dict(resource_list_of_configuration_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


