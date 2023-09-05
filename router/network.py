# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         a 
# Author:       yepeng
# Date:         2021/10/22 2:44 下午
# Description: 
# -------------------------------------------------------------------------------

from fastapi import APIRouter
from pydantic import BaseModel

from . import success, fail, db

router = APIRouter()

COLL_NAME = "network"


class Network(BaseModel):
    name: str
    cid: int


# 查询区块网络列表
@router.get('')
async def read_networks(name: str = None, cid: int = None, search: str | int = None):
    query = {}

    if name:
        query = {'name': name}
    if cid:
        query = {'cid': cid}
    if not name and not cid and search:
        query = {"name": {"$regex": search}}

    results = db.find_all(c=COLL_NAME, query=query, sort_keys=[('cid', 1), ]).limit(100)
    resp = list(map(lambda x: {'_id': str(x['_id']), 'name': x['name'], 'cid': x['cid']}, results))
    print(resp)
    return success(resp)


# 新增或更新区块网络
@router.post('')
async def create_network(network: Network):
    data = {
        'name': network.name,
        'cid': network.cid
    }
    result = db.insert_or_update(coll=COLL_NAME, query={'name': network.name}, data=data)
    if result:
        return success(result)
    else:
        return fail("update network failed:unknown mongodb error")


# 删除某区块网络信息
@router.delete('')
async def delete_network(_id: str):
    result = db.delete(coll=COLL_NAME, _id=_id)
    if result == 1:
        return success(f"success to delete {_id}")
    else:
        return fail("can not find network by id")
