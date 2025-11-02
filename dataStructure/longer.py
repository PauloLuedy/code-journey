class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pre = []
        for i in range(len(strs[0])):
            for s in strs:
                if s[i] != strs[0][i]:
                    return ''.join(pre)
            pre.append(strs[0][i])
        return ''.join(pre)