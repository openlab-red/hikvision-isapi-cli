from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_response_status import RootTypeForXMLResponseStatus
from ...models.root_type_for_xml_video_input_channel_list import RootTypeForXMLVideoInputChannelList
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/ISAPI/System/Video/inputs/channels".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForXMLVideoInputChannelList.from_dict(xmltodict.parse(response.text))

        return response_200
    if response.status_code == HTTPStatus.BAD_REQUEST:
        response_400 = RootTypeForXMLResponseStatus.from_dict(xmltodict.parse(response.text))

        return response_400
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]:
    """inputs/channels

     inputs/channels

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]:
    """inputs/channels

     inputs/channels

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]:
    """inputs/channels

     inputs/channels

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]:
    """inputs/channels

     inputs/channels

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatus, RootTypeForXMLVideoInputChannelList]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
