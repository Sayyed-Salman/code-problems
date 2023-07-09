class TwoSum:

    def __init__(self, arr: list) -> None:
        self.arr = arr
        self.arr.sort()

    def two_sum(self, target: int) -> list[int]:

        history = {}

        for i, n in enumerate(self.arr):
            diff = target - n
            if diff in history:
                return [history[diff], i]
            history[n] = i


arr = [2, 1, 5, 6, 7, 0]
target = 8

two_sum = TwoSum(arr)
result = two_sum.two_sum(8)
print(result)
