# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AssetFolder(pydantic.BaseModel):
    display_name: typing.Optional[str] = pydantic.Field(
        alias="displayName", description="User visible name for the Asset Folder"
    )
    id: typing.Optional[str] = pydantic.Field(description="Unique identifier for the Asset Folder")
    parent_folder: typing.Optional[str] = pydantic.Field(
        alias="parentFolder", description="Pointer to parent Asset Folder (or null if root)"
    )
    assets: typing.Optional[typing.List[str]] = pydantic.Field(description="Array of Asset instances in the folder")
    site_id: typing.Optional[str] = pydantic.Field(
        alias="siteId", description="The unique id of the site the Asset Folder belongs to"
    )
    created_on: typing.Optional[dt.datetime] = pydantic.Field(
        alias="createdOn", description="Date that the Asset Folder was created on"
    )
    last_updated: typing.Optional[dt.datetime] = pydantic.Field(
        alias="lastUpdated", description="Date that the Asset Folder was last updated on"
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
