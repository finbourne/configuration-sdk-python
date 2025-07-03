# ConfigurationItemSummary

A single configuration object
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key** | **str** | The key which identifies the configuration item | 
**value** | **str** | The value of the configuration item | 
**value_type** | **str** | The type of the configuration item&#39;s value | 
**is_secret** | **bool** | Defines whether or not the value is a secret. | 
**ref** | **str** | The reference to the configuration item | [readonly] 
**block_reveal** | **bool** | Defines whether the value is blocked with non-internal request. | 
**links** | [**List[Link]**](Link.md) |  | [optional] 
## Example

```python
from lusid_configuration.models.configuration_item_summary import ConfigurationItemSummary
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, conlist, constr

key: StrictStr = "example_key"
value: StrictStr = "example_value"
value_type: StrictStr = "example_value_type"
is_secret: StrictBool = # Replace with your value
is_secret:StrictBool = True
ref: StrictStr = "example_ref"
block_reveal: StrictBool = # Replace with your value
block_reveal:StrictBool = True
links: Optional[conlist(Link)] = None
configuration_item_summary_instance = ConfigurationItemSummary(key=key, value=value, value_type=value_type, is_secret=is_secret, ref=ref, block_reveal=block_reveal, links=links)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

