class Solution:
    def isHappy(self, n: int) -> bool:

        squares = set()
        
        while n != 1:
            product = 0
            
            while n:
                digit = n % 10
                digit = digit ** 2
                product += digit
                n = n // 10

            if product in squares:
                return False

            squares.add(product)
            n = product

        return True
