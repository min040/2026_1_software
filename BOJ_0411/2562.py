nums = [int(input()) for _ in range(9)]
mx = max(nums)

print(mx)
print(nums.index(mx) + 1)