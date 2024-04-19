# -*- coding: utf-8 -*-

import aiomysql
import contextvars

from async_db import AsyncMysqlDB


ploutos_db_var: contextvars.ContextVar[AsyncMysqlDB] = contextvars.ContextVar(
    "ploutos_db_var"
)
db_conn_pool_var: contextvars.ContextVar[aiomysql.Pool] = contextvars.ContextVar(
    "db_conn_pool_var"
)
