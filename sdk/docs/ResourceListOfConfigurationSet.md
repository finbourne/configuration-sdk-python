# ResourceListOfConfigurationSet


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ConfigurationSet]**](ConfigurationSet.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from lusid_configuration.models.resource_list_of_configuration_set import ResourceListOfConfigurationSet

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfConfigurationSet from a JSON string
resource_list_of_configuration_set_instance = ResourceListOfConfigurationSet.from_json(json)
# print the JSON string representation of the object
print ResourceListOfConfigurationSet.to_json()

# convert the object into a dict
resource_list_of_configuration_set_dict = resource_list_of_configuration_set_instance.to_dict()
# create an instance of ResourceListOfConfigurationSet from a dict
resource_list_of_configuration_set_form_dict = resource_list_of_configuration_set.from_dict(resource_list_of_configuration_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


