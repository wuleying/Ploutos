# -*- coding: utf-8 -*-

import asyncio
import aiomysql
import config

from typing import Dict
from urllib.parse import urlparse
from async_db import AsyncMysqlDB
from tools import utils
from store.var import db_conn_pool_var, db_var


def parse_mysql_url(mysql_url) -> Dict:
    """
    从配置文件中解析db链接url，给到aiomysql用，因为aiomysql不支持直接以URL的方式传递链接信息。
    Args:
        mysql_url: mysql://root:{RELATION_DB_PWD}@localhost:3306/db_name
    Returns:
    """
    parsed_url = urlparse(mysql_url)
    db_params = {
        "host": parsed_url.hostname,
        "port": parsed_url.port or 3306,
        "user": parsed_url.username,
        "password": parsed_url.password,
        "db": parsed_url.path.lstrip("/"),
    }
    return db_params


async def init_ploutos_db():
    """
    初始化数据库链接池对象，并将该对象塞给ploutos_db_var上下文变量
    Returns:
    """
    db_conn_params = parse_mysql_url(config.RELATION_DB_URL)
    pool = await aiomysql.create_pool(autocommit=True, **db_conn_params)
    async_db_obj = AsyncMysqlDB(pool)

    # 将连接池对象和封装的CRUD sql接口对象放到上下文变量中
    db_conn_pool_var.set(pool)
    db_var.set(async_db_obj)


async def init_db():
    """
    初始化db连接池
    Returns:
    """
    utils.logger.info("[init_db] start init db connect object")
    await init_ploutos_db()
    utils.logger.info("[init_db] end init db connect object")


async def close():
    """
    关闭连接池
    Returns:
    """
    utils.logger.info("[close] close db pool")
    db_pool: aiomysql.Pool = db_conn_pool_var.get()
    if db_pool is not None:
        db_pool.close()


if __name__ == "__main__":
    asyncio.run(init_db())
