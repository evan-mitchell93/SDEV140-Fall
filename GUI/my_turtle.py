import turtle

#Constants
#turtle position for drawing text
TEXT_POS = (-100,100)
#turtle position to draw hangman
IMAGE_POS = (-50,300)
#Flag for won game
WIN = False

text_t = turtle.Turtle()
img_t = turtle.Turtle()
img_t.color("red")
img_t.hideturtle()
img_t.penup()
img_t.speed(100)
#start players with 0 misses
misses = 0

#Player enters a secret word
secret_word = turtle.textinput("Secret","Enter a word").lower()
num_chars = len(secret_word)
correct_letters = []

#hide the default turtle shape
text_t.hideturtle()
text_t.up()
#move turtle to starting position for text
text_t.goto(TEXT_POS[0],TEXT_POS[1])
#display blanks for each character in the secret
starting = "_ " * num_chars
#write the _ _ _ _ to the screen
text_t.write(starting,font=("Arial",20,"normal"))

#will be used to draw the hangman image on bad guesses
def draw_img(count):
    #for now do nothing
    if count == 1:
        img_t.goto(IMAGE_POS[0],IMAGE_POS[1])
        img_t.pendown()
        img_t.right(90)
        img_t.circle(15,None,100)
        img_t.penup()
    elif count == 2:
        img_t.goto(IMAGE_POS[0] + 15,IMAGE_POS[1]-15)
        img_t.pendown()
        img_t.forward(70)
        img_t.right(180)
        img_t.forward(50)
        img_t.penup()
    elif count == 3:
        img_t.right(135)
        img_t.pendown()
        img_t.forward(30)
        img_t.penup()
        img_t.right(180)
        img_t.forward(30)
    elif count == 4:
        img_t.pendown()
        img_t.left(90)
        img_t.forward(30)
        img_t.penup()
        img_t.right(180)
        img_t.forward(30)
        img_t.right(135)
    elif count == 5:
        img_t.forward(50)
        img_t.pendown()
        img_t.left(45)
        img_t.forward(30)
        img_t.penup()
        img_t.right(180)
        img_t.forward(30)
    elif count == 6:
        img_t.left(90)
        img_t.pendown()
        img_t.forward(30)
        img_t.penup()


while misses < 7 and WIN == False:
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
    text_t.clear()
    text_t.goto(TEXT_POS[0],TEXT_POS[1])
    text_t.write(output,font=("Arial",20,"normal"))

    #if all letters have been guessed, there will be no "_ " in the output
    if "_ " not in output:
        WIN = True
        text_t.clear()
        text_t.write("You won", font=("Arial",28,"normal"))
turtle.mainloop()
