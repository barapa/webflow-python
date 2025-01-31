# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

import typing_extensions

from ..core.datetime_utils import serialize_datetime
from .error_details_item import ErrorDetailsItem

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class UserLimitReached(pydantic.BaseModel):
    code: typing.Optional[typing_extensions.Literal["user_limit_reached"]]
    message: typing.Optional[str] = pydantic.Field(description="Error message")
    external_reference: typing.Optional[str] = pydantic.Field(
        alias="externalReference", description="Link to more information"
    )
    details: typing.Optional[typing.List[ErrorDetailsItem]] = pydantic.Field(description="Array of errors")

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
