# -*- coding: utf-8 -*-
# @Author : luoliang
# @Time   : 2024/4/19 08:29
# @Desc   : 雪球存储实现类

from typing import Dict

from base.base_crawler import AbstractStore
from tools import time_util
from store.var import crawler_type_var


class XueqiuCsvStoreImplement(AbstractStore):
    csv_store_path: str = "data/xhs"

    def make_save_file_name(self, store_type: str) -> str:
        """
        make save file name by store type
        Args:
            store_type: contents or comments

        Returns: eg: data/xueqiu/search_comments_20240114.csv ...

        """
        return f"{self.csv_store_path}/{crawler_type_var.get()}_{store_type}_{time_util.get_current_date()}.csv"

    async def store_content(self, content_item: Dict):
        pass


class XueqiuDbStoreImplement(AbstractStore):
    async def store_content(self, content_item: Dict):
        pass


class XueqiuJsonStoreImplement(AbstractStore):
    async def store_content(self, content_item: Dict):
        pass
