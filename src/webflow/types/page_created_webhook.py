# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class PageCreatedWebhook(pydantic.BaseModel):
    """
    The Webhook payload for when a Page is created
    """

    site_id: typing.Optional[str] = pydantic.Field(alias="siteId")
    page_id: typing.Optional[str] = pydantic.Field(alias="pageId")
    page_title: typing.Optional[str] = pydantic.Field(alias="pageTitle")
    created_at: typing.Optional[dt.datetime] = pydantic.Field(alias="createdAt")

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
