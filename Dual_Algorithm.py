#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/12/16 10:39
# @Author  : Xavier Ma
# @Email   : xavier_mayiming@163.com
# @File    : Dual_Algorithm.py
# @Statement : The dual algorithm to solve the minimum-cost flow problem
# The minimum-cost flow problem aims to find the cheapest possible way of sending a certain amount of flow through a flow network.


def Bellman_Ford(network, source, destination):
    """
    The Bellman-Ford algorithm to solve the shortest path problem with negative weights
    :param network: {node1: {node2: weight, node3: weight, ...}, ...}
    :param source: the source node
    :param destination: the destination node
    :return:
    """
    # Step 1. Initialization
    nn = len(network)  # node number
    dis = [float('inf')] * nn  # the distance set
    path = [[]] * nn  # the path set
    dis[source] = 0
    path[source] = [source]

    # Step 2. The main loop
    for _ in range(nn - 1):
        for i in range(nn):
            if dis[i] != float('inf'):
                for j in network[i].keys():
                    if dis[i] + network[i][j] < dis[j]:
                        dis[j] = dis[i] + network[i][j]
                        temp_path = path[i].copy()
                        temp_path.append(j)
                        path[j] = temp_path

    # Step 3. Judge if the path contains a negative weight cycle
    for i in range(nn):
        if dis[i] != float('inf'):
            for j in network[i].keys():
                if dis[i] + network[i][j] < dis[j]:
                    print('The network contains negative weight cycles')
                    return [], float('inf')
    return path[destination], dis[destination]


def main(network, source, destination, f):
    """
    The main function of the dual algorithm
    :param network: flow network, {node1: {node2: [capacity, cost], node3: [capacity, cost], ...}, ...}
    :param source: the source node
    :param destination: the destination node
    :param f: the pre-defined amount of flow
    :return:
    """
    # Step 1. Initialization
    nn = len(network)  # node number
    max_flow = 0
    cost = 0
    flow = {}  # flow
    for i in range(nn):
        flow[i] = {}
        for j in network[i].keys():
            flow[i][j] = 0

    # Step 2. The main loop
    while max_flow < f:

        # Step 2.1. Establish the length network
        length_network = {}
        for i in range(nn):
            length_network[i] = {}
        for i in range(nn):
            for j in network[i].keys():
                if flow[i][j] < network[i][j][0]:
                    length_network[i][j] = network[i][j][1]
                if flow[i][j] > 0:
                    length_network[j][i] = -network[i][j][1]

        # Step 2.2. Find an augmenting path
        aug_path, aug_cost = Bellman_Ford(length_network, source, destination)
        if not aug_path:  # there does not exist an augmenting path
            return "No feasible solution!"

        # Step 2.3. Change the flow
        aug_flow = float('inf')
        for i in range(len(aug_path) - 1):
            n1 = aug_path[i]
            n2 = aug_path[i + 1]
            if n2 in network[n1].keys():
                aug_flow = min(aug_flow, network[n1][n2][0] - flow[n1][n2])
            else:
                aug_flow = min(aug_flow, flow[n2][n1])
        aug_flow = min(f - max_flow, aug_flow)
        max_flow += aug_flow
        for i in range(len(aug_path) - 1):
            n1 = aug_path[i]
            n2 = aug_path[i + 1]
            if n2 in network[n1].keys():
                flow[n1][n2] += aug_flow
                cost += aug_flow * network[n1][n2][1]
            else:
                flow[n2][n1] -= aug_flow
                cost -= aug_flow * network[n2][n1][1]
    return cost


if __name__ == '__main__':
    test_network = {
        0: {1: [10, 4], 2: [8, 1]},
        1: {3: [2, 6], 4: [7, 1]},
        2: {1: [5, 2], 3: [10, 3]},
        3: {4: [4, 2]},
        4: {},
    }
    s = 0
    d = 4
    f = 10
    print(main(test_network, s, d, f))
