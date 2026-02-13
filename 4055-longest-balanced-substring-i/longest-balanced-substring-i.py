class Solution:
    def longestBalanced(self, s: str) -> int:
        # find the longest balanced substring starting at every possible start
        max_length = 0
        for left in range(len(s)):
            cur_string = ""
            freq = {}
            for right in range(left, len(s)):
                cur_string += s[right]
                if s[right] not in freq:
                    freq[s[right]] = 1
                else:
                    freq[s[right]] += 1
                if len(set(freq.values())) == 1 :
                    max_length = max(max_length, right - left + 1)
        return max_length
                     
                
