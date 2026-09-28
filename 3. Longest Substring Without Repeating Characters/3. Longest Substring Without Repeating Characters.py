class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0

        for i in range(len(s)):
            chars = set()

            for j in range(i, len(s)):
                if s[j] in chars:
                    break

                chars.add(s[j])

                length = max(length, j - i + 1)

        return length