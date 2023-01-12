from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_response_status import RootTypeForXMLResponseStatus
from ...types import Response


def _get_kwargs(
    channel_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ISAPI/System/TwoWayAudio/channels/{channelId}/close".format(client.base_url, channelId=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "auth": client.get_auth(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RootTypeForXMLResponseStatus]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForXMLResponseStatus.from_dict(xmltodict.parse(response.text))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RootTypeForXMLResponseStatus]:
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
) -> Response[RootTypeForXMLResponseStatus]:
    """channels/1/close

     channels/1/close

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: int,
    *,
    client: Client,
) -> Optional[RootTypeForXMLResponseStatus]:
    """channels/1/close

     channels/1/close

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: int,
    *,
    client: Client,
) -> Response[RootTypeForXMLResponseStatus]:
    """channels/1/close

     channels/1/close

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: int,
    *,
    client: Client,
) -> Optional[RootTypeForXMLResponseStatus]:
    """channels/1/close

     channels/1/close

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
