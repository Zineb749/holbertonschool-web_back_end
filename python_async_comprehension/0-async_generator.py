#!/usr/bin/env python3
"""Async Generator Module
This module contains an asynchronous generator that yields random numbers.
"""

import asyncio
import random

async def async_generator():
    """Asynchronously yields 10 random numbers between 0 and 10, one every second."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

