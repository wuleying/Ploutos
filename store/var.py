# -*- coding: utf-8 -*-

from contextvars import ContextVar
from async_db import AsyncMysqlDB
import aiomysql

ploutos_db_var: ContextVar[AsyncMysqlDB] = ContextVar("ploutos_db_var")
db_conn_pool_var: ContextVar[aiomysql.Pool] = ContextVar("db_conn_pool_var")
