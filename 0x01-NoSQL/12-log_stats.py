#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def print_nginx_request_logs(nginx_collection):
    """
    Prints stats about Nginx request logs.

    Args:
        nginx_collection (pymongo.collection.Collection): The MongoDB
        collection object for Nginx logs.

    Prints:
        The total number of logs, the count of each HTTP method, and the count
        of status checks.
    """
    print('{} logs'.format(nginx_collection.count_documents({})))

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = nginx_collection.count_documents({'method': method})
        print('\tmethod {}: {}'.format(method, method_count))

    status_checks_count = nginx_collection.count_documents(
        {'method': 'GET', 'path': '/status'})
    print('{} status check'.format(status_checks_count))


def run():
    """
    Connects to the MongoDB server, retrieves the Nginx logs collection,
    and prints stats about the Nginx request logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
