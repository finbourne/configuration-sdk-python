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
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

id: ResourceId = # Replace with your value
type: StrictStr = "example_type"
description: Optional[StrictStr] = "example_description"
create_configuration_set_instance = CreateConfigurationSet(id=id, type=type, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

