#!/usr/bin/env python
# encoding: utf-8
#
# Copyright (c) 2014 Doug Hellmann.  All rights reserved.
"""Creating a Future with ensure_future
"""
#end_pymotw_header

import asyncio


def mark_done(future, result):
    print('setting future result to {!r}'.format(result))
    future.set_result(result)


async def wrapped():
    print('wrapped')
    return 'result'


async def inner(task):
    print('inner: starting')
    print('inner: waiting for {!r}'.format(task))
    result = await task
    print('inner: task returned {!r}'.format(result))


async def starter(loop):
    print('starter: creating task')
    task = asyncio.ensure_future(wrapped(), loop=loop)
    print('starter: waiting for inner')
    await inner(task)
    print('starter: inner returned')


event_loop = asyncio.get_event_loop()

try:
    print('entering event loop')
    result = event_loop.run_until_complete(
        starter(event_loop)
    )
finally:
    event_loop.close()
