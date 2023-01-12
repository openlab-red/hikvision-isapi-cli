from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_two_way_audio_session import RootTypeForXMLTwoWayAudioSession
from ...types import Response


def _get_kwargs(
    channel_id: int,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ISAPI/System/TwoWayAudio/channels/{channelId}/open".format(client.base_url, channelId=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RootTypeForXMLTwoWayAudioSession]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForXMLTwoWayAudioSession.from_dict(xmltodict.parse(response.text))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RootTypeForXMLTwoWayAudioSession]:
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
) -> Response[RootTypeForXMLTwoWayAudioSession]:
    """channels/1/open

     channels/1/open

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLTwoWayAudioSession]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    channel_id: int,
    *,
    client: Client,
) -> Optional[RootTypeForXMLTwoWayAudioSession]:
    """channels/1/open

     channels/1/open

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLTwoWayAudioSession]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: int,
    *,
    client: Client,
) -> Response[RootTypeForXMLTwoWayAudioSession]:
    """channels/1/open

     channels/1/open

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLTwoWayAudioSession]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    channel_id: int,
    *,
    client: Client,
) -> Optional[RootTypeForXMLTwoWayAudioSession]:
    """channels/1/open

     channels/1/open

    Args:
        channel_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLTwoWayAudioSession]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
