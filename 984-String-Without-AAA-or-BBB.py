class Solution:
    def strWithout3a3b(self, A: int, B: int) -> str:
        if A < 3 and B < 3:
            return 'a' * A + 'b' * B
        if A == B:
            return 'ab' * A
        if A > B:
            long = ['a', A]
            short = ['b', B]
        else:
            long = ['b', B]
            short = ['a', A]
        ret = ''
        n = short[1]
        slot_2 = long[1] - (n + 1)  # number of 'aa'
        slot_1 = n + 1 - slot_2     # number of 'a'
        if slot_1 == 0:
            ret = (slot_2 - 1) * (2 * long[0] + short[0]) + 2 * long[0]
        else:
            ret = slot_2 * (2 * long[0] + short[0]) + (slot_1 - 1) * (long[0] + short[0]) + long[0]
            
        return ret