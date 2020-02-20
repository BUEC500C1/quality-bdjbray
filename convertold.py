def convert(input):
    ints = (1000, 500, 100, 50, 10,5, 1)
    nums = ('M', 'D', 'C', 'L','X','V','I')
    result = []
    for i in range(len(ints)):
        count = int(input / ints[i])
        result.append(nums[i] * count)
        input -= ints[i] * count
    return ''.join(result)







res=convert(6700)
print("the result is:",res)

#l        I   V   X   L   C   D   M
#Value   1   5   10  50  100 500 1,000