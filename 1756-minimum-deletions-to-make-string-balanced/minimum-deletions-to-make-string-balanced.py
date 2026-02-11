class Solution:
    def minimumDeletions(self, s: str) -> int:
        # condition: all a must be before b
        # either remove all Bs before an index and all As after an index
        if len(s) == 1:
            return 0
        idx = -1
        a_count, b_count = [0 for i in range(len(s))], [0 for i in range(len(s))]
        for i in range(len(s)):
            if i == 0:
                if s[i] == "a":
                    a_count[0] = 1
                if s[i] == "b":
                    b_count[0] = 1
            else:
                if s[i] == "a":
                    a_count[i] = a_count[i - 1] + 1
                    b_count[i] = b_count[i - 1]
                else:
                    a_count[i] = a_count[i - 1]
                    b_count[i] = b_count[i - 1] + 1
        min_deletions = a_count[-1]
        for i in range(len(s)):
            
            b_before = b_count[i]
            a_after = a_count[-1] - a_count[i]
            deletions = b_before + a_after
            if deletions < min_deletions:
                idx = i
                min_deletions = deletions
        # print(idx)
        # print(a_count)
        # print(b_count)
        return min_deletions



                
            
            
