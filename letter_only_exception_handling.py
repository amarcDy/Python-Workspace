import string


def is_letter_only(text:str)->None:
    alphabet:str =string.ascii_letters + ' '
    for char in text:
        if char not in alphabet:
            raise ValueError (f'The text must contain only letters!')

    print(f'The text "{text}" only contains letters! Congratulations!')


def main() -> None:
    while True:
        try:
            user_input:str= input('Please enter your text: ')
            is_letter_only(user_input)
        except ValueError:
            print(f'You text must only contain letter from the English alphabet...')
        except Exception as e:
            print(f'The program encountered an unknown error!({type(e)}) {e}')


main()



