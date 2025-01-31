# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class FormSubmission(pydantic.BaseModel):
    id: typing.Optional[str] = pydantic.Field(description="The unique id of the Form submission")
    display_name: typing.Optional[str] = pydantic.Field(
        alias="displayName", description="The Form name displayed on the site"
    )
    site_id: typing.Optional[str] = pydantic.Field(
        alias="siteId", description="The unique id of the Site the Form belongs to"
    )
    workspace_id: typing.Optional[str] = pydantic.Field(
        alias="workspaceId", description="The unique id of the Workspace the Site belongs to"
    )
    date_submitted: typing.Optional[dt.datetime] = pydantic.Field(
        alias="dateSubmitted", description="Date that the Form was submitted on"
    )
    form_response: typing.Optional[typing.Dict[str, typing.Any]] = pydantic.Field(
        alias="formResponse", description="The data submitted in the Form"
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
