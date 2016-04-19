blanks_to_fill = ["___1___", "___2___", "___3___", "___4___"]

sample_1 = 'When you ride your ___1___, you should always wear an ___2___ to protect your ___3___. ___2____s must respect very strict ___4___ and controls in order to be considered safe. '

answer_sample_1 = ['bicycle', 'helmet', 'head', 'regulations']

sample_2= 'A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you don t specify the value to return. ___2___ can be standard data types such as string, number, dictionary, tuple, and ___4___ or can be more complicated such as objects and lambda functions.'

answer_sample_2 = ['function', 'variables', 'outputs', 'lists']

sample_3 = 'Are you considered an ___1___ ? Do you love listening to music, any kind of music? Music has played an important role in cultural, traditions and societies for ___2___. But, was this wonderful sound first ___3___ and become one of largest ___4___ grossing industries in America? In 1877 the U.S. inventor Thomas Alva Edison heard "Mary had a little lamb"'

answer_sample_3 = ['audiophile', 'centuries', 'emit', 'capital']

def choose_level():
    levels_available = ['easy', 'medium', 'hard']
    print "Welcome to Federico's fill in the blanks game."
    level = raw_input("Choose a level between easy, medium or hard: ")
    if level == 'easy':
        return sample_1, answer_sample_1#print won't allow the computer to remember the output of this function. Return
    elif level == 'medium':
        return sample_2, answer_sample_2
    elif level == 'hard':
        return sample_3, answer_sample_3
	'''in case the user choose a level that is not available, I want to rerun the choose level function'''
    n = 0
    while level not in levels_available:
        print "The level you have chosen is not among those available."
        level = raw_input("Choose a level between easy, medium or hard: ")
        n += 1
        if n == 3:
            print "As you are unable to choose a level, I doubt you could solve the quiz. Goodbye!"
            return
    if level == 'easy':
        return sample_1, answer_sample_1
    elif level == 'medium':
        return sample_2, answer_sample_2
    elif level == 'hard':
        return sample_3, answer_sample_3

def word_in_pos(blank, parts_of_sample):
    for pos in parts_of_sample:
        if pos in blank:
            return pos
    return None

def play_again():
    user_play_again = raw_input("Would you like to play again? Please enter yes or no: ")
    if user_play_again == "yes":
        play_game()
    else:
        print "Ok, was nice playing with you."
       
def play_game():
    sample, answer = choose_level()
    print sample
    blank_nr = 0
    while blank_nr < len(answer):
        user_answer = raw_input("What should go in the blank nr." + str(blank_nr + 1) + "?")
        if user_answer == answer[blank_nr]:
            print "Correct!"
            sample = sample.replace(blanks_to_fill[blank_nr], user_answer, 3)
            print sample
            blank_nr += 1
            if blank_nr == len(answer):
                print "Congratulations you have completed the game!!!"
                play_again()
        else:
            print "This is not the correct answer. Try again"

play_game()
