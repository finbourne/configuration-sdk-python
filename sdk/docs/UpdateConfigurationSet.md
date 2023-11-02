# UpdateConfigurationSet

The information required to update a configuration set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The new description of the configuration set | [optional] 

## Example

```python
from finbourne_configuration.models.update_configuration_set import UpdateConfigurationSet

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateConfigurationSet from a JSON string
update_configuration_set_instance = UpdateConfigurationSet.from_json(json)
# print the JSON string representation of the object
print UpdateConfigurationSet.to_json()

# convert the object into a dict
update_configuration_set_dict = update_configuration_set_instance.to_dict()
# create an instance of UpdateConfigurationSet from a dict
update_configuration_set_form_dict = update_configuration_set.from_dict(update_configuration_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


