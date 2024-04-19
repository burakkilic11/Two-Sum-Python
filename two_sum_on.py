class Solution(object):
    def twoSum(self, nums, target):
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return[i, pair_idx[target - num]]
            pair_idx[num] = i

def test_two_sum():
    solution = Solution()

    # Test case 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = solution.twoSum(nums1, target1)
    assert sorted(result1) == sorted([0, 1]), f"Test case 1 failed. Result: {result1}"

    # Test case 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = solution.twoSum(nums2, target2)
    assert sorted(result2) == sorted([1, 2]), f"Test case 2 failed. Result: {result2}"

    # Test case 3
    nums3 = [3, 3]
    target3 = 6
    result3 = solution.twoSum(nums3, target3)
    assert sorted(result3) == sorted([0, 1]), f"Test case 3 failed. Result: {result3}"

    print("All test cases passed successfully!")

if __name__ == "__main__":
    test_two_sum()