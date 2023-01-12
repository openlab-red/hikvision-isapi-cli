from urllib.parse import urlparse
import logging
# Issue with opencv-python and homeassistant
# try:
#     # Verify that the OpenCV python package is pre-installed
#     import cv2
#     CV2_IMPORTED = True
# except ImportError:
#     CV2_IMPORTED = False

from hikvision_isapi_cli.client import Client

_LOGGER = logging.getLogger(__name__)

class RtspClient:
    def __init__(self, client: Client, rtsp_port: int, path: str) -> None:
        """
        Initialize the RtspClient class.

        :param client: A `Client` object containing the credentials for the RTSP stream.
        :param rtsp_port: The RTSP port of the stream.
        :param path: The path of the stream.
        """
        # if not CV2_IMPORTED:
        #     _LOGGER.error(
        #         "No OpenCV library found! Install or compile for your system "
        #         "following instructions here: http://opencv.org/releases.html"
        #     )
        #     return

        self.client = client
        self.rtsp_port = rtsp_port
        self.path = path
        self.host = urlparse(client.base_url).hostname
        self.stream_url = (
            f"rtsp://{client.username}:{client.password}@{self.host}:{rtsp_port}/{path}"
        )
        # self.cap = cv2.VideoCapture(self.stream_url)
        # self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 60)
        # self.cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"H264"))

    def get_snapshot(self) -> bytes:
        """
        Capture a snapshot from the RTSP stream and return the binary data of the image.

        :return: The binary data of the image, or None if the frame cannot be read.
        """
        # ret, frame = self.cap.read()
        # if ret:
        #     # Encode the image as JPEG
        #     _, img_encoded = cv2.imencode(".jpg", frame)
        #     # Return the binary data
        #     return img_encoded.tobytes()
        # else:
        #     # Return None if the frame cannot be read
        #     return None
        raise NotImplementedError()

    def release(self):
        """
        Release the RTSP stream.
        """
        #self.cap.release()
        raise NotImplementedError()

    def open(self):
        """
        Open the RTSP stream.
        """
        #self.cap.open(self.stream_url)
        raise NotImplementedError()
    
    def stream_source(self) -> str:
        """
        The RTSP stream string.
        """
        return self.stream_url
    
