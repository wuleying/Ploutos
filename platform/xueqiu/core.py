# -*- coding: utf-8 -*-

from typing import Optional, Dict

from base.base_crawler import AbstractCrawler
from playwright.async_api import BrowserContext, BrowserType, Page, async_playwright

from .client import XueQiuClient


class XueQiuCrawler(AbstractCrawler):
    platform: str
    login_type: str
    crawler_type: str
    context_page: Page
    xueqiu_client: XueQiuClient
    browser_context: BrowserContext

    def init_config(self, platform: str, login_type: str, target_type: str):
        print(
            "Init xueqiu crawler, platform: %s, login_type: %s, target_type: %s"
            % (platform, login_type, target_type)
        )
        pass

    async def start(self):
        pass

    async def search(self):
        pass

    async def launch_browser(
        self,
        chromium: BrowserType,
        playwright_proxy: Optional[Dict],
        user_agent: Optional[str],
        headless: bool = True,
    ) -> BrowserContext:
        pass
