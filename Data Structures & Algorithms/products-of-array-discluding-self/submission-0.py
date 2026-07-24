class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_products = [0] * (len(nums))
        prefix_products[0] = 1
        for i, n in enumerate(nums):
            if not i:
                continue
            prefix_products[i] = prefix_products[i-1] * nums[i-1]
        
        suffix_products = [0] * (len(nums))
        suffix_products[-1] = 1
        for i in range(len(nums)-2, -1, -1):
            suffix_products[i] = suffix_products[i+1] * nums[i+1]
        
        print(prefix_products)
        print(suffix_products)

        return [prefix_products[i] * suffix_products[i] for i in range(len(nums))]


        