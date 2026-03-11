class Solution(object):
    def bitwiseComplement(self, n):
        b = bin(n)[2:]      # remove '0b'
        
        res = ""
        for i in b:
            if i == '0':
                res += '1'
            else:
                res += '0'
        
        return int(res, 2)

        
        