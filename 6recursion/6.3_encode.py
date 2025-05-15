def encode_char(character, shift_position):
    if character.isupper():
        return chr((ord(character) - ord('A') + shift_position) % 26 + ord('A'))
    elif character.islower():
        return chr((ord(character) - ord('a') + shift_position) % 26 + ord('a'))
    else:
        return character

def decode_char(character, shift_position):
    if character.isupper():
        return chr((26 + ord(character) - ord('A') - shift_position) % 26 + ord('A'))
    elif character.islower():
        return chr((26 + ord(character) - ord('a') - shift_position) % 26 + ord('a'))
    else:
        return character

def encode_message(text, shift_position):
    if text == '':
        return ''
    if shift_position == 26:
        shift_position += 1
    return encode_char(text[0], shift_position) + encode_message(text[1:], shift_position + 1)

def decode_message(cipher_text, shift_position):
    if cipher_text == '':
        return ''
    if shift_position == 26:
        shift_position += 1
    return decode_char(cipher_text[0], shift_position) + decode_message(cipher_text[1:], shift_position + 1)

print("This is Caesar cipher")
plain_text, initial_shift_position = input("Enter Input : ").split(',')
encoded_text = encode_message(plain_text, int(initial_shift_position))
print("Encoded Message:", encoded_text)
decoded_text = decode_message(encoded_text, int(initial_shift_position))
print("Decoded Message:", decoded_text)