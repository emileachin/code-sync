class Solution(object):
    def isValid(self, s):
        brackets = {"(":")", "{":"}", "[": "]"}
        track = []

        for bracket in s:
            if bracket in brackets:
                track.append(bracket)
            elif len(track) == 0 or brackets[track.pop()] != bracket:
                return False
        return len(track) == 0