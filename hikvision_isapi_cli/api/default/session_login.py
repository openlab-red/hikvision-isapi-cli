from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx
import xmltodict

from ... import errors
from ...client import Client
from ...models.root_type_for_xml_response_status_authentication_failed import (
    RootTypeForXMLResponseStatusAuthenticationFailed,
)
from ...models.root_type_for_xml_session_login import RootTypeForXMLSessionLogin
from ...models.root_type_for_xml_session_login_response import RootTypeForXMLSessionLoginResponse
from ...types import UNSET, Response


def _get_kwargs(
    *,
    client: Client,
    json_body: RootTypeForXMLSessionLogin,
    time_stamp: float,
) -> Dict[str, Any]:
    url = "{}/ISAPI/Security/sessionLogin".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["timeStamp"] = time_stamp

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "data": xmltodict.unparse(json_json_body),
        "params": params,
    }


def _parse_response(
    *, client: Client, response: httpx.Response
) -> Optional[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = RootTypeForXMLSessionLoginResponse.from_dict(xmltodict.parse(response.text))

        return response_200
    if response.status_code == HTTPStatus.UNAUTHORIZED:
        response_401 = RootTypeForXMLResponseStatusAuthenticationFailed.from_dict(xmltodict.parse(response.text))

        return response_401
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(f"Unexpected status code: {response.status_code}")
    else:
        return None


def _build_response(
    *, client: Client, response: httpx.Response
) -> Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: RootTypeForXMLSessionLogin,
    time_stamp: float,
) -> Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]:
    """sessionLogin

     sessionLogin

    Args:
        time_stamp (float):
        json_body (RootTypeForXMLSessionLogin):  Example: {'SessionLogin': {'userName': 'admin',
            'password': 'xxxxxxxxxxxx', 'sessionID':
            '5ab522a707187090e375dc9e07f80f48f6a2a1c4a171b501b47ea9607db57f7f', 'isSupportSessionTag':
            'false', 'isSessionIDValidLongTerm': 'false', 'sessionIDVersion': '2', '@version': '2.0',
            '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        time_stamp=time_stamp,
    )

    response = client._api.request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: Client,
    json_body: RootTypeForXMLSessionLogin,
    time_stamp: float,
) -> Optional[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]:
    """sessionLogin

     sessionLogin

    Args:
        time_stamp (float):
        json_body (RootTypeForXMLSessionLogin):  Example: {'SessionLogin': {'userName': 'admin',
            'password': 'xxxxxxxxxxxx', 'sessionID':
            '5ab522a707187090e375dc9e07f80f48f6a2a1c4a171b501b47ea9607db57f7f', 'isSupportSessionTag':
            'false', 'isSessionIDValidLongTerm': 'false', 'sessionIDVersion': '2', '@version': '2.0',
            '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        time_stamp=time_stamp,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: RootTypeForXMLSessionLogin,
    time_stamp: float,
) -> Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]:
    """sessionLogin

     sessionLogin

    Args:
        time_stamp (float):
        json_body (RootTypeForXMLSessionLogin):  Example: {'SessionLogin': {'userName': 'admin',
            'password': 'xxxxxxxxxxxx', 'sessionID':
            '5ab522a707187090e375dc9e07f80f48f6a2a1c4a171b501b47ea9607db57f7f', 'isSupportSessionTag':
            'false', 'isSessionIDValidLongTerm': 'false', 'sessionIDVersion': '2', '@version': '2.0',
            '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        time_stamp=time_stamp,
    )

    response = await client._asyncio_api.request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: Client,
    json_body: RootTypeForXMLSessionLogin,
    time_stamp: float,
) -> Optional[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]:
    """sessionLogin

     sessionLogin

    Args:
        time_stamp (float):
        json_body (RootTypeForXMLSessionLogin):  Example: {'SessionLogin': {'userName': 'admin',
            'password': 'xxxxxxxxxxxx', 'sessionID':
            '5ab522a707187090e375dc9e07f80f48f6a2a1c4a171b501b47ea9607db57f7f', 'isSupportSessionTag':
            'false', 'isSessionIDValidLongTerm': 'false', 'sessionIDVersion': '2', '@version': '2.0',
            '@xmlns': 'http://www.isapi.org/ver20/XMLSchema'}}.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[RootTypeForXMLResponseStatusAuthenticationFailed, RootTypeForXMLSessionLoginResponse]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            time_stamp=time_stamp,
        )
    ).parsed
