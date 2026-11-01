class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        for i in range(len(numbers)):
            find = target - numbers[i]

            r = len(numbers)-1
            l = i + 1

            while l <= r:
                m = (r+l)//2

                if numbers[m] > find:
                    r = m - 1
                elif numbers[m] < find:
                    l = m + 1
                else:
                    if i != m :
                        return [i+1,m+1]