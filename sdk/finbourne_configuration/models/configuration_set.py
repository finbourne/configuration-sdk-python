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
from pydantic import BaseModel, Field, StrictStr, conlist, constr
from finbourne_configuration.models.configuration_item_summary import ConfigurationItemSummary
from finbourne_configuration.models.link import Link
from finbourne_configuration.models.resource_id import ResourceId

class ConfigurationSet(BaseModel):
    """
    The full version of the configuration set  # noqa: E501
    """
    created_at: datetime = Field(..., alias="createdAt", description="The date referring to the creation date of the configuration set")
    created_by: constr(strict=True, min_length=1) = Field(..., alias="createdBy", description="Who created the configuration set")
    last_modified_at: datetime = Field(..., alias="lastModifiedAt", description="The date referring to the date when the configuration set was last modified")
    last_modified_by: constr(strict=True, min_length=1) = Field(..., alias="lastModifiedBy", description="Who modified the configuration set most recently")
    description: Optional[StrictStr] = Field(None, description="Describes the configuration set")
    items: Optional[conlist(ConfigurationItemSummary)] = Field(None, description="The collection of the configuration items that this set contains.")
    id: ResourceId = Field(...)
    type: constr(strict=True, min_length=1) = Field(..., description="The type (personal or shared) of the configuration set")
    links: Optional[conlist(Link)] = None
    __properties = ["createdAt", "createdBy", "lastModifiedAt", "lastModifiedBy", "description", "items", "id", "type", "links"]

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
    def from_json(cls, json_str: str) -> ConfigurationSet:
        """Create an instance of ConfigurationSet from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in items (list)
        _items = []
        if self.items:
            for _item in self.items:
                if _item:
                    _items.append(_item.to_dict())
            _dict['items'] = _items
        # override the default output from pydantic by calling `to_dict()` of id
        if self.id:
            _dict['id'] = self.id.to_dict()
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

        # set to None if items (nullable) is None
        # and __fields_set__ contains the field
        if self.items is None and "items" in self.__fields_set__:
            _dict['items'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ConfigurationSet:
        """Create an instance of ConfigurationSet from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ConfigurationSet.parse_obj(obj)

        _obj = ConfigurationSet.parse_obj({
            "created_at": obj.get("createdAt"),
            "created_by": obj.get("createdBy"),
            "last_modified_at": obj.get("lastModifiedAt"),
            "last_modified_by": obj.get("lastModifiedBy"),
            "description": obj.get("description"),
            "items": [ConfigurationItemSummary.from_dict(_item) for _item in obj.get("items")] if obj.get("items") is not None else None,
            "id": ResourceId.from_dict(obj.get("id")) if obj.get("id") is not None else None,
            "type": obj.get("type"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None
        })
        return _obj