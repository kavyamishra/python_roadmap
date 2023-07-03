def natural(n):
    breakpoint()
    if n==1:
        return 1
    return natural(n-1)+n
print(natural(5))

"""
15
5 -> 10 + 5
4 -> 6 + 4
3 -> 3 + 3
2 -> 1 + 2
1 -> 1
"""