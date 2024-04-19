class Solution(object):
    def twoSum(self, nums, target):
        ans = []
        if len(nums) == 2:
            return[0,1]
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    ans.append(i)
                    ans.append(j)
                    return ans

def test_two_sum():
    solution = Solution()

    # Test 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    assert solution.twoSum(nums1, target1) == [0, 1], "Test 1 failed"

    # Test 2:
    nums2 = [3, 2, 4]
    target2 = 6
    assert solution.twoSum(nums2, target2) == [1, 2], "Test 2 failed"

    # Test 3:
    nums3 = [-1, -2, -3, -4, -5]
    target3 = -8
    assert solution.twoSum(nums3, target3) == [2, 4], "Test 3 failed"

    # Test 4:
    nums4 = [3, 3]
    target4 = 6
    assert solution.twoSum(nums4, target4) == [0, 1], "Test 4 failed"

    print("All tests passed successfully!")

if __name__ == "__main__":
    test_two_sum()



