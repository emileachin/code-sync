class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""
            
        min_word_len = min(len(word) for word in strs)
        first_word = strs[0]

        for i in range(min_word_len):
            char = first_word[i]

            for word in strs:
                if char != word[i]:
                    return strs[0][:i]
        return first_word[:min_word_len]