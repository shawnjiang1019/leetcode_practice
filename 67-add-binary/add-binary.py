class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""

        if len(a) < len(b):
            a, b = b, a
        
        carry = 0
        j = len(b) - 1
        for i in range(len(a) - 1, -1, -1):
            a_bit = int(a[i])
            bit_sum = a_bit + carry

            if j >= 0:
                bit_sum += int(b[j])
                j -= 1
            
            bit = bit_sum % 2
            carry = bit_sum // 2
            result += str(bit)
        if carry > 0:
            result += "1"
        return result[::-1]