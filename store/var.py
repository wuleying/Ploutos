# -*- coding: utf-8 -*-

import aiomysql
from contextvars import ContextVar

from async_db import AsyncMysqlDB


db_var: ContextVar[AsyncMysqlDB] = ContextVar("db_var")
db_conn_pool_var: ContextVar[aiomysql.Pool] = ContextVar("db_conn_pool_var")
crawler_type_var: ContextVar[str] = ContextVar("crawler_type", default="")
