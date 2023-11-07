# CreateConfigurationSet

The information required to create a new configuration set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type (personal or shared) of the new configuration set | 
**description** | **str** | The description of the new configuration set | [optional] 

## Example

```python
from lusid_configuration.models.create_configuration_set import CreateConfigurationSet

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigurationSet from a JSON string
create_configuration_set_instance = CreateConfigurationSet.from_json(json)
# print the JSON string representation of the object
print CreateConfigurationSet.to_json()

# convert the object into a dict
create_configuration_set_dict = create_configuration_set_instance.to_dict()
# create an instance of CreateConfigurationSet from a dict
create_configuration_set_form_dict = create_configuration_set.from_dict(create_configuration_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


