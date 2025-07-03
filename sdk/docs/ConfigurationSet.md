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
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictStr, conlist, constr
from datetime import datetime
created_at: datetime = # Replace with your value
created_by: StrictStr = "example_created_by"
last_modified_at: datetime = # Replace with your value
last_modified_by: StrictStr = "example_last_modified_by"
description: Optional[StrictStr] = "example_description"
items: Optional[conlist(ConfigurationItemSummary)] = # Replace with your value
id: ResourceId = # Replace with your value
type: StrictStr = "example_type"
links: Optional[conlist(Link)] = None
configuration_set_instance = ConfigurationSet(created_at=created_at, created_by=created_by, last_modified_at=last_modified_at, last_modified_by=last_modified_by, description=description, items=items, id=id, type=type, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

