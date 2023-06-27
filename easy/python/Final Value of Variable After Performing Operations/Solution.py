class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """

        x = 0

        for op in operations:
            if op == "++X":
                x += 1
            elif op == "X++":
                x += 1
            elif op == "--X":
                x -= 1
            elif op == "X--":
                x -= 1
            else:
                print("Should be nonenterable.")

        return x