# ResourceListOfConfigurationSetSummary


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**values** | [**List[ConfigurationSetSummary]**](ConfigurationSetSummary.md) |  | 
**href** | **str** |  | [optional] 
**links** | [**List[Link]**](Link.md) |  | [optional] 
**next_page** | **str** |  | [optional] 
**previous_page** | **str** |  | [optional] 

## Example

```python
from finbourne_configuration.models.resource_list_of_configuration_set_summary import ResourceListOfConfigurationSetSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ResourceListOfConfigurationSetSummary from a JSON string
resource_list_of_configuration_set_summary_instance = ResourceListOfConfigurationSetSummary.from_json(json)
# print the JSON string representation of the object
print ResourceListOfConfigurationSetSummary.to_json()

# convert the object into a dict
resource_list_of_configuration_set_summary_dict = resource_list_of_configuration_set_summary_instance.to_dict()
# create an instance of ResourceListOfConfigurationSetSummary from a dict
resource_list_of_configuration_set_summary_form_dict = resource_list_of_configuration_set_summary.from_dict(resource_list_of_configuration_set_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


