 
 
# Find the longest substring without repeating characters:
# Given a string s, find the length of the longest substring that contains no repeated characters.
# NOTE: You must find a contiguous substring (not subsequence).
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.
# Example 2:
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Constraints:
# 1 <= s.length <= 50,000
# s consists of:
# lowercase letters
# uppercase letters
# digits
# symbols
# spaces

def lengthOfLongestSubstring(s: str) -> int:
    char_set = set()
    left = 0
    max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


# ----- User input -----
s = input("Enter a string: ")

result = lengthOfLongestSubstring(s)

print("Length of the longest substring without repeating characters:", result)
