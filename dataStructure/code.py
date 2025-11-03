def longestSubstring(s: str) -> int:
    l = 0
    counter = {}
    max_len = 0

    for r in range(len(s)):
        counter[s[r]] = counter.get(s[r], 0) + 1
        while counter[s[r]] > 1:
            counter[s[l]] -= 1
            l += 1
        max_len = max(max_len, r - l + 1)
    return max_len
print(longestSubstring("abcabcbb"))  # 3
