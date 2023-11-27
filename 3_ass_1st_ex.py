#1st ex



def permutations(n):
    def permute(nums, start, end):
        if start == end:
            yield nums
        else:
            for i in range(start, end + 1):
                nums[start], nums[i] = nums[i], nums[start]
                yield from permute(nums, start + 1, end)
                nums[start], nums[i] = nums[i], nums[start]

    total_permutations = 1
    for i in range(1, n + 1):
        total_permutations *= i

    print(total_permutations)
    for perm in permute(list(range(1, n + 1)), 0, n - 1):
        print(' '.join(map(str, perm)))

n = 5  
permutations(n)

