# UpdateConfigurationSet

The information required to update a configuration set
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | The new description of the configuration set | [optional] 
## Example

```python
from lusid_configuration.models.update_configuration_set import UpdateConfigurationSet
from typing import List, Dict, Optional, Any, Union, TYPE_CHECKING
from typing_extensions import Annotated
from pydantic.v1 import BaseModel, StrictStr, StrictInt, StrictBool, StrictFloat, StrictBytes, Field, validator, ValidationError, conlist, constr
from datetime import datetime

description: Optional[StrictStr] = "example_description"
update_configuration_set_instance = UpdateConfigurationSet(description=description)

```

[Back to Model list](../README.md#documentation-for-models) &#8226; [Back to API list](../README.md#documentation-for-api-endpoints) &#8226; [Back to README](../README.md)

