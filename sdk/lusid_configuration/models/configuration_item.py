# coding: utf-8

"""
    FINBOURNE ConfigurationService API

    FINBOURNE Technology  # noqa: E501

    Contact: info@finbourne.com
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from typing import Any, Dict, List, Optional
from pydantic.v1 import BaseModel, Field, StrictBool, StrictStr, conlist, constr
from lusid_configuration.models.link import Link

class ConfigurationItem(BaseModel):
    """
    The full version of the configuration item  # noqa: E501
    """
    created_at: datetime = Field(..., alias="createdAt", description="The date referring to the creation date of the configuration item")
    created_by: constr(strict=True, min_length=1) = Field(..., alias="createdBy", description="Who created the configuration item")
    last_modified_at: datetime = Field(..., alias="lastModifiedAt", description="The date referring to the date when the configuration item was last modified")
    last_modified_by: constr(strict=True, min_length=1) = Field(..., alias="lastModifiedBy", description="Who modified the configuration item most recently")
    description: Optional[StrictStr] = Field(None, description="Describes the configuration item")
    key: constr(strict=True, min_length=1) = Field(..., description="The key which identifies the configuration item")
    value: constr(strict=True, min_length=1) = Field(..., description="The value of the configuration item")
    value_type: constr(strict=True, min_length=1) = Field(..., alias="valueType", description="The type of the configuration item's value")
    is_secret: StrictBool = Field(..., alias="isSecret", description="Defines whether or not the value is a secret.")
    ref: constr(strict=True, min_length=1) = Field(..., description="The reference to the configuration item")
    block_reveal: StrictBool = Field(..., alias="blockReveal", description="Defines whether the value is blocked with non-internal request.")
    links: Optional[conlist(Link)] = None
    __properties = ["createdAt", "createdBy", "lastModifiedAt", "lastModifiedBy", "description", "key", "value", "valueType", "isSecret", "ref", "blockReveal", "links"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ConfigurationItem:
        """Create an instance of ConfigurationItem from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "ref",
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if description (nullable) is None
        # and __fields_set__ contains the field
        if self.description is None and "description" in self.__fields_set__:
            _dict['description'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationItem:
        """Create an instance of ConfigurationItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationItem.parse_obj(obj)

        _obj = ConfigurationItem.parse_obj({
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "last_modified_at": obj.get("lastModifiedAt"),
            "last_modified_by": obj.get("lastModifiedBy"),
            "description": obj.get("description"),
            "key": obj.get("key"),
            "value": obj.get("value"),
            "value_type": obj.get("valueType"),
            "is_secret": obj.get("isSecret"),
            "ref": obj.get("ref"),
            "block_reveal": obj.get("blockReveal"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj
