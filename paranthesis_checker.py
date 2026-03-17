"""Given a string s, composed of different combinations of '(' , ')', '{', '}', '[', ']'. Determine whether the Expression is balanced or not.
An expression is balanced if:

Each opening bracket has a corresponding closing bracket of the same type.
Opening brackets must be closed in the correct order."""

def isBalanced(s):
    arr = []

    for i in range(len(s)):
        if s[i] == "[" or s[i] == "{" or s[i] == "(":
            arr.append(s[i])
        else:
            if not arr:
                return False

            top = arr.pop()

            if ((s[i] == "]" and top != "[") or
                (s[i] == "}" and top != "{") or
                (s[i] == ")" and top != "(")):
                return False

    return len(arr) == 0


# Test
s = "[{()}]"
print(isBalanced(s))
