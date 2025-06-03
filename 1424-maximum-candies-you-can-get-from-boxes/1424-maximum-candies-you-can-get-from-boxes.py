class Solution(object):
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        hasBox = [False] * n
        canOpen = status[:]
        visited = [False] * n

        from collections import deque
        queue = deque()

        # Collect initial boxes
        for box in initialBoxes:
            hasBox[box] = True
            if canOpen[box]:
                queue.append(box)

        totalCandies = 0

        while queue:
            box = queue.popleft()
            if visited[box]:
                continue
            visited[box] = True
            totalCandies += candies[box]

            # Collect new keys
            for key in keys[box]:
                if not canOpen[key]:
                    canOpen[key] = 1
                    if hasBox[key] and not visited[key]:
                        queue.append(key)

            # Collect contained boxes
            for contained in containedBoxes[box]:
                hasBox[contained] = True
                if canOpen[contained] and not visited[contained]:
                    queue.append(contained)

        return totalCandies
