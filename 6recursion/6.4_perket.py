def process_input(input_str, s_product=1, b_sum=0, idx=0):
    if input_str == "":
        return abs(s_product - b_sum)
    
    comma_idx = input_str.find(',')
    if comma_idx == -1:
        pair = input_str
        space_idx = pair.find(' ')
    else:
        pair = input_str[:comma_idx]
        space_idx = pair.find(' ')

    s = int(pair[:space_idx])
    b = int(pair[space_idx + 1:])

    if comma_idx == -1:
        return process_input("", s_product * s, b_sum + b, idx + 1)
    else:
        return process_input(input_str[comma_idx + 1:], s_product * s, b_sum + b, idx + 1)

user_input = input("Enter Input : ")
result = process_input(user_input)
print(result)