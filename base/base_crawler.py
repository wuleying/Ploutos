#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Dict, Optional

from playwright.async_api import BrowserContext, BrowserType


class AbstractCrawler(ABC):
    @abstractmethod
    def init_config(self, platform: str, login_type: str, target_type: str):
        pass

    @abstractmethod
    async def start(self):
        pass

    @abstractmethod
    async def search(self):
        pass

    @abstractmethod
    async def launch_browser(self,
                             chromium: BrowserType,
                             playwright_proxy: Optional[Dict],
                             user_agent: Optional[str],
                             headless: bool = True) -> BrowserContext:
        pass


class AbstractLogin(ABC):
    @abstractmethod
    async def begin(self):
        pass

    @abstractmethod
    async def login_by_qrcode(self):
        pass

    @abstractmethod
    async def login_by_mobile(self):
        pass

    @abstractmethod
    async def login_by_cookies(self):
        pass


class AbstractStore(ABC):
    @abstractmethod
    async def store_content(self, content_item: Dict):
        pass


class AbstractApiClient(ABC):
    @abstractmethod
    async def request(self, method, url, **kwargs):
        pass

    @abstractmethod
    async def update_cookies(self, browser_context: BrowserContext):
        pass

    @abstractmethod
    async def pong(self):
        pass
