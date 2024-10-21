#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def print_nginx_ips(nginx_collection):
    """
    Prints the top 10 IPs and their total request counts.

    Args:
        nginx_collection (pymongo.collection.Collection): The MongoDB
        collection object for Nginx logs.
    """
    print('IPs:')
    request_logs = nginx_collection.aggregate(
        [
            {
                '$group': {'_id': "$ip", 'totalRequests': {'$sum': 1}}
            },
            {
                '$sort': {'totalRequests': -1}
            },
            {
                '$limit': 10
            },
        ]
    )
    for request_log in request_logs:
        ip = request_log['_id']
        ip_requests_count = request_log['totalRequests']
        print(f'\t{ip}: {ip_requests_count}')


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
    total_logs = nginx_collection.count_documents({})
    print(f'{total_logs} logs')

    print('Methods:')
    methods = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    for method in methods:
        method_count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {method_count}')

    print_nginx_ips(nginx_collection)

    status_check_count = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"})
    print(f'{status_check_count} status check')


def run():
    """
    Connects to the MongoDB server, retrieves the Nginx logs collection,
    and prints stats about the Nginx request logs.
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    print_nginx_request_logs(client.logs.nginx)


if __name__ == '__main__':
    run()
