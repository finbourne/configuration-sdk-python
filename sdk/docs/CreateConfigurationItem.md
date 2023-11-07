# CreateConfigurationItem

The information required to create a configuration item

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the new configuration item | 
**value** | **str** | The value of the new configuration item                The maximum size for secrets is 4KB and for text values is 2MB | 
**value_type** | **str** | The type (text, number, boolean, textCollection, numberCollection) of the new configuration item&#39;s value.  The validation for each type is as follows:  - text: any value  - number: double (e.g. \&quot;5.5\&quot;)  - boolean: true/false  - textCollection: comma separated list (e.g. \&quot;a,b,c\&quot;)  - numberCollection: comma separated list of doubles (e.g. \&quot;1,2,3\&quot;) | [optional] 
**is_secret** | **bool** | Defines whether or not the value is a secret | 
**description** | **str** | The description of the new configuration item | [optional] 

## Example

```python
from lusid_configuration.models.create_configuration_item import CreateConfigurationItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConfigurationItem from a JSON string
create_configuration_item_instance = CreateConfigurationItem.from_json(json)
# print the JSON string representation of the object
print CreateConfigurationItem.to_json()

# convert the object into a dict
create_configuration_item_dict = create_configuration_item_instance.to_dict()
# create an instance of CreateConfigurationItem from a dict
create_configuration_item_form_dict = create_configuration_item.from_dict(create_configuration_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


