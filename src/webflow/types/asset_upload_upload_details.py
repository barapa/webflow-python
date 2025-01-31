# This file was auto-generated by Fern from our API Definition.

import datetime as dt
import typing

from ..core.datetime_utils import serialize_datetime

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore


class AssetUploadUploadDetails(pydantic.BaseModel):
    """
    Metadata for uploading the asset binary
    """

    acl: typing.Optional[str]
    bucket: typing.Optional[str]
    key: typing.Optional[str]
    policy: typing.Optional[str] = pydantic.Field(alias="Policy")
    x_amz_algorithm: typing.Optional[str] = pydantic.Field(alias="X-Amz-Algorithm")
    x_amz_credential: typing.Optional[str] = pydantic.Field(alias="X-Amz-Credential")
    x_amz_date: typing.Optional[str] = pydantic.Field(alias="X-Amz-Date")
    x_amz_security_token: typing.Optional[str] = pydantic.Field(
        alias="X-Amz-Security-Token",
        description="(optional) Temporary security token obtained when authenticated through AWS STS",
    )
    x_amz_signature: typing.Optional[str] = pydantic.Field(alias="X-Amz-Signature")
    success_action_status: typing.Optional[str]
    content_type: typing.Optional[str] = pydantic.Field(alias="content-type")
    cache_control: typing.Optional[str] = pydantic.Field(alias="Cache-Control")

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
