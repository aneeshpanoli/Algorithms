# This is a sandbox to experiment with CoderPad's execution capabilities.
# It's a temporary, throw-away session only visible to you.
'''
Few questions:
edge cases:
input:
output:

EXAMPLES:
'(())())' -> invalid
'({)}' -> invalid
'(()(()))' -> 3

Keep track of the opening brackets in mind -> general idea here is
to  use a queue or stack as short term memory. Here
a stack is ideal
I could also use a counter - increment everytime I see a opening bracket
decrement when you see a closing: Once I finish iterating if the counter is greater than 0 then -- its not balanced
'''
def find_depth(s):
    brace_counter = 0
    max_depth = 0
    for b in s:
        if b == '(':
            brace_counter += 1
            max_depth = max(brace_counter, max_depth)
        elif b == ')':
            brace_counter -= 1
    if brace_counter != 0:
        return -1
    return max_depth

def find_depth_any(s):
    stack = []
    max_depth = 0
    brackets = {'(':')', '{':'}', '[':']'}
    pipe_counter = 0
    for b in s:
        if b in brackets:
            stack.append(b)
            max_depth = max(max_depth, len(stack))
        elif b in set(brackets.values()):
            if not stack or b != brackets[stack[-1]]:
                return -1
            stack.pop()
        elif b == '|':
            if pipe_counter > 0 and stack[-1] == b:
                pipe_counter -= 1
                stack.pop()
            else:
                pipe_counter += 1
                stack.append(b)
                max_depth = max(max_depth, len(stack))
    if pipe_counter != 0:
        return -1

    return max_depth
            
    
    
print(find_depth_any('(())(){{{||}}}||'))
