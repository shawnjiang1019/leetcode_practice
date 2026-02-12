class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        # very important observation: a smaller substring will always occur more than longer
        # just test substrings of minSize

        str_freq = {}
        for i in range(len(s) - minSize + 1):
            substring = s[i : i + minSize]
            if len(set(substring)) <= maxLetters:
                if substring not in str_freq:
                    str_freq[substring] = 1
                else:
                    str_freq[substring] += 1
        if str_freq:
            return max(str_freq.values())
        return 0


                

        