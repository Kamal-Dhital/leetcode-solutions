class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        square_root = int(num**0.5)
        return (square_root * square_root == num)