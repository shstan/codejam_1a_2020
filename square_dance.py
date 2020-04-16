import numpy as np
"""
    You just implement what is said in the question...
    Takes time... But the solution also needs optimizations.
    This solution is TLE, but works for small grids.
"""

def compass_neighbor_avg(arr, still_competing, r, c):
    R, C = arr.shape
    all_neighbors = []
    for i in range(r + 1, R):
        if still_competing[i, c]:
            all_neighbors.append(arr[i, c])
            break
    for i in reversed(range(r)):
        if still_competing[i, c]:
            all_neighbors.append(arr[i, c])
            break
    for i in range(c + 1, C):
        if still_competing[r, i]:
            all_neighbors.append(arr[r, i])
            break
    for i in reversed(range(c)):
        if still_competing[r, i]:
            all_neighbors.append(arr[r, i])
            break
    if not all_neighbors:
        all_neighbors = [0]
    return sum(all_neighbors) / len(all_neighbors)

def neighbor_scores(arr, still_competing):
    R, C = arr.shape
    scores = np.empty(shape=(R, C))
    for r in range(R):
        for c in range(C):
            scores[r, c] = compass_neighbor_avg(arr, still_competing, r, c)
    return scores

def interest_level(arr, still_competing):
    sum_ = 0
    for r in range(R):
        for c in range(C):
            if still_competing[r, c]:
                sum_ += arr[r, c]
    return sum_

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        R, C = [int(x) for x in input().split()]
        arr = np.empty(shape=(R, C))
        still_competing = np.ones(shape=(R, C)).astype('bool')
        old_still_competing = np.zeros(shape=(R, C)).astype('bool')
        for i in range(R):
            arr[i, :] = np.array([int(x) for x in input().split()])
        print('start!')
        interest_level_competition = 0
        while np.any(still_competing != old_still_competing):
            interest_level_competition += interest_level(arr, still_competing)
            scores = neighbor_scores(arr, still_competing)
            old_still_competing[:] = still_competing[:]
            still_competing[:] = (arr >= scores)[:]
        print("Case #{}:".format(t), int(interest_level_competition))


