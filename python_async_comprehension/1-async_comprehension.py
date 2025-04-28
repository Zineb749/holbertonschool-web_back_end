#!/usr/bin/env python3
"""Async Comprehension Module
This module contains a coroutine that collects random numbers using async comprehension.
"""

from 0-async_generator import async_generator

async def async_comprehension():
    """Collect 10 random numbers asynchronously and return them."""
    return [i async for i in async_generator()]
