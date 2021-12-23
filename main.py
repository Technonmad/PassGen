import random


def createPassword(lang):
    mas = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
           'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
           'I',
           'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', '$', '%',
           '&',
           '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', ']', '^', '_', '`', '{', '|',
           '}', '~']
    if lang == '1':
        print("Выберите размерность пароля\n\t[1]\t8-16\n\t[2]\t16-32")
        length = input()
        if length == '1':
            count = 0
            pas = ""
            while count < 16:
                i = random.randrange(0, len(mas))
                pas += mas[i]
                count += 1
            print("Ваш пароль готов: ", pas)
    if lang == '2':
        print("Choose the password length")
    createPassword(lang)

print(''' _____      __      ____    ____     __      __    ___
/\ '__`\  /'__`\   /',__\  /',__\  /'_ `\  /'__`\/' _ `\ 
\ \ \L\ \/\ \L\.\_/\__, `\/\__, `\/\ \L\ \/\  __//\ \/\ \ 
 \ \ ,__/\ \__/.\_\/\____/\/\____/\ \____ \ \____\ \_\ \_\ 
  \ \ \/  \/__/\/_/\/___/  \/___/  \/___L\ \/____/\/_/\/_/
   \ \_\                             /\____/
    \/_/                             \_/__/''')
print("\n[1]\tРусский\n[2]\tEnglish")
lang = input()

while lang != "exit":
    createPassword(lang)
    lang = input()
