# ConfigurationSetSummary

A group of configuration items

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | [**ResourceId**](ResourceId.md) |  | 
**type** | **str** | The type (personal or shared) of the configuration set | 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_configuration.models.configuration_set_summary import ConfigurationSetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ConfigurationSetSummary from a JSON string
configuration_set_summary_instance = ConfigurationSetSummary.from_json(json)
# print the JSON string representation of the object
print ConfigurationSetSummary.to_json()

# convert the object into a dict
configuration_set_summary_dict = configuration_set_summary_instance.to_dict()
# create an instance of ConfigurationSetSummary from a dict
configuration_set_summary_form_dict = configuration_set_summary.from_dict(configuration_set_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


