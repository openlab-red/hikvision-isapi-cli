from http import HTTPStatus
from typing import Any, Dict, Optional

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_session_login_cap import RootTypeForXMLSessionLoginCap
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    username: str,
    random: int,
) -> Dict[str, Any]:
    url = "{}/ISAPI/Security/sessionLogin/capabilities".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["username"] = username

    params["random"] = random

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RootTypeForXMLSessionLoginCap]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForXMLSessionLoginCap.from_dict(xmltodict.parse(response.text))

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RootTypeForXMLSessionLoginCap]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    username: str,
    random: int,
) -> Response[RootTypeForXMLSessionLoginCap]:
    """sessionLogin/capabilities

     sessionLogin/capabilities

    Args:
        username (str):
        random (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLSessionLoginCap]
    """

    kwargs = _get_kwargs(
        client=client,
        username=username,
        random=random,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    username: str,
    random: int,
) -> Optional[RootTypeForXMLSessionLoginCap]:
    """sessionLogin/capabilities

     sessionLogin/capabilities

    Args:
        username (str):
        random (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLSessionLoginCap]
    """

    return sync_detailed(
        client=client,
        username=username,
        random=random,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    username: str,
    random: int,
) -> Response[RootTypeForXMLSessionLoginCap]:
    """sessionLogin/capabilities

     sessionLogin/capabilities

    Args:
        username (str):
        random (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLSessionLoginCap]
    """

    kwargs = _get_kwargs(
        client=client,
        username=username,
        random=random,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    username: str,
    random: int,
) -> Optional[RootTypeForXMLSessionLoginCap]:
    """sessionLogin/capabilities

     sessionLogin/capabilities

    Args:
        username (str):
        random (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForXMLSessionLoginCap]
    """

    return (
        await asyncio_detailed(
            client=client,
            username=username,
            random=random,
        )
    ).parsed
