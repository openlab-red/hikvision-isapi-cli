from urllib.parse import urlparse
import logging

from hikvision_isapi_cli.client import Client
from hikvision_isapi_cli.api.isapi import channels_1_picture

_LOGGER = logging.getLogger(__name__)

class RtspClient:
    def __init__(self, client: Client, rtsp_port: int, path: str) -> None:
        """
        Initialize the RtspClient class.

        :param client: A `Client` object containing the credentials for the RTSP stream.
        :param rtsp_port: The RTSP port of the stream.
        :param path: The path of the stream.
        """
        
        self.client = client
        self.rtsp_port = rtsp_port
        self.path = path
        self.host = urlparse(client.base_url).hostname
        self.stream_url = (
            f"rtsp://{client.username}:{client.password}@{self.host}:{rtsp_port}/{path}"
        )

    def get_snapshot(self, channel_id: int) -> bytes:
        """
        Capture a snapshot from the RTSP stream and return the binary data of the image.

        :return: The binary data of the image, or None if the frame cannot be read.
        """
        return channels_1_picture.sync_detailed(channel_id=channel_id,client=self.client).content
    
    def stream_source(self) -> str:
        """
        The RTSP stream string.
        """
        return self.stream_url
    
