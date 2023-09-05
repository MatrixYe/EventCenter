# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         a 
# Author:       yepeng
# Date:         2021/10/22 2:44 下午
# Description: 
# -------------------------------------------------------------------------------
from typing import Callable, Any

from tool.mongo_api import MongoApi


def _get_mogo_database():
    return MongoApi.from_conf(host='127.0.0.1', port=6002, user='root', password='password', db='event_center')


db = _get_mogo_database()

success: Callable[[Any], dict[str, str | int | Any]] = lambda data: {'code': 1, 'data': data, 'msg': 'success'}
fail: Callable[[Any], dict[str, Any | None]] = lambda msg: {'code': 0, 'data': None, 'msg': msg}
