# UpdateConfigurationItem

The information required to update a configuration item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **str** | The new value of the configuration item | 
**description** | **str** | The new description of the configuration item | [optional] 
**block_reveal** | **bool** | The requested new state of BlockReveal | [optional] 
## Example

```python
from lusid_configuration.models.update_configuration_item import UpdateConfigurationItem
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, constr, validator

value: StrictStr = "example_value"
description: Optional[StrictStr] = "example_description"
block_reveal: Optional[StrictBool] = # Replace with your value
block_reveal:Optional[StrictBool] = None
update_configuration_item_instance = UpdateConfigurationItem(value=value, description=description, block_reveal=block_reveal)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

