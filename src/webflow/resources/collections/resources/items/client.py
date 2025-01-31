# This file was auto-generated by Fern from our API Definition.

import typing
import urllib.parse
from json.decoder import JSONDecodeError

from .....core.api_error import ApiError
from .....core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .....core.jsonable_encoder import jsonable_encoder
from .....core.remove_none_from_dict import remove_none_from_dict
from .....errors.bad_request_error import BadRequestError
from .....errors.internal_server_error import InternalServerError
from .....errors.not_found_error import NotFoundError
from .....errors.too_many_requests_error import TooManyRequestsError
from .....errors.unauthorized_error import UnauthorizedError
from .....types.collection_item import CollectionItem
from .....types.collection_item_list import CollectionItemList
from .types.items_publish_item_response import ItemsPublishItemResponse

try:
    import pydantic.v1 as pydantic  # type: ignore
except ImportError:
    import pydantic  # type: ignore

# this is used as the default value for optional parameters
OMIT = typing.cast(typing.Any, ...)


class ItemsClient:
    def __init__(self, *, client_wrapper: SyncClientWrapper):
        self._client_wrapper = client_wrapper

    def list_items(
        self, collection_id: str, *, offset: typing.Optional[float] = None, limit: typing.Optional[float] = None
    ) -> CollectionItemList:
        """
        List of all Items within a Collection. </br></br> Required scope | `cms:read`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - offset: typing.Optional[float]. Offset used for pagination if the results have more than limit records

            - limit: typing.Optional[float]. Maximum number of records to be returned (max limit: 100)
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.items.list_items(
            collection_id="collection-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items"),
            params=remove_none_from_dict({"offset": offset, "limit": limit}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CollectionItemList, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def create_item(self, collection_id: str, *, request: CollectionItem) -> None:
        """
        Create Item in a Collection. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - request: CollectionItem.
        ---
        from webflow import CollectionItem
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.items.create_item(
            collection_id="collection-id",
            request=CollectionItem(
                id="580e64008c9a982ac9b8b754",
                last_published="2023-03-17T18:47:35.560Z",
                last_updated="2023-03-17T18:47:35.560Z",
                created_on="2023-03-17T18:47:35.560Z",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def get_item(self, collection_id: str, item_id: str) -> CollectionItem:
        """
        Get details of a selected Collection Item. </br></br> Required scope | `cms:read`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.items.get_item(
            collection_id="collection-id",
            item_id="item-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CollectionItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def delete_item(self, collection_id: str, item_id: str) -> None:
        """
        Delete an Item from a Collection. This endpoint does not currently support bulk deletion. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.items.delete_item(
            collection_id="collection-id",
            item_id="item-id",
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def update_item(self, collection_id: str, item_id: str, *, request: CollectionItem) -> CollectionItem:
        """
        Update a selected Item in a Collection. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item

            - request: CollectionItem.
        ---
        from webflow import CollectionItem
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.items.update_item(
            collection_id="collection-id",
            item_id="item-id",
            request=CollectionItem(
                id="580e64008c9a982ac9b8b754",
                last_published="2023-03-17T18:47:35.560Z",
                last_updated="2023-03-17T18:47:35.560Z",
                created_on="2023-03-17T18:47:35.560Z",
            ),
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CollectionItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    def publish_item(self, collection_id: str, *, item_ids: typing.List[str]) -> ItemsPublishItemResponse:
        """
        Publish an item or multiple items. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_ids: typing.List[str].
        ---
        from webflow.client import Webflow

        client = Webflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        client.collections.items.publish_item(
            collection_id="collection-id",
            item_ids=[],
        )
        """
        _response = self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/publish"
            ),
            json=jsonable_encoder({"itemIds": item_ids}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ItemsPublishItemResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)


class AsyncItemsClient:
    def __init__(self, *, client_wrapper: AsyncClientWrapper):
        self._client_wrapper = client_wrapper

    async def list_items(
        self, collection_id: str, *, offset: typing.Optional[float] = None, limit: typing.Optional[float] = None
    ) -> CollectionItemList:
        """
        List of all Items within a Collection. </br></br> Required scope | `cms:read`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - offset: typing.Optional[float]. Offset used for pagination if the results have more than limit records

            - limit: typing.Optional[float]. Maximum number of records to be returned (max limit: 100)
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.items.list_items(
            collection_id="collection-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items"),
            params=remove_none_from_dict({"offset": offset, "limit": limit}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CollectionItemList, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def create_item(self, collection_id: str, *, request: CollectionItem) -> None:
        """
        Create Item in a Collection. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - request: CollectionItem.
        ---
        from webflow import CollectionItem
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.items.create_item(
            collection_id="collection-id",
            request=CollectionItem(
                id="580e64008c9a982ac9b8b754",
                last_published="2023-03-17T18:47:35.560Z",
                last_updated="2023-03-17T18:47:35.560Z",
                created_on="2023-03-17T18:47:35.560Z",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items"),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def get_item(self, collection_id: str, item_id: str) -> CollectionItem:
        """
        Get details of a selected Collection Item. </br></br> Required scope | `cms:read`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.items.get_item(
            collection_id="collection-id",
            item_id="item-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "GET",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CollectionItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def delete_item(self, collection_id: str, item_id: str) -> None:
        """
        Delete an Item from a Collection. This endpoint does not currently support bulk deletion. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.items.delete_item(
            collection_id="collection-id",
            item_id="item-id",
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "DELETE",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}"
            ),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def update_item(self, collection_id: str, item_id: str, *, request: CollectionItem) -> CollectionItem:
        """
        Update a selected Item in a Collection. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_id: str. Unique identifier for an Item

            - request: CollectionItem.
        ---
        from webflow import CollectionItem
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.items.update_item(
            collection_id="collection-id",
            item_id="item-id",
            request=CollectionItem(
                id="580e64008c9a982ac9b8b754",
                last_published="2023-03-17T18:47:35.560Z",
                last_updated="2023-03-17T18:47:35.560Z",
                created_on="2023-03-17T18:47:35.560Z",
            ),
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "PATCH",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/{item_id}"
            ),
            json=jsonable_encoder(request),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(CollectionItem, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)

    async def publish_item(self, collection_id: str, *, item_ids: typing.List[str]) -> ItemsPublishItemResponse:
        """
        Publish an item or multiple items. </br></br> Required scope | `cms:write`

        Parameters:
            - collection_id: str. Unique identifier for a Collection

            - item_ids: typing.List[str].
        ---
        from webflow.client import AsyncWebflow

        client = AsyncWebflow(
            access_token="YOUR_ACCESS_TOKEN",
        )
        await client.collections.items.publish_item(
            collection_id="collection-id",
            item_ids=[],
        )
        """
        _response = await self._client_wrapper.httpx_client.request(
            "POST",
            urllib.parse.urljoin(
                f"{self._client_wrapper.get_base_url()}/", f"collections/{collection_id}/items/publish"
            ),
            json=jsonable_encoder({"itemIds": item_ids}),
            headers=self._client_wrapper.get_headers(),
            timeout=60,
        )
        if 200 <= _response.status_code < 300:
            return pydantic.parse_obj_as(ItemsPublishItemResponse, _response.json())  # type: ignore
        if _response.status_code == 400:
            raise BadRequestError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 401:
            raise UnauthorizedError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 404:
            raise NotFoundError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 429:
            raise TooManyRequestsError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        if _response.status_code == 500:
            raise InternalServerError(pydantic.parse_obj_as(typing.Any, _response.json()))  # type: ignore
        try:
            _response_json = _response.json()
        except JSONDecodeError:
            raise ApiError(status_code=_response.status_code, body=_response.text)
        raise ApiError(status_code=_response.status_code, body=_response_json)
