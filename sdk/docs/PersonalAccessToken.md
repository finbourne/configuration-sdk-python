# PersonalAccessToken

Representation of a Personal Access Token under a Configuration Item format.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | Value of the Personal Access Token. | [readonly] 
**type** | **str** | The type of the Personal Access Token. | [readonly] 
**description** | **str** | The description of the Personal Access Token. | [readonly] 
**ref** | **str** | The reference to the Personal Access Token | [readonly] 
**links** | [**List[Link]**](Link.md) |  | [optional] 

## Example

```python
from lusid_configuration.models.personal_access_token import PersonalAccessToken

# TODO update the JSON string below
json = "{}"
# create an instance of PersonalAccessToken from a JSON string
personal_access_token_instance = PersonalAccessToken.from_json(json)
# print the JSON string representation of the object
print PersonalAccessToken.to_json()

# convert the object into a dict
personal_access_token_dict = personal_access_token_instance.to_dict()
# create an instance of PersonalAccessToken from a dict
personal_access_token_form_dict = personal_access_token.from_dict(personal_access_token_dict)
```
[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)


