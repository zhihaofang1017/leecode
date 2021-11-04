def intToRoman(num):
    """
    :type num: int
    :rtype: str
    """
    num_list = list(str(num))
    result = ""
    for i in range(0, len(num_list)):
        if len(num_list) - i == 4:
            result = result + "M" * int(num_list[i])
        elif len(num_list) - i == 3:
            result = result + calculate("C.py", "D", "M", int(num_list[i]))
        elif len(num_list) - i == 2:
            result = result + calculate("X", "L", "C.py", int(num_list[i]))
        elif len(num_list) - i == 1:
            result = result + calculate("I", "V", "X", int(num_list[i]))
    print(result)

def calculate(a, b, c, num):
    if num < 4:
        return a * num
    elif num == 4:
        return a + b
    elif num < 9:
        return b + a * (num - 5)
    else:
        return a + c

intToRoman(3)
