class Solution:
    def calculate(self, s: str) -> int:
        def helper(i: int):
            def update(sign, num):
                if sign == "+":
                    stack.append(num)
                if sign == "-":
                    stack.append(-num)
                if sign == "*":
                    stack.append(stack.pop() * num)
                if sign == "/":
                    stack.append(int(stack.pop() / num))
        
            num, sign, stack = 0, "+", []

            while i < len(s):
                if s[i].isdigit():
                    num = (num * 10) + int(s[i])
                elif s[i] in "+-/*":
                    update(sign, num)
                    sign, num = s[i], 0
                elif s[i] == "(":
                    num, j = helper(i+1)
                    i = j - 1
                elif s[i] == ")":
                    update(sign, num)
                    return sum(stack), i + 1
                i += 1
            update(sign, num)
            return sum(stack)
        return helper(0)
        
