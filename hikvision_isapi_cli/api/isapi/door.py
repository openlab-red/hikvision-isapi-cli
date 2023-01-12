from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_remote_control_door import RootTypeForXMLRemoteControlDoor
from ...models.root_type_for_xml_response_status import RootTypeForXMLResponseStatus
from ...types import Response


def _get_kwargs(
    door_id: int,
    *,
    client: Client,
    json_body: RootTypeForXMLRemoteControlDoor,
) -> Dict[str, Any]:
    url = "{}/ISAPI/AccessControl/RemoteControl/door/{doorId}".format(client.base_url, doorId=door_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": xmltodict.unparse(json_json_body),
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
    door_id: int,
    *,
    client: Client,
    json_body: RootTypeForXMLRemoteControlDoor,
) -> Response[RootTypeForXMLResponseStatus]:
    """door/1

     door/1

    Args:
        door_id (int):
        json_body (RootTypeForXMLRemoteControlDoor): RemoteControlDoor message in XML format
            Example: {'RemoteControlDoor': {'@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema', 'cmd': '', 'password': ''}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    kwargs = _get_kwargs(
        door_id=door_id,
        client=client,
        json_body=json_body,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    door_id: int,
    *,
    client: Client,
    json_body: RootTypeForXMLRemoteControlDoor,
) -> Optional[RootTypeForXMLResponseStatus]:
    """door/1

     door/1

    Args:
        door_id (int):
        json_body (RootTypeForXMLRemoteControlDoor): RemoteControlDoor message in XML format
            Example: {'RemoteControlDoor': {'@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema', 'cmd': '', 'password': ''}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    return sync_detailed(
        door_id=door_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    door_id: int,
    *,
    client: Client,
    json_body: RootTypeForXMLRemoteControlDoor,
) -> Response[RootTypeForXMLResponseStatus]:
    """door/1

     door/1

    Args:
        door_id (int):
        json_body (RootTypeForXMLRemoteControlDoor): RemoteControlDoor message in XML format
            Example: {'RemoteControlDoor': {'@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema', 'cmd': '', 'password': ''}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    kwargs = _get_kwargs(
        door_id=door_id,
        client=client,
        json_body=json_body,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    door_id: int,
    *,
    client: Client,
    json_body: RootTypeForXMLRemoteControlDoor,
) -> Optional[RootTypeForXMLResponseStatus]:
    """door/1

     door/1

    Args:
        door_id (int):
        json_body (RootTypeForXMLRemoteControlDoor): RemoteControlDoor message in XML format
            Example: {'RemoteControlDoor': {'@version': '2.0', '@xmlns':
            'http://www.isapi.org/ver20/XMLSchema', 'cmd': '', 'password': ''}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLResponseStatus]
    """

    return (
        await asyncio_detailed(
            door_id=door_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
