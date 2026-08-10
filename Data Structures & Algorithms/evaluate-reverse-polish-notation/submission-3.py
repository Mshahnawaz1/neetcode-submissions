class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # postfix evaluation
        stack = []
        for char in tokens:
            if stack and char in "+-*/":
                c1 = stack.pop()
                c2 = stack.pop()
                # concatenate all the string into one expression and evaluate into int

                stack.append(int(eval(f"{c2} {char} {c1}")))
            else:
                stack.append(int(char))

        return stack.pop()

        