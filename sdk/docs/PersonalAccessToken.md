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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

value: StrictStr = "example_value"
type: StrictStr = "example_type"
description: StrictStr = "example_description"
ref: StrictStr = "example_ref"
links: Optional[conlist(Link)] = None
personal_access_token_instance = PersonalAccessToken(value=value, type=type, description=description, ref=ref, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

