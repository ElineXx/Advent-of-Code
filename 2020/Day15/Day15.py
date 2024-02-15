# 1
nums = [0, 13, 16, 17, 1, 10, 6]
nums.reverse()

while len(nums) < 2020:
    if nums[0] in nums[1:]:
        nums.insert(0, nums[1:].index(nums[0]) + 1)
    else:
        nums.insert(0, 0)

print(nums[0])

# 2
nums = [0, 13, 16, 17, 1, 10, 6]
age_dict = {}
for i, num in enumerate(nums, 1):
    age_dict[num] = i

counter = len(nums)
current_num = nums[-1]
while counter < 30000000:
    if current_num in age_dict:
        old_age = age_dict[current_num]
        age_dict[current_num] = counter
        current_num = counter - old_age
    else:
        age_dict[current_num] = counter
        current_num = 0
    counter += 1

print(current_num)
