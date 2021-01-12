#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time: 2021/1/11 下午4:23
# @Author: Bruce Chen
# @Site: 
# @File: leetcode_1122.py
# @Software: PyCharm

"""
给你两个数组，arr1 和 arr2，

    arr2 中的元素各不相同
    arr2 中的每个元素都出现在 arr1 中

对 arr1 中的元素进行排序，使 arr1 中项的相对顺序和 arr2 中的相对顺序相同。未在 arr2 中出现过的元素需要按照升序放在 arr1 的末尾。

示例：

输入：arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
输出：[2,2,2,1,4,3,3,9,6,7,19]


提示：

    1 <= arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    arr2 中的元素 arr2[i] 各不相同
    arr2 中的每个元素 arr2[i] 都出现在 arr1 中
"""
from collections import Counter
class Solution:
    def relativeSortArray(self, arr1, arr2):
        """
        :param arr1: list[int]
        :param arr2: list[int]
        :return: list[int]
        """
        dic1 = Counter(arr1)
        result = []
        tmp = []
        for key in arr2:
            for i in range(dic1[key]):
                result.append(key)
        for j in arr1:
            if j not in arr2:
                tmp.append(j)
        result.extend(sorted(tmp))
        return result



if __name__ == "__main__":
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    test = Solution()
    result = test.relativeSortArray(arr1, arr2)
    print(result)
