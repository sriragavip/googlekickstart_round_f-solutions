def scheduling_a_meeting():
    N, K, X, D = map(int, input().split())
    events = [[] for _ in range(X+D+1)]
    M = int(input())
    for _ in range(M):
        P, L, R = map(int, input().split())
        events[L+1].append((+1, P-1))
        events[R+X].append((-1, P-1))
    result = M
    cnt = [0]*N
    freq = [0]*(M+1)
    freq[0] = N
    curr = kth_cnt = 0
    kth_cnt_used_freq = K
    for d in range(D+1):
        for diff, p in events[d]:
            if cnt[p] < kth_cnt:
                curr += diff
                if diff == 1 and cnt[p]+1 == kth_cnt:
                    kth_cnt_used_freq += 1
            elif cnt[p] == kth_cnt:
                if diff == 1:
                    if kth_cnt_used_freq == freq[kth_cnt]:
                        curr += 1
                        kth_cnt += 1
                        kth_cnt_used_freq = 1
                else:
                    curr -= 1
                    kth_cnt_used_freq -= 1
                    if kth_cnt_used_freq == 0:
                        kth_cnt -= 1
                        kth_cnt_used_freq = freq[kth_cnt]+1
            freq[cnt[p]] -= 1
            cnt[p] += diff
            freq[cnt[p]] += 1
        if d >= X:
            result = min(result, curr)
    return result

for case in range(int(input())):
    print('Case #%d: %s' % (case+1, scheduling_a_meeting()))