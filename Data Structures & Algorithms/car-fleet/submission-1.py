class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        stack = []
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        for p, s in pair:
            time = (target - p) / s

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)