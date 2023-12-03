def count_down(n: int):
    if n <= 0:
        return "Cheers"
    else:
        print(f"I am at {n}")
        return count_down(n - 1)


print(count_down(5))
