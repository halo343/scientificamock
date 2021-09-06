import random as rnd


def list_tostr(list):
    string = ''
    for element in list_:
        string += element
    return string


movies = ['The Dark Knight Rises', "Inception", "The Emoji Movie", "Godzilla vs Kong", "Justice League", "Army of the Dead",
          "Doctor Strange", "Sholay", 'Avatar', "Deadshot", "Star Trek", "Star Wars", "Deadpool", "Dabang", "Tiger Zinda Hai",
          "Ant Man"]

letters = 'abcdefghijklmnopqrstuvwxyz'

run = True
attempts = 0
max_attempts = 5
answer = rnd.choice(movies).casefold()

display_thing = ''

for stuff in answer:
    if stuff not in 'aeiou ':  # rnd.randint(1, 100) < 70 and stuff not in 'aeiou':
        displaything += ''
    else:
        display_thing += stuff

# print(display_thing)  #TODO: remove print statement
answer_list = list(answer)

while run:
    print(display_thing + '\n')

    guess = input("Guess a letter: ").casefold()

    # Wrong Input
    if len(guess) != 1 or guess not in letters:
        print("Please enter a single alphabet")
        pass

    display_list = list(display_thing)

    if guess in answer_list:
        for index in range(len(display_list)):
            if guess == answer_list[index]:
                display_list[index] = guess
    else:
        print()
        attempts += 1
        print(f"Sorry, that letter is not in the answer, You have {max_attempts-attempts} guesses left.")

        if attempts == max_attempts:
            print(f"You Lose :(\nThe correct answer was: {answer}")
            break

    display_thing = list_to_str(display_list)

    if display_thing == answer:
        print(answer + '\n')
        print("Congratulations, you did it! :D")
        run = False