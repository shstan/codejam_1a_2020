"""
1. construct the head by taking all the starting string before first *, then check if there is a string that can satisfy all
2. construct tail using strings after last *
3. take all leftovers (between first * and last *) and put them, in any order of rules, from left to right.
4. Profit?
"""

if __name__ == "__main__":
    T = int(input())
    for i in range(1, T + 1):
        N = int(input())
        patterns = []
        for j in range(N):
            patterns.append(input())

        heads = []
        tails = []
        mids = []
        for pattern in patterns:
            heads.append(pattern[:pattern.find("*")])
            tails.append(pattern[pattern.rfind("*") + 1:])
            mids.extend(pattern[pattern.find("*") + 1 : pattern.rfind("*")].split("*"))

        max_head = max(heads, key = lambda s: len(s))
        max_tail = max(tails, key=lambda s: len(s))
        for head in heads:
            if len(max_head) > 0 and len(head) > 0 and max_head.find(head) != 0:
                print("Case #{}: *".format(i))
                break
        else:
            for tail in tails:
                if len(max_tail) > 0 and len(tail) > 0 and max_tail.rfind(tail) + len(tail) != len(max_tail):
                    print("Case #{}: *".format(i))
                    break
            else:
                res = ''.join([max_head] + mids + [max_tail])
                print("Case #{}: {}".format(i, res))

