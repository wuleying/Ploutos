#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import asyncio
import sys

import config
from base.base_crawler import AbstractCrawler
from platform.xueqiu.core import XueQiuCrawler


class CrawlerFactory:
    CRAWLERS = {
        "xueqiu": XueQiuCrawler
    }

    @staticmethod
    def create_crawler(platform: str) -> AbstractCrawler:
        crawler_class = CrawlerFactory.CRAWLERS.get(platform)

        if not crawler_class:
            raise ValueError("Invalid Platform Currently only supported xueqiu ...")

        return crawler_class()


async def main():
    # define command line params ...
    parser = argparse.ArgumentParser(description='Media Ploutos program.')
    parser.add_argument('--platform', type=str, help='Media platform select (xueqiu)',
                        choices=["xueqiu"], default=config.PLATFORM)
    parser.add_argument('--lt', type=str, help='Login type (qrcode | phone | cookie)',
                        choices=["qrcode", "phone", "cookie"], default=config.LOGIN_TYPE)
    parser.add_argument('--type', type=str, help='crawler type (stock)',
                        choices=["stock"], default=config.CRAWLER_TYPE)

    args = parser.parse_args()
    crawler = CrawlerFactory.create_crawler(platform=args.platform)
    crawler.init_config(
        platform=args.platform,
        login_type=args.lt,
        target_type=args.type
    )

    await crawler.start()


if __name__ == '__main__':
    try:
        asyncio.run(main())
        # asyncio.get_event_loop().run_until_complete(main())
    except KeyboardInterrupt:
        sys.exit()
