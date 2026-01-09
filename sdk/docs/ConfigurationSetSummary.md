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
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

id: ResourceId
type: StrictStr = "example_type"
links: Optional[List[Link]] = None
configuration_set_summary_instance = ConfigurationSetSummary(id=id, type=type, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

