"""Write a function that takes an array of numbers (integers for the tests) and a target number. It should find two
different items in the array that, when added together, give the target value. The indices of these items should then be
returned in a tuple / list (depending on your language) like so: (index1, index2).

For the purposes of this kata, some tests may have multiple answers; any valid solutions will be accepted.

The input will always be valid (numbers will be an array of length 2 or greater, and all of the items will be numbers;
target will always be the sum of two different items from that array).

Based on: http://oj.leetcode.com/problems/two-sum/
two_sum([1, 2, 3], 4) # returns [0, 2] or [2, 0]"""

#Basically, I need to test all possibilities and find the first one where the sum of x and y equals the target value.
# To avoid redundant operations, I will discard the x element from the y list. For example, given [1, 2, 3],
# I will calculate 1+2 and 1+3, but then only calculate 2+3.
def two_sum(numbers, target):
    size = len(numbers)
    for x in range(0,len(numbers)):
        for y in range(x+1,len(numbers)):
            if numbers[x]+numbers[y] == target:
                return[x,y]
    return []