from typing import Dict

import httpx


class Client(object):
    """A Client which has been authenticated with Digest Auth"""

    """
        Attributes:
        base_url: The base URL for the API, all requests are made to a relative path to this URL
        username: The username for the API
        password: The password for the API
        cookies: A dictionary of cookies to be sent with every request
        headers: A dictionary of headers to be sent with every request
        timeout: The maximum amount of a time in seconds a request can take. API functions will raise
            httpx.TimeoutException if this is exceeded.
        verify_ssl: Whether or not to verify the SSL certificate of the API server. This should be True in production,
            but can be set to False for testing purposes.
        raise_on_unexpected_status: Whether or not to raise an errors.UnexpectedStatus if the API returns a
            status code that was not documented in the source OpenAPI document.
    """

    def __init__(
        self,
        base_url: str,
        username: str,
        password: str,
        cookies: Dict[str, str] = {},
        headers: Dict[str, str] = {},
        timeout: float = 30,
        verify_ssl: bool = True,
        raise_on_unexpected_status: bool = False,
        keepalive_expiry: float = 30,
    ) -> None:

        self.base_url = base_url
        self.cookies = cookies
        self.headers = headers
        self.timeout = timeout
        self.verify_ssl = verify_ssl
        self.raise_on_unexpected_status = raise_on_unexpected_status
        self.cookies = cookies
        self.username = username
        self.password = password
        self.keepalive_expiry = keepalive_expiry

        limits = httpx.Limits(keepalive_expiry=keepalive_expiry)
        self._api = httpx.Client(limits=limits, verify=verify_ssl, auth=httpx.DigestAuth(username, password))
        self._asyncio_api = httpx.AsyncClient(
            limits=limits, verify=verify_ssl, auth=httpx.DigestAuth(username, password)
        )

    def get_headers(self) -> Dict[str, str]:
        """Get headers to be used in all endpoints"""
        return {**self.headers}

    def get_cookies(self) -> Dict[str, str]:
        """Get cookies to be used in all endpoints"""
        return {**self.cookies}

    def get_timeout(self) -> float:
        """Get timeout to be used in all endpoints"""
        return self.timeout
