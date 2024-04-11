#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from abc import ABC, abstractmethod
from typing import Dict, Optional

from playwright.async_api import BrowserContext, BrowserType


class AbstractPloutos(ABC):
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
