def length(txt, idx=0, modified_txt=""):
    if txt == "":
        return modified_txt, idx
    char = txt[0]
    modified_txt += char
    if idx % 2 == 0:
        modified_txt += "*"
    else:
        modified_txt += "~"
    return length(txt[1:], idx + 1, modified_txt)

user_input = input("Enter Input : ")
modified_text, text_length = length(user_input)
print(f"{modified_text}\n{text_length}")