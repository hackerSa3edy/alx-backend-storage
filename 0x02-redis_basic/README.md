# Project: 0x02. Redis basic

## Description

This project focuses on using Redis with Python. It covers the basics of connecting to Redis, storing and retrieving data, implementing caching, and tracking function calls. The tasks provide hands-on experience with Redis and its integration with Python.

## Resources

### Read or watch

* [Redis commands](https://redis.io/commands)
* [Redis python client](https://pypi.org/project/redis)
* [How to Use Redis With Python](https://realpython.com/python-redis)
* [Redis Crash Course Tutorial](https://www.youtube.com/watch?v=Hbt56gFj998)

## Learning Objectives

### General

* How to connect to a Redis server from Python
* How to store and retrieve data in Redis
* How to implement caching in Redis
* How to track function calls using Redis
* How to use decorators to enhance functions with Redis

## Tasks

| Task                                               | File                         | Description                                                                 |
|----------------------------------------------------|------------------------------|-----------------------------------------------------------------------------|
| 0. Writing strings to Redis                        | [exercise.py](./exercise.py) | Implement a method to store data in Redis.                                  |
| 1. Reading from Redis and recovering original type | [exercise.py](./exercise.py) | Implement methods to retrieve data from Redis and convert it to the original type. |
| 2. Incrementing values                             | [exercise.py](./exercise.py) | Implement a decorator to count the number of times a method is called.      |
| 3. Storing lists                                   | [exercise.py](./exercise.py) | Implement a method to store lists in Redis.                                 |
| 4. Retrieving lists                                | [exercise.py](./exercise.py) | Implement a method to retrieve lists from Redis.                            |
| 5. Implementing an expiring web cache and tracker  | [web.py](./web.py)           | Implement a caching mechanism for HTTP requests and track the number of requests. |
