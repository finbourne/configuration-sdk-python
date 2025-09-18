# CreateConfigurationItem

The information required to create a configuration item
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key of the new configuration item | 
**value** | **str** | The value of the new configuration item              The maximum size for secrets is 4KB and for text values is 2MB | 
**value_type** | **str** | The type (text, number, boolean, textCollection, numberCollection) of the new configuration item&#39;s value. The validation for each type is as follows: - text: any value - number: double (e.g. \&quot;5.5\&quot;) - boolean: true/false - textCollection: comma separated list (e.g. \&quot;a,b,c\&quot;) - numberCollection: comma separated list of doubles (e.g. \&quot;1,2,3\&quot;) | [optional] 
**is_secret** | **bool** | Defines whether or not the value is a secret | 
**description** | **str** | The description of the new configuration item | [optional] 
**block_reveal** | **bool** | A property to indicate if revealing the value is blocked. | [optional] 
## Example

```python
from lusid_configuration.models.create_configuration_item import CreateConfigurationItem
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, constr, validator

key: StrictStr = "example_key"
value: StrictStr = "example_value"
value_type: Optional[StrictStr] = "example_value_type"
is_secret: StrictBool = # Replace with your value
is_secret:StrictBool = True
description: Optional[StrictStr] = "example_description"
block_reveal: Optional[StrictBool] = # Replace with your value
block_reveal:Optional[StrictBool] = None
create_configuration_item_instance = CreateConfigurationItem(key=key, value=value, value_type=value_type, is_secret=is_secret, description=description, block_reveal=block_reveal)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

