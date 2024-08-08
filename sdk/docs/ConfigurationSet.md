# ConfigurationSet

The full version of the configuration set

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date referring to the creation date of the configuration set | 
**created_by** | **str** | Who created the configuration set | 
**last_modified_at** | **datetime** | The date referring to the date when the configuration set was last modified | 
**last_modified_by** | **str** | Who modified the configuration set most recently | 
**description** | **str** | Describes the configuration set | [optional] 
**items** | [**List[ConfigurationItemSummary]**](ConfigurationItemSummary.md) | The collection of the configuration items that this set contains. | [optional] 
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type (personal or shared) of the configuration set | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_configuration.models.configuration_set import ConfigurationSet

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationSet from a JSON string
configuration_set_instance = ConfigurationSet.from_json(json)
# print the JSON string representation of the object
print ConfigurationSet.to_json()

# convert the object into a dict
configuration_set_dict = configuration_set_instance.to_dict()
# create an instance of ConfigurationSet from a dict
configuration_set_form_dict = configuration_set.from_dict(configuration_set_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


