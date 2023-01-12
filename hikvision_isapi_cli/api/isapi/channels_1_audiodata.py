from http import HTTPStatus
from io import BytesIO
from typing import Any, Dict, Optional, Union

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_response_status import RootTypeForXMLResponseStatus
from ...types import UNSET, File, Response, Unset


def _get_kwargs(
    channel_id: int,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ISAPI/System/TwoWayAudio/channels/{channelId}/audioData".format(client.base_url, channelId=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["sessionId"] = session_id

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[Union[File, RootTypeForXMLResponseStatus]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = File(payload=BytesIO(response.content))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RootTypeForXMLResponseStatus.from_dict(xmltodict.parse(response.text))

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[Union[File, RootTypeForXMLResponseStatus]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    channel_id: int,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[File, RootTypeForXMLResponseStatus]]:
    """Receive audio data from a specific two-way audio channel.

    Args:
        channel_id (int):
        session_id (Union[Unset, None, str]):  Example: le4bckh5l7tzbkxu4uzjh5takgmdhu22.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, RootTypeForXMLResponseStatus]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        session_id=session_id,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: int,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[File, RootTypeForXMLResponseStatus]]:
    """Receive audio data from a specific two-way audio channel.

    Args:
        channel_id (int):
        session_id (Union[Unset, None, str]):  Example: le4bckh5l7tzbkxu4uzjh5takgmdhu22.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, RootTypeForXMLResponseStatus]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        session_id=session_id,
    ).parsed


async def asyncio_detailed(
    channel_id: int,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Response[Union[File, RootTypeForXMLResponseStatus]]:
    """Receive audio data from a specific two-way audio channel.

    Args:
        channel_id (int):
        session_id (Union[Unset, None, str]):  Example: le4bckh5l7tzbkxu4uzjh5takgmdhu22.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, RootTypeForXMLResponseStatus]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        session_id=session_id,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: int,
    *,
    client: Client,
    session_id: Union[Unset, None, str] = UNSET,
) -> Optional[Union[File, RootTypeForXMLResponseStatus]]:
    """Receive audio data from a specific two-way audio channel.

    Args:
        channel_id (int):
        session_id (Union[Unset, None, str]):  Example: le4bckh5l7tzbkxu4uzjh5takgmdhu22.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[File, RootTypeForXMLResponseStatus]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            session_id=session_id,
        )
    ).parsed
