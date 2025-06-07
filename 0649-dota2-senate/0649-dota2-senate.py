class Solution(object):
    def predictPartyVictory(self, senate):
        n = len(senate)

        r_arr = [i for i in range(n) if senate[i] == 'R']
        d_arr = [j for j in range(n) if senate[j] == 'D']
        
        while r_arr and d_arr:
            r = r_arr.pop(0)
            d = d_arr.pop(0)
            if r < d:
                r_arr.append(r + n)
            else:
                d_arr.append(d + n)
                
        return 'Radiant' if r_arr else 'Dire'
