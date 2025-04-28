#!/usr/bin/env python3
"""Measure Runtime Module
This module measures the runtime of running async_comprehension 4 times in parallel.
"""

import asyncio
import time
from 1-async_comprehension import async_comprehension

async def measure_runtime():
    """Measure total runtime of running async_comprehension four times in parallel."""
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end = time.perf_counter()
    return end - start
