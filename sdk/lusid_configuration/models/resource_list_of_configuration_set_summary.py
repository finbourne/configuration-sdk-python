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


from typing import Any, Dict, List, Optional
from pydantic.v1 import StrictStr, Field, BaseModel, Field, StrictStr, conlist 
from lusid_configuration.models.configuration_set_summary import ConfigurationSetSummary
from lusid_configuration.models.link import Link

class ResourceListOfConfigurationSetSummary(BaseModel):
    """
    ResourceListOfConfigurationSetSummary
    """
    values: conlist(ConfigurationSetSummary) = Field(...)
    href:  Optional[StrictStr] = Field(None,alias="href") 
    links: Optional[conlist(Link)] = None
    next_page:  Optional[StrictStr] = Field(None,alias="nextPage") 
    previous_page:  Optional[StrictStr] = Field(None,alias="previousPage") 
    __properties = ["values", "href", "links", "nextPage", "previousPage"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def __str__(self):
        """For `print` and `pprint`"""
        return pprint.pformat(self.dict(by_alias=False))

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> ResourceListOfConfigurationSetSummary:
        """Create an instance of ResourceListOfConfigurationSetSummary from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in values (list)
        _items = []
        if self.values:
            for _item in self.values:
                if _item:
                    _items.append(_item.to_dict())
            _dict['values'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in links (list)
        _items = []
        if self.links:
            for _item in self.links:
                if _item:
                    _items.append(_item.to_dict())
            _dict['links'] = _items
        # set to None if href (nullable) is None
        # and __fields_set__ contains the field
        if self.href is None and "href" in self.__fields_set__:
            _dict['href'] = None

        # set to None if links (nullable) is None
        # and __fields_set__ contains the field
        if self.links is None and "links" in self.__fields_set__:
            _dict['links'] = None

        # set to None if next_page (nullable) is None
        # and __fields_set__ contains the field
        if self.next_page is None and "next_page" in self.__fields_set__:
            _dict['nextPage'] = None

        # set to None if previous_page (nullable) is None
        # and __fields_set__ contains the field
        if self.previous_page is None and "previous_page" in self.__fields_set__:
            _dict['previousPage'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ResourceListOfConfigurationSetSummary:
        """Create an instance of ResourceListOfConfigurationSetSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return ResourceListOfConfigurationSetSummary.parse_obj(obj)

        _obj = ResourceListOfConfigurationSetSummary.parse_obj({
            "values": [ConfigurationSetSummary.from_dict(_item) for _item in obj.get("values")] if obj.get("values") is not None else None,
            "href": obj.get("href"),
            "links": [Link.from_dict(_item) for _item in obj.get("links")] if obj.get("links") is not None else None,
            "next_page": obj.get("nextPage"),
            "previous_page": obj.get("previousPage")
        })
        return _obj
