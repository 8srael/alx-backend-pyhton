#!/usr/bin/env python3
"""Waits for a random number of seconds"""

import asyncio
import random


async def wait_random(max_delay=10):
    """Waits for a random number of seconds."""
    random_number = random.uniform(0, max_delay)
    await asyncio.sleep(random_number)
    return random_number