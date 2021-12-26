def numFriendRequests(ages):
    cnt = [0] * 121
    for age in ages:
        cnt[age] += 1
    pre = [0] * 121
    for i in range(1, 121):
        pre[i] = pre[i - 1] + cnt[i]

    ans = 0
    for i in range(15, 121):
        if cnt[i] > 0:
            bound = int(i * 0.5 + 8)
            ans += cnt[i] * (pre[i] - pre[bound - 1] - 1)
    return ans

