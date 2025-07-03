# UpdateConfigurationSet

The information required to update a configuration set
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The new description of the configuration set | [optional] 
## Example

```python
from lusid_configuration.models.update_configuration_set import UpdateConfigurationSet
from typing import Any, Dict, Optional
from pydantic.v1 import BaseModel, Field, constr

description: Optional[StrictStr] = "example_description"
update_configuration_set_instance = UpdateConfigurationSet(description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

