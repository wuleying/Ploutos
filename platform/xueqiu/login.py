# -*- coding: utf-8 -*-

from typing import Optional

from base.base_crawler import AbstractLogin
from playwright.async_api import BrowserContext, Page


class XueQiuLogin(AbstractLogin):
    def __init__(self,
                 login_type: str,
                 browser_context: BrowserContext,
                 context_page: Page,
                 login_phone: Optional[str] = "",
                 cookie_str: str = ""
                 ):
        self.login_type = login_type
        self.browser_context = browser_context
        self.context_page = context_page
        self.login_phone = login_phone
        self.cookie_str = cookie_str

    async def begin(self):
        pass

    async def login_by_qrcode(self):
        pass

    async def login_by_mobile(self):
        pass

    async def login_by_cookies(self):
        pass
