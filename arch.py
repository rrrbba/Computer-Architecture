# 2 ** 0 = 1
# 2 ** 1 = 2
# 2 ** 2 = 4
# 2 ** 3 = 8
# 2 ** 4 = 16
# 2 ** 5 = 32
# 2 ** 6 = 64
# 2 ** 7 = 128
# 2 ** 8 = 256
# 2 ** 9 = 512
# 2 ** 10 = 10231


# 0b -> 0x #binary to hexidecimal
# 1010 0011
# 8+2 =10 -> A
# A 3

for A in [False, True]:
    for B in [False, True]:
        print(f"{A} - {B} -- {(not A or not B)}")

2 in binary is 10 (there is a true at the place where 2 is)