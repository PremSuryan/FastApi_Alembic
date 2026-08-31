""" 
Given array of the  positive integers nums and a positive integer target 

Input : target = 7
nums = [2,3,1,2,4,3]
output:2 eg subarray =[4,3]
"""
nums = [2,3,1,2,4,3,6,1]
target = 7
out=[]
for i in range(len(nums)):
    left = nums.index(nums[i]) + 1

    if nums[i] == target:
        out.append([i])
    while left<len(nums)-1:
        while nums[left]+nums[i] == target:
            out.append(sorted([i,left]))
            left += 1
        left += 1
                
# print(out)
sequence = [arr for arr in out if all( arr[i]+1==arr[i+1] for i in range(len(arr)-1))]
res = min(sequence ,key=len)
print(res)


#gpt approach:
# left = 0
# total = 0
# min_len = float("inf")
# result = []

# for right in range(len(nums)):
#     total += nums[right]

#     while total >= target:
#         current_len = right - left + 1

#         if current_len < min_len:
#             min_len = current_len
#             result = nums[left:right + 1]

#         total -= nums[left]
#         left += 1

# print(result)