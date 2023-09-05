# -*- coding: utf-8 -*-#
# -------------------------------------------------------------------------------
# Name:         a 
# Author:       yepeng
# Date:         2021/10/22 2:44 下午
# Description: 
# -------------------------------------------------------------------------------
from typing import Union

from fastapi import APIRouter
from pydantic import BaseModel

from . import success, db

router = APIRouter()


@router.get('')
def hello():
    return "hello network router"


@router.get('/')
async def read_networks(key: Union[str] = None):
    var = db['networks'].find()
    return success(var)


class Network(BaseModel):
    name: str
    cid: int


@router.post('/')
async def create_network(network: Network):
    print(network)
    data = {
        'name': network.name,
        'cid': network.cid
    }
    # db.insert(colle='network',data=data)
    db.update_one('network', query={'name': network.name}, data=data)
    return 'done'
