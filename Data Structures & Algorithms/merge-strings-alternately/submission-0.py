class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n = len(word1)
        m = len(word2)

        merged = []

        for i in range(min(n, m)):
            merged.append(word1[i])
            merged.append(word2[i])

        if n < m:
            merged.append(word2[n:])
        elif m < n:
            merged.append(word1[m:])

        return "".join(merged)


