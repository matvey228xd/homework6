text = input("Введіть слово: ")
shift = 3

result = ""

for letter in text:
    new_letter = chr((ord(letter) - ord('a') + shift) % 26 + ord('a'))
    result += new_letter

print(f'Зашифрований текст: "{result}"')