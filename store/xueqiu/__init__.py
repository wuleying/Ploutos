# -*- coding: utf-8 -*-
# @Author : luoliang
# @Time   : 2024/4/18 08:22
# @Desc   : 持久化

import config

from . import xueqiu_store_impl
from .xueqiu_store_impl import *


class XueqiuStoreFactory:
    STORES = {
        "csv": "XueqiuCsvStoreImplement",
        "db": "XueqiuDbStoreImplement",
        "json": "XueqiuJsonStoreImplement",
    }

    @staticmethod
    def create_store() -> AbstractStore:
        store_class = XueqiuStoreFactory.STORES.get(config.SAVE_DATA_OPTION)
        if not store_class:
            raise ValueError(
                "[XueqiuStoreFactory.create_store] Invalid save option only supported csv or db or json ..."
            )

        return store_class()
