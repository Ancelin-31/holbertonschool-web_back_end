#!/usr/bin/env python3
"""
create a rancom loop 10 times
"""
from typing import AsyncGenerator, List
import asyncio
import random


async def async_generator() -> AsyncGenerator[float, None]:
    """
    create a random loop 10 times
    """
    i = float
    for _ in range(10):
        await asyncio.sleep(1)
        yield i
