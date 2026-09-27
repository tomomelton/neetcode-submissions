class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opps = ['+','-','*','/']
        stack = []
        for x in tokens:
            if x in opps:
                opr1 = stack.pop()
                opr2 = stack.pop()
                if x == '+':
                    stack.append(opr1 + opr2)
                elif x == '-':
                    stack.append(opr2 - opr1)
                elif x == '*':
                    stack.append(opr1 * opr2)
                elif x == '/':
                    stack.append(int(opr2 / opr1))
            else:
                stack.append(int(x))
        return stack[0]
