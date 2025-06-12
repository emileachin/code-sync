class Solution(object):
    def romanToInt(self, s):
        romanNums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        total = 0
        prev = 0

        for i in s:
            currVal = romanNums[i]
            total += (currVal - prev - prev) if (currVal > prev) else currVal
            prev = currVal

        return total