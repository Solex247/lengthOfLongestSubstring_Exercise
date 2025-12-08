# lengthOfLongestSubstring_Exercise
An optimized Python solution to the Longest Substring Without Repeating Characters problem using the sliding window algorithm, achieving O(n) time complexity and clean, readable code.


# Longest Substring Without Repeating Characters

## Problem Description

Given a string `s`, find the length of the **longest substring** that contains no repeated characters.

**Note:** You must find a contiguous substring (not subsequence).

## Examples

### Example 1:
```
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Note that "bca" and "cab" are also correct answers.
```

### Example 2:
```
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
```

## Constraints

- `1 <= s.length <= 50,000`
- `s` consists of:
  - lowercase letters
  - uppercase letters
  - digits
  - symbols
  - spaces

## Solution Approach

### Algorithm: Sliding Window with Hash Map

The solution uses the **sliding window technique** combined with a hash map to efficiently track characters and their positions.

#### Key Concepts:

1. **Sliding Window**: Maintain a window `[left, right]` that contains no repeating characters
2. **Hash Map**: Store the last seen index of each character
3. **Two Pointers**: 
   - `right` pointer expands the window
   - `left` pointer shrinks the window when duplicates are found

#### How It Works:

1. Initialize an empty hash map and set `left = 0`
2. Iterate through the string with `right` pointer
3. For each character:
   - If it's already in the window (exists in map and index >= left):
     - Move `left` to the position after the last occurrence
   - Update the character's index in the map
   - Calculate current window size and update max length
4. Return the maximum length found

#### Visual Example:

```
String: "abcabcbb"

Step 1: a
Window: [a]     left=0, right=0, max_len=1

Step 2: ab
Window: [ab]    left=0, right=1, max_len=2

Step 3: abc
Window: [abc]   left=0, right=2, max_len=3

Step 4: abca (duplicate 'a')
Window: [bca]   left=1, right=3, max_len=3

Step 5: abcab (duplicate 'b')
Window: [cab]   left=2, right=4, max_len=3

Step 6: abcabc (duplicate 'c')
Window: [abc]   left=3, right=5, max_len=3

Step 7: abcabcb (duplicate 'b')
Window: [cb]    left=5, right=6, max_len=3

Step 8: abcabcbb (duplicate 'b')
Window: [b]     left=7, right=7, max_len=3

Result: 3
```

### Complexity Analysis

- **Time Complexity**: O(n)
  - We traverse the string once with the right pointer
  - The left pointer only moves forward, never backward
  - Each character is visited at most twice (once by right, once by left)

- **Space Complexity**: O(min(m, n))
  - m = size of the character set
  - n = length of the string
  - In the worst case, we store all unique characters in the hash map

## Implementation

The solution is implemented in Python with two main functions:

1. `length_of_longest_substring(s)`: Returns the length of the longest substring
2. `get_longest_substring(s)`: Returns the actual substring (for verification)

## Running the Code

### Prerequisites
- Python 3.6 or higher

### Execute the solution:

```bash
python longest_substring.py
```

This will:
- Run comprehensive test cases
- Display results for each test
- Show interactive examples

### Run tests only:

```bash
python -m pytest test_longest_substring.py -v
```

## Test Cases

The solution includes comprehensive test cases covering:

- ✓ Basic examples from the problem
- ✓ Edge cases (empty string, single character)
- ✓ All same characters
- ✓ All unique characters
- ✓ Strings with spaces
- ✓ Mixed case sensitivity
- ✓ Strings with digits and symbols
- ✓ Various repeating patterns

## Files

- `longest_substring.py` - Main solution implementation
- `test_longest_substring.py` - Unit tests using pytest
- `README.md` - This documentation
- `requirements.txt` - Python dependencies

## Alternative Approaches

### 1. Brute Force (Not Recommended)
- Check all possible substrings
- Time: O(n³), Space: O(min(m, n))

### 2. Sliding Window with Set
- Use a set instead of hash map
- Requires shrinking window one character at a time
- Time: O(2n) = O(n), Space: O(min(m, n))

### 3. Optimized Sliding Window (Current Implementation)
- Use hash map to jump directly to the correct position
- Time: O(n), Space: O(min(m, n))
- **Best approach** ✓

## Author

Solution for the Longest Substring Without Repeating Characters problem.

## License

MIT License

