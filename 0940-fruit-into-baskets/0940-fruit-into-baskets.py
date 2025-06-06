class Solution(object):
    def totalFruit(self, fruits):
        max_len = 0
        fruit_count = {}
        left = 0

        for right in range(len(fruits)):
            fruit = fruits[right]
            fruit_count[fruit] = fruit_count.get(fruit, 0) + 1

            while len(fruit_count) > 2:
                left_fruit = fruits[left]
                fruit_count[left_fruit] -= 1
                if fruit_count[left_fruit] == 0:
                    del fruit_count[left_fruit]
                left += 1

            max_len = max(max_len, right - left + 1)

        return max_len
