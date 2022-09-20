# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round F - Problem C. Story of Seasons
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000bef319
#
# Time:  O(NlogN)
# Space: O(N)
#

from heapq import heappush, heappop

def story_of_seasons():
    D, N, X = map(int, input().split())
    seeds = [list(map(int, input().split())) for _ in range(N)]
    seeds.sort(key=lambda x: D-x[1])
    result = 0
    max_heap = []
    prev = D
    for d in sorted({0}|{D-l for _, l, _ in seeds}, reverse=True):
        cnt = 0
        while cnt < (prev-d)*X and max_heap:
            v, q = heappop(max_heap)
            v, q = -v, -q
            g = min((prev-d)*X-cnt, q)
            q -= g
            cnt += g
            result += g*v
            if q:
                heappush(max_heap, (-v, -q))
        while seeds and D-seeds[-1][1] == d:
            q, _, v = seeds.pop()
            heappush(max_heap, (-v, -q))
        prev = d
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, story_of_seasons()))


# Copyright (c) 2022 kamyu. All rights reserved.
#
# Google Kick Start 2022 Round F - Problem B. Water Container System
# https://codingcompetitions.withgoogle.com/kickstart/round/00000000008cb409/0000000000bef79e
#
# Time:  O(N)
# Space: O(N)
#

def bfs(adj):
    capacity = []
    lookup = [False]*len(adj)
    q = [0]
    lookup[0] = True
    while q:
        capacity.append(len(q))
        new_q = []
        for u in q:
            for v in adj[u]:
                if lookup[v]:
                    continue
                lookup[v] = True
                new_q.append(v)
        q = new_q
    return capacity

def water_container_system():
    N, Q = map(int, input().split())
    adj = [[] for _ in range(N)]
    for _ in range(N-1):
        i, j = map(int, input().split())
        i -= 1
        j -= 1
        adj[i].append(j)
        adj[j].append(i)
    _ = [input() for _ in range(Q)]
    result = 0
    for c in bfs(adj):
        if result+c > Q:
            break
        result += c
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, water_container_system()))