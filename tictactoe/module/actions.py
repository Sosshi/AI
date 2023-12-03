def test(x):
    if x == 1:
        return 1
    x = test(x - 1)
    print(x)


test(10)
