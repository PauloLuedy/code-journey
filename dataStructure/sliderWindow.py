# return max of substring without repeating 3 characters

# [abcabcbb]
# l = 3
# r = 7
# _max = 1
# counter = {}
# counter = {'b': 2, 'c': 1, 'a': 1}

def maximumLengthSubString(self, s: str) -> int:
    l, r    = 0, 0
    _max = 1
    counter = {}
    counter[s[0]] = 1

    while r < len(s):  
        r += 1
        if r < len(s):
            counter[s[r]] = counter.get(s[r], 0) + 1

            while counter[s[r]] == 3:
                  counter[s[l]] -= 1
                  l += 1
            print("Decreasing counter of",s[l], "to", counter[s[l]])
            _max = max(_max, r - l + 1)

    print("l: ",l)
    print("r: ",r)
    print("_max: ",_max)
    print("counter: ",counter)

    return _max

print("Resposta: ",maximumLengthSubString("","bcbbcba"))
