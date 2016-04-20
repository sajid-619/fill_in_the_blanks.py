sample = '''A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.'''

# The answer for ___1___ is 'function'. Can you figure out the others?
# ___2___ => 
# ___3___ => 
# ___4___ => 

level_1 = ''''''

level_2 = ''''''

level_3 = ''''''

word_list = ['___1___', '___2___', '___3___', '___4___']
# We've also given you a file called fill-in-the-blanks.pyc which is a working version of the project.
# A .pyc file is a Python file that has been translated into "byte code".
# This means the code will run the same as the original .py file, but when you open it
# it won't look like Python code! But you can run it just like a regular Python file
# to see how your code should behave.

# Hint: It might help to think about how this project relates to the Mad Libs generator you built with Sean.
# In the Mad Libs generator, you take a paragraph and replace all instances of NOUN and VERB.
# How can you adapt that design to work with numbered blanks?

# If you need help, you can sign up for a 1 on 1 coaching appointment: https://calendly.com/ipnd1-1/20min/

# Checks if a word in the word list is a substring of the word passed in.
def word_in_wl(word, word_list)
    for i in word_list
        if i in word
            return i
    return None
    
# Plays a full game of fill-in-the-blanks. Player is prompted to replace words in sample, 
# which appear in word_list with their own words.
def blank_game(sample, word_list)    
    replaced = []
    sample = sample.split()
    for word in sample
        replacement = word_in_wl(word, word_list)
        if replacement != None
            user_input = raw_input('Fill in the blank'  + replacement + )
            word = word.replace(replacement, user_input)
            replaced.append(word)
        else
            replaced.append(word)
    replaced =  .join(replaced)
    return replaced

print blank_game(sample, word_list)
