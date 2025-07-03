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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, conlist, constr

id: ResourceId = # Replace with your value
type: StrictStr = "example_type"
links: Optional[conlist(Link)] = None
configuration_set_summary_instance = ConfigurationSetSummary(id=id, type=type, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

