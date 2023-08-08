#!/usr/bin/python3
#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number *= -1
        last = abs(number % 10)
    else:
        last = abs(number % 10)
    print("{}".format(last), end="")
    return last
