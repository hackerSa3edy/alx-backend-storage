#!/usr/bin/env python3
"""Connecting Redis with Python

This module provides a Cache class to interact with Redis, including
decorators to count method calls and store call history.
"""
import uuid
from functools import wraps
from typing import Union, Callable, Optional, Tuple, Dict

import redis


def count_calls(method: Callable) -> Callable:
    """Decorator to count the number of times a method is called.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with call counting functionality.
    """
    @wraps(method)
    def wrapper(self, *args: Tuple, **kwargs: Dict) -> Callable:
        """Wrapper function for the decorator function.

        Increments the call count each time the method is called.

        Args:
            *args (Tuple): Positional arguments for the method.
            **kwargs (Dict): Keyword arguments for the method.

        Returns:
            Callable: The result of the original method call.
        """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store the history of inputs and outputs for a
    particular function.

    Args:
        method (Callable): The method to be decorated.

    Returns:
        Callable: The wrapped method with history storing functionality.
    """
    @wraps(method)
    def wrapper(self, *args: Tuple, **kwargs: Dict) -> Union[
        str, bytes, int, float
    ]:
        """Wrapper function for the decorator function.

        Stores the inputs and outputs of the method call in Redis.

        Args:
            *args (Tuple): Positional arguments for the method.
            **kwargs (Dict): Keyword arguments for the method.

        Returns:
            Union[str, bytes, int, float]: The result of the original
            method call.
        """
        inputs = str(args)
        result = method(self, *args, **kwargs)
        outputs = str(result)

        self._redis.rpush(f'{method.__qualname__}:inputs', inputs)
        self._redis.rpush(f'{method.__qualname__}:outputs', outputs)

        return result

    return wrapper


def replay(fn: Callable) -> None:
    """Function to display the history of calls of a particular function.

    Args:
        fn (Callable): The function whose call history is to be displayed.
    """
    client = redis.Redis()
    method_name = fn.__qualname__
    input_list_name = f"{method_name}:inputs"
    output_list_name = f"{method_name}:outputs"

    calls_count = client.get(method_name)
    if calls_count:
        calls_count = calls_count.decode('utf-8')
    else:
        calls_count = '0'

    inputs = [input.decode('utf-8') for input in client.lrange(
        input_list_name,
        0,
        -1
        )]
    outputs = [output.decode('utf-8') for output in client.lrange(
        output_list_name,
        0,
        -1
        )]

    print(f'{method_name} was called {calls_count} times:')
    for input, output in zip(inputs, outputs):
        print(f'{method_name}(*{input}) -> {output}')


class Cache:
    """Cache class for connecting to Redis.

    This class provides methods to store and retrieve data from Redis,
    with decorators to count method calls and store call history.
    """

    def __init__(self) -> None:
        """Initialize the Redis connection and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the given data with a random key.

        Args:
            data (Union[str, bytes, int, float]): The data to be stored.

        Returns:
            str: The key under which the data is stored.
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
        str,
        bytes,
        int,
        float
    ]:
        """Get the value of a specific key.

        Args:
            key (str): The key whose value is to be retrieved.
            fn (Optional[Callable]): An optional function to convert the value.

        Returns:
            Union[str, bytes, int, float]: The value of the key, optionally
            converted.
        """
        value = self._redis.get(key)
        if value and fn:
            return fn(value)
        return value

    def get_str(self, key: str) -> str:
        """Get the value of a key and convert it to a string.

        Args:
            key (str): The key whose value is to be retrieved.

        Returns:
            str: The value of the key as a string.
        """
        return self.get(key, lambda data: data.decode('utf-8'))

    def get_int(self, key: str) -> int:
        """Get the value of a key and convert it to an integer.

        Args:
            key (str): The key whose value is to be retrieved.

        Returns:
            int: The value of the key as an integer.
        """
        return self.get(key, int)
