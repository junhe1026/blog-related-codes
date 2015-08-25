# -*- coding: utf-8 -*-


__author__ = 'Juno He<hejun@immengxin.com>'


class Solution(object):
    @classmethod
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        length = len(nums)
        for i in range(length):
            for j in range(i, length):
                if nums[i]+nums[j] == target:
                    return [i,j]


if __name__ == '__main__':
    r = Solution.twoSum([2, 7, 11, 15], 9)
    print(r)
    pass
