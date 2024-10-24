#!/usr/bin/env python3
"""Caching request module"""

from functools import wraps
from typing import Callable

import redis
import requests

# Constants
CACHE_EXPIRATION = 10  # Cache expiration time in seconds


def track_get_page(fn: Callable) -> Callable:
    """Decorator for get_page to cache responses and track call counts.

    Args:
        fn (Callable): The function to be decorated.

    Returns:
        Callable: The wrapped function with caching and tracking functionality.
    """
    @wraps(fn)
    def wrapper(url: str) -> str:
        """Wrapper function that:
            - Checks whether URL data is cached
            - Tracks how many times get_page is called

        Args:
            url (str): The URL to fetch.

        Returns:
            str: The response text from the URL.
        """
        client = redis.Redis()
        client.incr(f'count:{url}')
        cached_page = client.get(url)
        if cached_page:
            return cached_page.decode('utf-8')

        response = fn(url)
        client.setex(url, CACHE_EXPIRATION, response)
        return response

    return wrapper


@track_get_page
def get_page(url: str) -> str:
    """Makes an HTTP request to a given endpoint.

    Args:
        url (str): The URL to fetch.

    Returns:
        str: The response text from the URL.
    """
    return requests.get(url).text
