import turtle

secret_word = turtle.textinput("Secret","Enter a word")
num_chars = len(secret_word)
correct_letters = []

"""t.up()
t.goto(-50,-100)
for i in range(num_chars):
    t.down()
    t.forward(25)
    t.up()
    t.forward(10)"""

turtle.hideturtle()
starting = turtle.write("_ " * num_chars)
turtle.write(starting)
misses = 0
while misses < 8:
    guess = turtle.textinput("Guess","Guess a letter in the word")
    if guess in secret_word:
        correct_letters.append(guess)
    else:
        misses += 1
    
    output = ""
    for letter in secret_word:
        if letter in correct_letters:
            output = output + letter
        else:
            output = output + "_"
    #turtle.write(output)
turtle.mainloop()