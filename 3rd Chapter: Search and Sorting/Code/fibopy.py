def get_fibo(position):
    if 0 <= position <= 1:
        return position
    else:
        return get_fibo(position - 1) + get_fibo(position - 2)


print(get_fibo(3))
print(get_fibo(4))
