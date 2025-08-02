#!/usr/bin/env python3
"""
async chrono
"""
import asyncio
import time
from typing import Callable

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    measure time
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    total_time = (time.perf_counter() - start)
    return (total_time / n)
