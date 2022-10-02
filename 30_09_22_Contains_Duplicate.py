class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        new_set = set()
        for i in range(len(nums)):
            if nums[i] in new_set:
                print(new_set)
                return True
            else:
                new_set.add(nums[i])
        print(new_set)
        return False