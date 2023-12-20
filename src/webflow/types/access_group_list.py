# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime
from .access_group import AccessGroup

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AccessGroupList(pydantic.BaseModel):
    """
    The list access groups results
    """

    count: typing.Optional[float] = pydantic.Field(description="Number of access groups returned")
    limit: typing.Optional[float] = pydantic.Field(description="The limit specified in the request")
    offset: typing.Optional[float] = pydantic.Field(description="The offset specified for pagination")
    total: typing.Optional[float] = pydantic.Field(description="Total number of access groups in the collection")
    access_groups: typing.Optional[typing.List[AccessGroup]] = pydantic.Field(
        alias="accessGroups", description="List of Site Access Groups"
    )

    def json(self, **kwargs: typing.Any) -> str:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().json(**kwargs_with_defaults)

    def dict(self, **kwargs: typing.Any) -> typing.Dict[str, typing.Any]:
        kwargs_with_defaults: typing.Any = {"by_alias": True, "exclude_unset": True, **kwargs}
        return super().dict(**kwargs_with_defaults)

    class Config:
        frozen = True
        smart_union = True
        allow_population_by_field_name = True
        json_encoders = {dt.datetime: serialize_datetime}
