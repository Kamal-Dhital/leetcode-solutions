class Solution:
    def addDigits(self, num: int) -> int:
        if (num < 10):
            return num
        else:
            quotient = num // 10
            remainder = num % 10
            sum_of_number = quotient + remainder
            return Solution.addDigits(self, sum_of_number)