import string
import random

#userul alege lungimea parolei
#caractere mari, mici, numere, speciale - poate sa aleaga mai multe
#se genereaza o parola random

char_no = 0
while char_no == 0:
    try:
        char_no = int(input("Introdu nr de caractere: "))
    except ValueError:
        print("Tre sa fie int. ", end="")

options = "0"

lower_chars = list(string.ascii_lowercase)
upper_chars = list(string.ascii_uppercase)
digit_chars = [str(x) for x in range(10)]
special_chars = list('!@#$%^&*()-+{}:;|')

selected_chars = []

characters = ['a', 'A', '1', '!']
final_list = []
def generate_list():
    options = input("Ce fel de caractere (a - litere mici, A - litere mari, 1 - numere, ! - speciale): ")
    for opt in options:
        if opt in characters:
            match opt:
                case 'a':
                    selected_chars.append(lower_chars)
                case 'A':
                    selected_chars.append(upper_chars)
                case '1':
                    selected_chars.append(digit_chars)
                case '!':
                    selected_chars.append(special_chars)
    if selected_chars == []:
        generate()
    else:
        for lst in selected_chars:
            for el in lst:
                final_list.append(el)

generate_list()

print("Parola generate este:",''.join(random.sample(final_list, char_no)))


