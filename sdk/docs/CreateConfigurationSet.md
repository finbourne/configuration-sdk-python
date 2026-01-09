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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
type: StrictStr = "example_type"
description: Optional[StrictStr] = "example_description"
create_configuration_set_instance = CreateConfigurationSet(id=id, type=type, description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

