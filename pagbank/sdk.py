"""
Module: sdk
"""

from pagbank.config import RequestOptions
from pagbank.http_cli import HttpClient
from pagbank.resources import (
    Charge,
)


class SDK:
    """Generate access to all API' modules, which are:

    1. Charge
    """

    def __init__(
        self,
        access_token,
        http_client=None,
        request_options=None,
    ):
        """Construct ur SDK Object to have access to all APIs modules.
        Args:
            [Click here for more info](https://www.pagbank.com/mlb/account/credentials)
            http_client (pagbank.http.http_client, optional): An implementation of
            HttpClient can be pass to be used to make the REST calls. Defaults to None.
            request_options (pagbank.config.request_options, optional): An instance
            of RequestOptions can be pass changing or adding custom options to ur REST
            calls. Defaults to None.
        Raises:
            ValueError: Param request_options must be a RequestOptions Object
        """

        self.http_client = http_client
        if http_client is None:
            self.http_client = HttpClient()

        self.request_options = request_options
        if request_options is None:
            self.request_options = RequestOptions()

        self.request_options.access_token = access_token

    def charge(self, request_options=None):
        """
        Returns the attribute value of the function
        """
        return Charge(
            request_options is not None and request_options or self.request_options,
            self.http_client,
        )

    @property
    def request_options(self):
        """
        Sets the attribute value and validates request_options
        """
        return self.__request_options

    @request_options.setter
    def request_options(self, value):
        if value is not None and not isinstance(value, RequestOptions):
            raise ValueError("Param request_options must be a RequestOptions Object")
        self.__request_options = value

    @property
    def http_client(self):
        """
        Sets the attribute value and validates http_client
        """
        return self.__http_client

    @http_client.setter
    def http_client(self, value):
        if value is not None and not isinstance(value, HttpClient):
            raise ValueError("Param http_client must be a HttpClient Object")
        self.__http_client = value
