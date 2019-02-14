#Una palabras es palindromo

def palindrome(word):
    reversedWord = word[::-1]
    if word.lower() == reversedWord.lower():
        print('"{}" SI es palindromo'.format(word))
    else:
        print('"{}" NO es palindromo'.format(word))

if __name__ == '__main__':
    word = str(input('Escribe una palabra: '))
    palindrome(word)
