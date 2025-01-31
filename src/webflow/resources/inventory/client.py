# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from ...core.api_error import ApiError
from ...core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from ...core.jsonable_encoder import jsonable_encoder
from ...errors.bad_request_error import BadRequestError
from ...errors.conflict_error import ConflictError
from ...errors.forbidden_error import ForbiddenError
from ...errors.internal_server_error import InternalServerError
from ...errors.not_found_error import NotFoundError
from ...errors.too_many_requests_error import TooManyRequestsError
from ...errors.unauthorized_error import UnauthorizedError
from ...types.inventory_item import InventoryItem
from .types.inventory_update_request_inventory_type import InventoryUpdateRequestInventoryType

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class InventoryClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list(self, collection_id: str, item_id: str) -> InventoryItem:
        """
        List the current inventory levels for a particular SKU item.

        Required scope | `ecommerce:read`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.inventory.list(
            collection_id="collection-id",
            item_id="item-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}/inventory"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InventoryItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update(
        self,
        collection_id: str,
        item_id: str,
        *,
        inventory_type: InventoryUpdateRequestInventoryType,
        update_quantity: typing.Optional[float] = OMIT,
        quantity: typing.Optional[float] = OMIT,
    ) -> InventoryItem:
        """
        Updates the current inventory levels for a particular SKU item. Updates may be given in one or two methods, absolutely or incrementally. Absolute updates are done by setting `quantity` directly. Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.

        Required scope | `ecommerce:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item

            - inventory_type: InventoryUpdateRequestInventoryType. infinite or finite

            - update_quantity: typing.Optional[float]. Adds this quantity to currently store quantity. Can be negative.

            - quantity: typing.Optional[float]. Immediately sets quantity to this value.
        ---
        from webflow import InventoryUpdateRequestInventoryType
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.inventory.update(
            collection_id="collection-id",
            item_id="item-id",
            inventory_type=InventoryUpdateRequestInventoryType.INFINITE,
            update_quantity=1.0,
            quantity=100.0,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"inventoryType": inventory_type}
        if update_quantity is not OMIT:
            _request["updateQuantity"] = update_quantity
        if quantity is not OMIT:
            _request["quantity"] = quantity
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}/inventory"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InventoryItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncInventoryClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list(self, collection_id: str, item_id: str) -> InventoryItem:
        """
        List the current inventory levels for a particular SKU item.

        Required scope | `ecommerce:read`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.inventory.list(
            collection_id="collection-id",
            item_id="item-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}/inventory"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InventoryItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update(
        self,
        collection_id: str,
        item_id: str,
        *,
        inventory_type: InventoryUpdateRequestInventoryType,
        update_quantity: typing.Optional[float] = OMIT,
        quantity: typing.Optional[float] = OMIT,
    ) -> InventoryItem:
        """
        Updates the current inventory levels for a particular SKU item. Updates may be given in one or two methods, absolutely or incrementally. Absolute updates are done by setting `quantity` directly. Incremental updates are by specifying the inventory delta in `updateQuantity` which is then added to the `quantity` stored on the server.

        Required scope | `ecommerce:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item

            - inventory_type: InventoryUpdateRequestInventoryType. infinite or finite

            - update_quantity: typing.Optional[float]. Adds this quantity to currently store quantity. Can be negative.

            - quantity: typing.Optional[float]. Immediately sets quantity to this value.
        ---
        from webflow import InventoryUpdateRequestInventoryType
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.inventory.update(
            collection_id="collection-id",
            item_id="item-id",
            inventory_type=InventoryUpdateRequestInventoryType.INFINITE,
            update_quantity=1.0,
            quantity=100.0,
        )
        """
        _request: typing.Dict[str, typing.Any] = {"inventoryType": inventory_type}
        if update_quantity is not OMIT:
            _request["updateQuantity"] = update_quantity
        if quantity is not OMIT:
            _request["quantity"] = quantity
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}/inventory"
            ),
            json=jsonable_encoder(_request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(InventoryItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 403:
            raise ForbiddenError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 409:
            raise ConflictError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
