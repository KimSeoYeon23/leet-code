class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        split_str = list(s.split(" "))
        none_space = ' '.join(split_str).split()
        last_str = none_space[-1]
        return len(''.join(last_str))
        