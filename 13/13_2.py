# БСБО-05-19 Савранский Сергей

nums = [int(input("Num >> ")) for i in range(int(input("N >> ")))]
nums.sort(reverse=True)
for num in nums:
    print(num)