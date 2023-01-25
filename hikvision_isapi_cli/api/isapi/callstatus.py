from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import Client
from ...models.root_type_for_call_status import RootTypeForCallStatus
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    format_: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/ISAPI/VideoIntercom/callStatus".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["format"] = format_

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, client: Client, response: httpx.Response) -> Optional[RootTypeForCallStatus]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForCallStatus.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(*, client: Client, response: httpx.Response) -> Response[RootTypeForCallStatus]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    format_: Union[Unset, None, str] = UNSET,
) -> Response[RootTypeForCallStatus]:
    """callStatus

     callStatus

    Args:
        format_ (Union[Unset, None, str]):  Example: json.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForCallStatus]
    """

    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    format_: Union[Unset, None, str] = UNSET,
) -> Optional[RootTypeForCallStatus]:
    """callStatus

     callStatus

    Args:
        format_ (Union[Unset, None, str]):  Example: json.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForCallStatus]
    """

    return sync_detailed(
        client=client,
        format_=format_,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    format_: Union[Unset, None, str] = UNSET,
) -> Response[RootTypeForCallStatus]:
    """callStatus

     callStatus

    Args:
        format_ (Union[Unset, None, str]):  Example: json.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForCallStatus]
    """

    kwargs = _get_kwargs(
        client=client,
        format_=format_,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    format_: Union[Unset, None, str] = UNSET,
) -> Optional[RootTypeForCallStatus]:
    """callStatus

     callStatus

    Args:
        format_ (Union[Unset, None, str]):  Example: json.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[RootTypeForCallStatus]
    """

    return (
        await asyncio_detailed(
            client=client,
            format_=format_,
        )
    ).parsed
