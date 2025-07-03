# ConfigurationItem

The full version of the configuration item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** | The date referring to the creation date of the configuration item | 
**created_by** | **str** | Who created the configuration item | 
**last_modified_at** | **datetime** | The date referring to the date when the configuration item was last modified | 
**last_modified_by** | **str** | Who modified the configuration item most recently | 
**description** | **str** | Describes the configuration item | [optional] 
**key** | **str** | The key which identifies the configuration item | 
**value** | **str** | The value of the configuration item | 
**value_type** | **str** | The type of the configuration item&#39;s value | 
**is_secret** | **bool** | Defines whether or not the value is a secret. | 
**ref** | **str** | The reference to the configuration item | [readonly] 
**block_reveal** | **bool** | Defines whether the value is blocked with non-internal request. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_configuration.models.configuration_item import ConfigurationItem
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from datetime import datetime
created_at: datetime = # Replace with your value
created_by: StrictStr = "example_created_by"
last_modified_at: datetime = # Replace with your value
last_modified_by: StrictStr = "example_last_modified_by"
description: Optional[StrictStr] = "example_description"
key: StrictStr = "example_key"
value: StrictStr = "example_value"
value_type: StrictStr = "example_value_type"
is_secret: StrictBool = # Replace with your value
is_secret:StrictBool = True
ref: StrictStr = "example_ref"
block_reveal: StrictBool = # Replace with your value
block_reveal:StrictBool = True
links: Optional[conlist(Link)] = None
configuration_item_instance = ConfigurationItem(created_at=created_at, created_by=created_by, last_modified_at=last_modified_at, last_modified_by=last_modified_by, description=description, key=key, value=value, value_type=value_type, is_secret=is_secret, ref=ref, block_reveal=block_reveal, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

