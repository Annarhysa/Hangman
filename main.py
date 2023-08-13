import random

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    with open("Hangman/words.txt", "r") as words:
        line = words.readlines()
    # wordlist: list of strings
    # wordlist = line.split()
    print(len(line), "words loaded.")
    return line

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for i in secretWord:
        if i not in lettersGuessed:
           return False
    return True




def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    k = ""
    for i in secretWord:
         if i in lettersGuessed:
             k += i
         else:
             k += " _ "
    return k


def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    s = 'abcdefghijklmnopqrstuvwxyz'
    k = ''
    for i in s:
        if i not in lettersGuessed:
            k += i
    return k

def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    print('      ', 'Welcome to the game Hangman!', '      ')
    print('I am thinking of a word that is', str(len(secretWord)), ' letters long.')
    lettersGuessed = ''
    gl = 8
    print('............')
    print(' ')
    while True:
        print('You have ', gl, ' guesses left.')
        print('Available letters: ',getAvailableLetters(lettersGuessed))
        y = str(input('Please guess a letter: '))
        if y in secretWord and y not in lettersGuessed:
            lettersGuessed += y
            print('Good guess: ', getGuessedWord(secretWord, lettersGuessed))
            print(' ')       
        elif y in lettersGuessed:
            print("Oops! You've already guessed that letter: ", getGuessedWord(secretWord, lettersGuessed))
            print(' ')     
        else:
            lettersGuessed += y
            print ("Oops! That letter is not in my word: ", getGuessedWord(secretWord, lettersGuessed))
            print(' ')
            gl -= 1
        print ("............")
        print(' ')
        if gl <= 0:
            print ("Sorry, You've ran out of guesses. The word was ", secretWord, ".")
            print(' ')
            break
        if isWordGuessed(secretWord, lettersGuessed):
            print ("Congratulations! You've won!")
            print(' ')
            break

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)    
   