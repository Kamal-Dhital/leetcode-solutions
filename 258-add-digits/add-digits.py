class Solution:
    def addDigits(self, num: int) -> int:
        if (num < 10):
            return num
        else:
            return Solution.addDigits(self, ((num // 10) + (num % 10)))