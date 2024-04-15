# -*- coding: utf-8 -*-

from typing import Dict
from playwright.async_api import BrowserContext, Page

from base.base_crawler import AbstractApiClient


class XueQiuClient(AbstractApiClient):

    def __init__(
            self,
            timeout=10,
            proxies=None,
            *,
            headers: Dict[str, str],
            playwright_page: Page,
            cookie_dict: Dict[str, str],
    ):
        self.proxies = proxies
        self.timeout = timeout
        self.headers = headers
        self._host = "https://xueqiu.com"
        self.playwright_page = playwright_page
        self.cookie_dict = cookie_dict

    async def request(self, method, url, **kwargs):
        pass

    async def update_cookies(self, browser_context: BrowserContext):
        pass

    async def pong(self):
        pass
