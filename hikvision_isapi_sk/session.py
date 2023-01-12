import hashlib
import logging
import random
import time
from http import HTTPStatus
from typing import Dict

from hikvision_isapi_cli import Client
from hikvision_isapi_cli.api.default import session_heartbeat, session_login, session_login_capabilities
from hikvision_isapi_cli.models.root_type_for_xml_session_login import RootTypeForXMLSessionLogin
from hikvision_isapi_cli.models.root_type_for_xml_session_login_cap import RootTypeForXMLSessionLoginCap
from hikvision_isapi_cli.models.root_type_for_xml_session_login_session_login import (
    RootTypeForXMLSessionLoginSessionLogin,
)
from hikvision_isapi_cli.types import Response

_LOGGER = logging.getLogger(__name__)


class Session(object):

    __length = 8

    def __init__(self, client: Client) -> None:
        self.client = client

    def __sha256(self, msg: str) -> str:
        return hashlib.sha256(msg.encode("utf-8")).hexdigest()

    def __encodePwd(self, model: Dict[str, str], is_irreversible: bool) -> str:
        if is_irreversible:
            encode = self.__sha256(model["username"] + model["salt"] + self.client.password)
            encode = self.__sha256(encode + model["challenge"])
            for i in range(2, int(model["iterations"])):
                encode = self.__sha256(encode)
        else:
            encode = self.__sha256(self.client.password) + model["challenge"]
            for a in range(1, int(model["iterations"])):
                encode = self.__sha256(encode)
        return encode

    def start(self) -> None:

        random_number = random.randint(10 ** (self.__length - 1), 10**self.__length - 1)
        session_cap: RootTypeForXMLSessionLoginCap = session_login_capabilities.sync(
            client=self.client, username=self.client.username, random=random_number
        )
        session_login_cap = session_cap.session_login_cap

        encoded = self.__encodePwd(
            model={
                "challenge": session_login_cap.challenge,
                "username": self.client.username,
                "salt": session_login_cap.salt,
                "iterations": session_login_cap.iterations,
            },
            is_irreversible=session_login_cap.is_irreversible,
        )

        millis = int(round(time.time() * 1000))
        login = RootTypeForXMLSessionLogin()
        login.session_login = RootTypeForXMLSessionLoginSessionLogin()
        login.session_login.user_name = self.client.username
        login.session_login.password = encoded
        login.session_login.session_id = session_login_cap.session_id
        login.session_login.is_support_session_tag = False
        login.session_login.is_session_id_valid_long_term = True
        login.session_login.session_id_version = 2

        response: Response = session_login.sync_detailed(client=self.client, time_stamp=millis, json_body=login)
        cookies = response.headers["set-cookie"]
        web_session = cookies.split(";")[0].split("=")

        self.client.cookies = {web_session[0]: web_session[1], "Connection": "Keep-Alive"}
        self.client._api.cookies = self.client.cookies
        self.client._asyncio_api.cookies = self.client.cookies

        response: Response = session_heartbeat.sync_detailed(client=self.client)
        if response.status_code == HTTPStatus.OK:
            return True

        _LOGGER.error(response)
        return False

    def stop(self) -> None:
        _LOGGER.info("Stop Web Session: " + str(self.client._api.cookies))
        self.client.cookies = {}
        self.client._api.cookies = {}
        self.client._asyncio_api.cookies = {}

    async def heartbeat(self) -> bool:
        response: Response = await session_heartbeat.asyncio_detailed(client=self.client)
        if response.status_code == HTTPStatus.OK:
            return True
        return False
