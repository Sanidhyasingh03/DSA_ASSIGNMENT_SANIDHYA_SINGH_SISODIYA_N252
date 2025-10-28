# ✅ DSA Assignment - Problem 2 (Stack)
# Program to check Balanced Parentheses using Stack
 
def isBalanced(expression):
    stack = []  # Stack to store opening brackets
 
    # Dictionary to match closing bracket with its opening
    matching = {')': '(', '}': '{', ']': '['}
 
    # Traverse each character of the string
    for char in expression:
        # If opening bracket → push into stack
        if char in "({[":
            stack.append(char)
        else:
            # If stack empty or mismatch → Not Balanced
            if not stack or stack.pop() != matching.get(char):
                return False
    
    # If at end stack empty → Balanced, else Not Balanced
    return len(stack) == 0
 
 
# ✅ Taking input from user
expression = input("Enter bracket expression: ")
 
# ✅ Printing final result
if isBalanced(expression):
    print("Balanced ✅")
else:
    print("Not Balanced ❌")
 