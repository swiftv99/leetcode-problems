"""
Problem Number: 20. Valid Parentheses
Difficulty Level: Easy
https://leetcode.com/problems/valid-parentheses

********************************************************************************

Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if: Open brackets must be closed by the same type of brackets. Open brackets must be closed in 
the correct order. Every close bracket has a corresponding open bracket of the same type.
  
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
  
Constraints:
1 <= s.length <= 10^4
s consists of parentheses only '()[]{}'.
"""


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in {"(", "[", "{"}:
                stack.append(char)
            elif len(stack) > 0 and \
                ((stack[-1] == "[" and char == "]") or
                 (stack[-1] == "{" and char == "}") or
                 (stack[-1] == "(" and char == ")")):
                stack.pop()
            else:
                return False
        return len(stack) == 0

# Time Complexity: O(n)
# Space Complexity: O(n)
