# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         a 
# Author:       yepeng
# Date:         2021/10/22 2:44 下午
# Description: 
# -------------------------------------------------------------------------------

from fastapi import APIRouter
from pydantic import BaseModel

from . import success

router = APIRouter()


#
# @router.get('')
# def hello():
#     return "hello event router"


class EventTask(BaseModel):
    # 区块网络
    network: str
    # 合约地址
    contract: str
    # 节点url
    node: str
    # 同步起始点(区块高度)
    start_block: int
    # interval 扫块时间间隔
    interval: int = 10
    # 区块延时(高度)
    delay: int = 0
    # 是否删除历史数据
    clear: bool = False


# -----------------------------控制器--------------------------------
# 启动一个新的任务
@router.post('/start')
def start_task(task: EventTask):
    return task
    pass


# 停止一个同步任务
@router.post('/stop/{task_id}')
def stop_task(task_id: str):
    result = {
        'task_id': task_id
    }
    return success(result)


# 移除一个任务，并删除历史数据
@router.post('/remove/{task_id}')
def remove_task(task_id: str):
    result = {
        'task_id': task_id
    }
    return success(result)


# -----------------------------状态信息--------------------------------
@router.get('/{task_id}/state')
def task_state(task_id: str):
    resilt = {
        'task_id': task_id
    }
    return success(resilt)


@router.get('/{task_id}/last_height')
def last_height(task_id: str):
    result = {
        'task_id': task_id,
        'height': 9999999
    }
    return success(result)


@router.get('/{task_id}/data')
def data(task_id: str, block_height: int):
    result = {
        'task_id': task_id,
        'block_height': block_height,
        'event': {
            'arg1': 'hahaha',
            'arg2': 8888
        }
    }
    return success(result)


@router.get('/data')
def query_data(contract: str, start: int, end: int, senders: str = ''):
    print(senders)
    result = {
        'contract': contract,
        'start': start,
        'end': end,
        'senders': senders.replace(' ', '').split(',') if senders else None

    }
    return success(result)
    pass
