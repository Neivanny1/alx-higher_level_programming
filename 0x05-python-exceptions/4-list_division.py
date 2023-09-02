#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    ans = []
    for i in range(0, list_length):
        try:
            ans.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            ans.append(0)
            print("wrong type")
            continue
        except ZeroDivisionError:
            ans.append(0)
            print("division by 0")
            continue
        except IndexError:
            ans.append(0)
            print("out of range")
            continue
        finally:
            pass
    return ans
