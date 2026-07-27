inp = "3[a2[c]]"
#output : "accaccacc"


#"3[a2[c]]" ----> 3a2c


def decode_str(s):
    stack = []
    current_number = 0
    current_string = ""

    for i in s:
        if i.isdigit():
            current_number = current_number * 10  + int(i)

        elif i == "[":
            stack.append((current_string, current_number))
            current_string = ""
            current_number = 0

        elif i == "]":
            previous_string, repeat = stack.pop()
            current_string = previous_string + current_string * repeat

        else:
            current_string += i


    return current_string


print(decode_str(inp))