class Solution(object):
    def maxDiff(self, num):
        
        num_str = str(num)

        # Maximize the number by replacing first non-9 digit with 9
        for d in num_str:
            if d != '9':
                max_num = int(num_str.replace(d, '9'))
                break
        else:
            max_num = num  # already all 9s

        # Minimize the number
        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        else:
            for d in num_str[1:]:
                if d != '0' and d != '1':
                    min_num = int(num_str.replace(d, '0'))
                    break
            else:
                min_num = num  # nothing to change

        return max_num - min_num
