#!/usr/bin/env python
# -*- coding: utf-8 -*-

dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]

global visited
global m, n
global count


def check_edge(x, y):
    if (x < m and x >= 0) and \
            (y < n and y >= 0) and \
            (visited[x][y] == 0):
        return True
    else:
        return False


def dfs(x, y, dep):
    global m, n
    global count

    if (dep == m * n):
        count += 1
        return

    for i in range(0, 4):
        x_next = x + dir[i][0]
        y_next = y + dir[i][1]
        if (check_edge(x_next, y_next)):
            visited[x_next][y_next] = 1
            dfs(x_next, y_next, dep + 1)
            visited[x_next][y_next] = 0


def main(argv):
    if len(argv) != 2:
        exit(1)
    global m, n
    m = int(argv[0])
    n = int(argv[1])

    global visited
    visited = [([0] * n) for i in range(m)]
    visited[0][0] = 1

    global count
    count = 0

    dfs(0, 0, 1)
    print(count)
    exit(0)
