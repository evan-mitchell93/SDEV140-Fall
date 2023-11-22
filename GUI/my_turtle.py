import turtle

#Constants
#turtle position for drawing text
TEXT_POS = (-100,100)
#turtle position to draw hangman
IMAGE_POS = (100,150)
#Flag for won game
WIN = False

#start players with 0 misses
misses = 0

#Player enters a secret word
secret_word = turtle.textinput("Secret","Enter a word").lower()
num_chars = len(secret_word)
correct_letters = []

#hide the default turtle shape
turtle.hideturtle()
turtle.up()
#move turtle to starting position for text
turtle.goto(TEXT_POS[0],TEXT_POS[1])
#display blanks for each character in the secret
starting = "_ " * num_chars
#write the _ _ _ _ to the screen
turtle.write(starting,font=("Arial",20,"normal"))

#will be used to draw the hangman image on bad guesses
def draw_img(count):
    #for now do nothing
    pass

while misses < 8 and WIN == False:
    guess = turtle.textinput("Guess","Guess a letter in the word").lower()
    if guess in secret_word:
        correct_letters.append(guess)
    else:
        misses += 1
        draw_img(misses)
    
    output = ""
    #add a letter or an underscore to the output
    for letter in secret_word:
        if letter in correct_letters:
            output = output + letter + " "
        else:
            output = output + "_ "
    turtle.clear()
    turtle.goto(TEXT_POS[0],TEXT_POS[1])
    turtle.write(output,font=("Arial",20,"normal"))

    #if all letters have been guessed, there will be no "_ " in the output
    if "_ " not in output:
        WIN = True
        turtle.Screen().bgcolor = "blue"
turtle.mainloop()